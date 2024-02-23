from os import getcwd,makedirs
from os.path import join
from mc_cb import Define

class file_manage:
    def __init__(self,work_path:str=getcwd()) -> None:
        self.work_path=work_path

    def touch(self,file_name):
        file_path=join(self.work_path,file_name)
        with open(file_path,"a") as fp: ...
        return file_path
        
    def save(self,content:bytes | str,file_name:str,save_path=None):
        if isinstance(content,bytes):   mode="wb"
        elif isinstance(content,str):   mode="w"
        if not save_path:   save_path=self.work_path
        file_path=join(save_path,file_name)
        with open(file_path,mode) as fp:    fp.write(content)
        return file_path
    
def creat_behavior_pack():
    b_file_manage=file_manage()
    
    makedirs()
