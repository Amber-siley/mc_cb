from os import getcwd,makedirs,mkdir
from os.path import join,exists
from zipfile import ZipFile
from tkinter.filedialog import askdirectory
from json import dumps
from uuid import uuid1
from typing import Callable
from .variable import _TMP_FUNCTION
from shutil import make_archive

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
        make_archive(new_path,"zip",raw_path)
    
    @staticmethod
    def mkdir(path,exist:bool=False):
        if exist:
            if exists(path):
                return 0
        try:
            mkdir(path)
        except:
            ...
            
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
    def __init__(self) -> None:
        self.format_version=1
        self.header={"description":"description","name":"behavior_pack","uuid":str(uuid1()),"version":[1,0,0],"min_engine_version":[1,13,0]}
        '''
        索引     and        值
        - description       " "
        - name              " "
        - uuid              " "
        - version           [1,0,0]
        - min_engine_version[1,13,0]'''
        self.modules={"description":"description","type":"data","uuid":str(uuid1()),"version":[1,0,0]}
        '''
        索引     and        值
        - description   " "
        - type     "data" or "resource"
        - uuid          " "
        - version       [1,0,0]'''
        self.dependencies={"uuid":None,"version":[1,0,0]}
        '''
        索引     and        值
        - uuid      " "
        - version   [1,0,0]'''
    
    @property
    def _manifest_dict(self):
        _manifest_dict={'format_version':self.format_version,"header":self.header,"modules":[self.modules]}
        if self.dependencies['uuid']:
           _manifest_dict["dependencies"]=[self.dependencies]
        return _manifest_dict

class behavior_pack(file_manage):
    '''行为包管理'''
    def __init__(self,work_path:str=getcwd()) -> None:
        super().__init__(work_path)
        self.FILE_NAME='init'
        '''行为包文件夹或者行为包名称'''
        self.MANIFEST=_manifest()
        
    @property
    def function_path(self):
        return join(self.behavior_path,"functions")
    
    def create_behavior_pack(self):
        self.behavior_path=join(self.work_path,self.FILE_NAME)
        self.mkdir(self.behavior_path,True)
        self.mkdir(self.function_path,True)
        self.touch('pack_icon.png',self.behavior_path,True)
        self.manifest_path=join(self.behavior_path,'manifest.json')
        manifest_json=json_manage(self.manifest_path)
        manifest_json.write(self.MANIFEST._manifest_dict,True)

    def create_behavior_mcaddon(self):
        self.create_behavior_pack()
        self.zip(join(self.work_path,self.FILE_NAME),self.behavior_path)
        
    
    def read_hehavivor_pack(self,behavior_path:str=None):
        '''- behavior_path 行为包包路径
        \n默认为空则为手动选择'''
        if not behavior_path:   behavior_path=askdirectory()
    
    def add_func(self,is_alive:bool=False,is_repeat:bool=False,save_tree:tuple[str]=(""),*condition:Callable):
        '''装饰器'''
        def tmp_1(function:Callable,*args, **kwargs):
            def tmp_2():
                function(*args, **kwargs)
                func_path=join(self.function_path,save_tree,f"{function.__name__}.mcfunction")
                with open(func_path,"w+",encoding="utf-8") as fp:
                    for command in _TMP_FUNCTION:
                        fp.write(f"{command}\n")
                    tmp_function.cls()
            tmp_2()
            return tmp_2
        return tmp_1
    
class tmp_function:
    '''暂时存储指令列表'''
    global _TMP_FUNCTION
    @staticmethod
    def add(command_str:str):
        '''添加'''
        _TMP_FUNCTION.append(command_str)
        
    @staticmethod
    def cls():
        '''清除'''
        _TMP_FUNCTION.clear()
    
class tick:
    tick={"values":[]}
    
    def add(function):
        def add_1(*args, **kwargs):
            ...
    
def command_str(*commands):
    '''按照给与的字符串生成指令'''
    return_data=""
    max=len(commands)
    for index,tmp in enumerate(commands):
        return_data+=str(tmp)
        if index+1<max: return_data+=" "
    return return_data
