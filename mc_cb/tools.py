from os import getcwd,makedirs
from os.path import join
from json import dumps
from mc_cb import Define

class file_manage:
    def __init__(self,work_path:str=getcwd()) -> None:
        self.work_path=work_path

    def touch(self,file_name,save_path=None):
        if not save_path:   file_path=join(self.work_path,file_name)
        else:   file_path=join(save_path,file_name)
        with open(file_path,"a") as fp: ...
        return file_path
        
    def save(self,content:bytes | str,file_name:str,save_path=None):
        if isinstance(content,bytes):   mode="wb"
        elif isinstance(content,str):   mode="w"
        if not save_path:   save_path=self.work_path
        file_path=join(save_path,file_name)
        with open(file_path,mode) as fp:    fp.write(content)
        return file_path
    
class json_manage:
    def __init__(self,file_path) -> None:
        self.file_path=file_path
        
    def write(self,content:dict | list):
        with open(self.file_path,"w",encoding='utf-8') as fp:
            content=dumps(content,indent=4)
            fp.write(content)

def command_str(*commands):
    '''按照给与的字符串生成指令'''
    return_data=""
    max=len(commands)
    for index,tmp in enumerate(commands):
        return_data+=str(tmp)
        if index+1<max: return_data+=" "
    return return_data
    
def creat_behavior_pack():
    b_file_manage=file_manage()
    behavior_path=join(b_file_manage.work_path,Define.FILE_NAME)
    function_path=join(Define.FILE_NAME,"functions")
    makedirs(function_path)
    b_file_manage.touch('pack_icon.png',behavior_path)
    manifest_path=join(behavior_path,'manifest.json')
    manifest_json=json_manage(manifest_path)
    manifest_json.write(Define.MANIFEST._manifest_dict)
