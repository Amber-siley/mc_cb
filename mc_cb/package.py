from os import getcwd,rename,mkdir,unlink,walk
from os.path import join,exists,isdir,split,isfile,basename,relpath
from zipfile import ZipFile
from json import dumps,loads
from uuid import uuid1
from typing import Callable
from shutil import make_archive,move,copy,copytree,rmtree
from zipfile import ZipFile
from math import ceil

from .define import _TMP_FUNCTION
from .base import _attr_value,tmp_function
from .commands import execute,scoreboard,Function,schedule
    
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
        is_live=exists(self.file_path)
        if is_live and exist:
            run = True
        elif not is_live:
            run = True
        else:
            run = False
        if run:
            with open(self.file_path,"w",encoding='utf-8') as fp:
                content=dumps(content,indent=4)
                fp.write(content)

    def read(self):
        with open(self.file_path,mode="r",encoding="utf-8") as fp:
            return loads(fp.read())
        
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
        min_engine_version=_attr_value("",lambda _list:_list,[1,20,0],True)
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
        self.create_behavior_pack()
        
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
        manifest_json.write(self.MANIFEST._manifest_dict)
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
    
    def add_func(self,is_alive:bool=False,is_repeat:bool=False,save_tree:str=None,func_name=False,opertimizing:bool=False,*condition:Callable):
        '''装饰器'''
        def tmp_1(function:Callable,*args, **kwargs):
            name=func_name
            if not func_name:
                name=function.__name__
            if is_repeat:
                self.tick(name)
            def tmp_2():
                function(*args, **kwargs)
                self.write_function(save_tree,name,opertimizing=opertimizing)
                tmp_function.cls()
            tmp_2()
            return tmp_2
        return tmp_1
    
    def write_function(self,save_tree:str = None,func_name:str = "test",addon_str:str="",index:int=-1,first_run:bool=True,opertimizing:bool=False):
        if save_tree:
            self.mkdir(join(self.function_path,save_tree),True)
            #函数文件的保存路径
            func_save_tree=join(self.function_path,save_tree)
            #执行函数的名称
            function_name = f"{save_tree}/{func_name}{addon_str}"
        else:
            func_save_tree=self.function_path
            function_name = f"{func_name}{addon_str}"
        #函数文件的路径
        if index != -1:
            addon_str = f"_{str(index)}"
        index += 1
        func_path=join(func_save_tree,f"{func_name}{addon_str}.mcfunction")
        fp = open(func_path,"w+",encoding="utf-8")
        
        def write_now(command):
            fp.write("\n")
            if isinstance(command,str):
                fp.write(command)
            else:
                fp.write(command.command_str)
            tmp_function.Del(-1)
            
        if len(_TMP_FUNCTION) <= 10000:
            fp.write("\n".join(_TMP_FUNCTION))
            if not first_run and opertimizing:
                write_now(scoreboard(scoreboard.obj.remove(func_name)))
        else:
            if first_run and opertimizing:
                tmp_function.Tmp_storage()
                name=func_name
                scoreboard(scoreboard.obj.add(name,f"{name}_Display"))
                # scoreboard(scoreboard.obj.setdisplay.sidebar(name))
                scoreboard(scoreboard.player.Set(scoreboard.target("@s"),name,0))
                self.write_function(save_tree=save_tree,func_name=func_name)
                tmp_function.cls()
                tmp_function.Tmp_storage()
                index_len=ceil(len(_TMP_FUNCTION)/9997)
                tmp_function.Tmp_storage()
                self.SystemRunFunction(function_name,f"{func_name}",index_len)
                tmp_function.Tmp_storage()
                self.write_function(save_tree,func_name,addon_str,index,False,opertimizing)
            elif opertimizing:
                fp.write("\n".join(_TMP_FUNCTION[:9000]))
                write_now(scoreboard(scoreboard.player.add(scoreboard.target("@s"),func_name,1)))
                tmp_function.cut(9000)
            # write_now(schedule(schedule.handle.cube(),f"{function_name}{addon_str}"))
                fp.close()
                self.write_function(save_tree,func_name,addon_str,index,False,opertimizing)
            elif not opertimizing:
                fp.write("\n".join(_TMP_FUNCTION[:10000]))
                fp.close()
                tmp_function.cut(10000)
                index += 1
                self.write_function(save_tree,func_name,addon_str,index,opertimizing=opertimizing)
            return 0
    
    def tick(self,*adds:str):
        tick_path=join(self.function_path,"tick.json")
        if exists(tick_path):
            tick=json_manage(tick_path).read()
            functions=tick["values"]
        else:
            json_manage(tick_path).write({"values":[]})
            functions=[]
            tick={"values":[]}
        for i in adds:
            functions.append(i)
        tick["values"]=functions
        json_manage(tick_path).write(tick,exist=True)
    
    def SystemRunFunction(self,function:str,name,len_index:int):
        @self.add_func(is_repeat=True,func_name=f"System_{name}")
        def RunFunctionsManage():
            functions=[f"{function}_{i}" for i in range(len_index)]
            for i in range(len(functions)):
                execute(Function(functions[i]),execute.As("@a",execute.As.score[name,i]))
