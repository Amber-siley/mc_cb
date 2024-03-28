from os import getcwd,rename,mkdir,unlink,walk
from os.path import join,exists,isdir,split,isfile,basename,relpath
from zipfile import ZipFile
from json import dumps
from uuid import uuid1
from typing import Callable
from shutil import make_archive,move,copy,copytree,rmtree
from zipfile import ZipFile
from .define import _TMP_FUNCTION
from .tools import _attr_value,tmp_function
    
class file_manage:
    def __init__(self,work_path:str=getcwd()) -> None:
        self.work_path=work_path
    
    def touch(self,file_name,save_path=None,exist:bool=False):
        if not save_path:   file_path=join(self.work_path,file_name)
        else:   file_path=join(save_path,file_name)
        if exist:
            is_live=exists(file_path)
        else:
            is_live=False
        if not is_live:
            with open(file_path,"a+") as fp: ...
            return file_path
        
    def save(self,content:bytes | str,file_name:str,save_path=None,exist:bool=False):
        if isinstance(content,bytes):   mode="wb"
        elif isinstance(content,str):   mode="w"
        if not save_path:   save_path=self.work_path
        file_path=join(save_path,file_name)
        if exist:
            is_live=exists(file_path)
        else:
            is_live=False
        if not is_live:
            with open(file_path,mode) as fp:    fp.write(content)
            return file_path

    @staticmethod
    def zip(raw_path,new_path):
        if isdir(new_path):
            zip_file_name=f"{split(new_path)[1]}.zip"
        elif isfile(new_path):
            zip_file_name=basename(new_path)
        dir=split(new_path)[0]
        if isdir(raw_path):
            with ZipFile(join(dir,zip_file_name), 'w', 8) as zipf:
                for root, _, files in walk(raw_path):
                    for file in files:
                        file_path = join(root, file)
                        arcname = relpath(file_path, raw_path)
                        zipf.write(file_path, arcname=arcname)
                return join(dir,zip_file_name)
        else:
            return make_archive(new_path,"zip",raw_path)
    
    @staticmethod
    def mkdir(path,exist:bool=False):
        if exist:
            if exists(path):
                return 0
        try:
            mkdir(path)
        except:
            ...
    
    @staticmethod
    def rename(src,dst):
        if exists(dst):
            unlink(dst)
        rename(src,dst)
        
    def nr_mv(self,old_path,new_path):
        '''not root move'''
        if not exists(new_path):
            move(old_path,new_path)
        else:
            self.cp(old_path,new_path)
            self.rm(old_path)
    
    def mv(self,old_path,new_path):
        if isdir(old_path):
            dir=split(old_path)[-1]
            new_path=join(new_path,dir)
        self.nr_mv(old_path,new_path)
    
    @staticmethod
    def cp(main_path,aim_path):
        if isdir(main_path):
            copytree(main_path,aim_path,dirs_exist_ok=True)
        if isfile(main_path):
            copy(main_path,aim_path)
    
    @staticmethod
    def rm(path):
        if isdir(path):
            rmtree(path)
        if isfile(path):
            unlink(path)
    
class json_manage:
    def __init__(self,file_path) -> None:
        self.file_path=file_path
        
    def write(self,content:dict | list,exist:bool=False):
        if exist:
            is_live=exists(self.file_path)
        else:
            is_live=False
        if not is_live:
            with open(self.file_path,"w",encoding='utf-8') as fp:
                content=dumps(content,indent=4)
                fp.write(content)

