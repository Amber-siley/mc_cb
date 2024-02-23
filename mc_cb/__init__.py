from uuid import uuid1

class _manifest:
    def __init__(self) -> None:
        self.format_version=1
        self.header={"description":"description","name":"behavior_pack","uuid":str(uuid1()),"version":[1,0,0],"min_engine_version":[1,16,0]}
        '''
        索引     and        值
        - description       " "
        - name              " "
        - uuid              " "
        - version           [1,0,0]
        - min_engine_version[1,16,0]'''
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

###     全局变量    ###      
class _DEFINE:
    def __init__(self) -> None:
        self.FILE_NAME='init'
        '''行为包文件夹或者行为包名称'''
        self.MANIFEST=_manifest()
        '''manifest行为包描述文件'''
        self.MANIFEST.header['name']=self.FILE_NAME

Define=_DEFINE()