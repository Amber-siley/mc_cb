from mc_cb.variable import target_attrs
from .base import command_str,tmp_function
from .variable import target,target_obj,score_oper_hanld
from typing import Literal

class execute_handle:
    '''execute 子命令'''
    class align:
        '''对坐标进行向下取整'''
        x="align x"
        y="align y"
        z="align z"
        xy="align xy"
        xz="align xz"
        yz="align yz"
        xyz="align xyz"
        
    class anchored:
        '''更改执行基准点'''
        eyes="anchored eyes"
        '''执行为头部'''
        feet="anchored feet"
        ''''执行为腿部'''
        
    class As(target):
        def __init__(self, obj:target_obj, *args: target_attrs) -> None:
            super().__init__(obj, *args)
            self.target_str=command_str("as",self.target_str)
        
    class At(target):
        def __init__(self, obj:target_obj, *args: target_attrs) -> None:
            super().__init__(obj, *args)
            self.target_str=command_str("at",self.target_str)
    
    _type="if"
    class If:
        blocks_type=Literal["all","masked"]
        def block(xyz,block):
            return command_str(execute_handle._type,block)

        def blocks(xyz_1,xyz_2,pos,type:str="all"):
            return command_str(execute_handle._type,xyz_1,xyz_2,pos,type)

        class entity(target):
            def __init__(self, obj:target_obj, *args: target_attrs) -> None:
                super().__init__(obj, *args)
                self.target_str=command_str(execute_handle._type,"entity",self.target_str)
        
        def score(obj_1:target,name_1:str,handle:score_oper_hanld,obj_2:target,name_2):
            return command_str(execute_handle._type,"score",obj_1.target_str,name_1,handle,obj_2.target_str,name_2)
    
    _type="unless"
    class unless(If):...
        
class execute(execute_handle):
    def __init__(self,run,*args:str | execute_handle) -> None:
        attr=""
        for i in args:
            if isinstance(i,str):
                attr+=i
            else:
                attr+=i.target_str
        self.command_str=command_str("execute",attr,"run",run.command_str)
        tmp_function.Del(-1)
        tmp_function.add(self.command_str)