class _manifest:
    '''附加包主描述文件
    - format_version
    - header
    - modules
    - dependencies'''
    class _manifest_header:
        name="behavior_pack"
        '''资源包名称'''
        description="description"
        '''简介'''
        uuid=str(uuid1())
        version=_attr_value("",lambda _list:_list,[1,0,0],True)
        '''版本号 Use: \n >>> version[1,2,4] #版本号1.2.4'''
        min_engine_version=_attr_value("",lambda _list:_list,[1,16,0],True)
        '''游戏最低版本 Use: \n >>> min_engine_version[1,16,0] #最低版本1,16,0'''
    
    class _manifest_modules:
        type="data"
        description="description"
        uuid=str(uuid1())
        version=_attr_value("",lambda _list:_list,[1,0,0],True)
    
    class _manifest_depen:
        uuid=None
        version=_attr_value("",lambda _list:_list,[1,0,0],True)
        
    def __init__(self) -> None:
        self.format_version=2
        self.header=self._manifest_header()
        self.modules=self._manifest_modules()
        self.dependencies=self._manifest_depen()
    
    @property
    def _header(self):
        header=self.header
        return {"description":header.description,"name":header.name,"uuid":header.uuid,"version":header.version.get,"min_engine_version":header.min_engine_version.get}
    
    @property
    def _modules(self):
        modules=self.modules
        return {"description":modules.description,"type":modules.type,"uuid":modules.uuid,"version":modules.version.get}
    
    @property
    def _dependencies(self):
        depen=self.dependencies
        return {"uuid":depen.uuid,"version":depen.version.get}
    
    @property
    def _manifest_dict(self):
        _manifest_dict={'format_version':self.format_version,"header":self._header,"modules":[self._modules]}
        if self.dependencies.uuid:
           _manifest_dict["dependencies"]=[self._dependencies]
        return _manifest_dict

class behavior_pack(file_manage):
    '''行为包管理'''
    def __init__(self,name,work_path:str=getcwd()) -> None:
        super().__init__(work_path)
        self.FILE_NAME=name
        '''行为包工程文件夹名称'''
        self.MANIFEST=_manifest()
        self.MANIFEST.header.name=self.FILE_NAME
        
    @property
    def function_path(self):
        return join(self.behavior_path,"functions")
    
    def create_behavior_pack(self) -> str:
        '''创建行为包工程文件夹及其文件'''
        self.behavior_path=join(self.work_path,self.FILE_NAME)
        self.mkdir(self.behavior_path,True)
        self.mkdir(self.function_path,True)
        self.touch('pack_icon.png',self.behavior_path,True)
        self.manifest_path=join(self.behavior_path,'manifest.json')
        manifest_json=json_manage(self.manifest_path)
        manifest_json.write(self.MANIFEST._manifest_dict,True)
        return self.behavior_path

    def build_mcaddon(self):
        '''打包构建附加包的mcaddon格式'''
        tmp_mcaddon_path=join(self.work_path,f"tmp_{self.FILE_NAME}")
        self.mkdir(tmp_mcaddon_path,True)
        self.cp(self.behavior_path,join(tmp_mcaddon_path,self.FILE_NAME))
        zip_path=self.zip(tmp_mcaddon_path,join(self.work_path,self.FILE_NAME))
        file_name=f"{self.FILE_NAME}.mcaddon"
        self.rm(join(tmp_mcaddon_path))
        self.rename(zip_path,file_name)
    
    def add_func(self,is_alive:bool=False,is_repeat:bool=False,save_tree:str=None,*condition:Callable):
        '''装饰器'''
        def tmp_1(function:Callable,*args, **kwargs):
            def tmp_2():
                function(*args, **kwargs)
                self.write_function(save_tree,function.__name__)
                tmp_function.cls()
            tmp_2()
            return tmp_2
        return tmp_1
    
    def write_function(self,save_tree:str = None,func_name:str = "test",addon_str:str="",index:int=0):
        if save_tree:
            self.mkdir(join(self.function_path,save_tree),True)
            func_save_tree=join(self.function_path,save_tree)
        else:
            func_save_tree=self.function_path
        func_path=join(func_save_tree,f"{func_name}{addon_str}.mcfunction")
        fp = open(func_path,"w+",encoding="utf-8")
        global _TMP_FUNCTION
        for i,command in enumerate(_TMP_FUNCTION):
            if i < 9999:
                fp.write(f"{command}\n")
            else:
                addon_str = f"_{str(index)}"
                fp.write(f"function {save_tree}/{func_name}{addon_str}")
                fp.close()
                _TMP_FUNCTION=_TMP_FUNCTION[9999:]
                index += 1
                self.write_function(save_tree,func_name,addon_str,index)
                break
    
    
class tick:
    tick={"values":[]}
    
    def add(function):
        def add_1(*args, **kwargs):
            ...
