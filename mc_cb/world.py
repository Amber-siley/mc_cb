from typing import Literal

from .base import command_str,tmp_function
from .game import position
from .variable import target,score_oper_hanld

class schedule_handle:
    def cube(xyz_1:str | list[int]="~~~",xyz_2:str | list[int]="~~~"):
        '''长方体加载时执行'''
        xyz_1=str(position(xyz_1))
        xyz_2=str(position(xyz_2))
        return command_str(xyz_1,xyz_2)
        
    def circle(xyz:str | list[int],r:int):
        '''球形区域加载时执行'''
        r= str(r)
        xyz=str(position(xyz))
        return command_str("circle",xyz,r)
        
    def tickingarea(chunk_name:str):
        '''常加载区块'''
        return command_str("tickingarea",chunk_name)

class scoreboard_obj:
    def List():
        return command_str("objectives","list")
    
    def add(name:str,show_name:str):
        return command_str("objectives","add",name,"dummy",show_name)
    
    def remove(name:str):
        return command_str("objectives","remove",name)
    
    class setdisplay:
        def _ending(name:str,display:str,ascending:bool=True):
            '''- name 计分版名称
            - ascending 是否为升序'''
            if ascending:
                ending="ascending"
            else:
                ending="descending"
            return command_str("objectives","setdisplay",display,name,ending)
        
        def List(name:str,ascending:bool=True):
            return scoreboard_obj.setdisplay._ending(name,"list",ascending)
        
        def sidebar(name:str,ascending:bool=True):
            return scoreboard_obj.setdisplay._ending(name,"sidebar",ascending)
        
        def belowname(name:str,ascending:bool=True):
            return scoreboard_obj.setdisplay._ending(name,"belownname",ascending)

class scoreboard_player:
    def List(obj:target):
        return command_str("players list",obj.target_str)
    
    def Set(obj:target,name:str,value:int):
        return command_str("players set",obj.target_str,name,value)
    
    def add(obj:target,name:str,value:int):
        return command_str("players add",obj.target_str,name,value)
    
    def remove(obj:target,name:str,value:int):
        return command_str("players remove",obj.target_str,name,value)
    
    def test(obj:target,name:str,min:int="*",max:int="*"):
        return command_str("players test",obj.target_str,name,min,max)
    
    def random(obj:target,name:str,min:int=0,max:int=100):
        return command_str("players random",obj.target_str,name,min,max)
    
    def reset(obj:target,name:str):
        return command_str("players reset",obj.target_str,name)
    
    def operation(obj_1:target,name_1:str,handle:score_oper_hanld,obj_2:target,name_2):
        return command_str("players operation",obj_1.target_str,name_1,handle,obj_2.target_str,name_2)

class schedule:
    def __init__(self,schedule_handle:schedule_handle,func_name:str) -> None:
        self.command_str=command_str("schedule on_area_loaded add",schedule_handle,func_name)
        tmp_function.add(self.command_str)
    
    class handle(schedule_handle):
        ...

class scoreboard:
    def __init__(self,scoreboard_handle:scoreboard_obj | scoreboard_player) -> None:
        self.command_str=command_str("scoreboard",scoreboard_handle)
        tmp_function.add(self.command_str)
    
    class obj(scoreboard_obj):...
    class player(scoreboard_player):...
    class target(target):...
    
class Function:
    def __init__(self,func_name:str) -> None:
        self.command_str=command_str("function",func_name)
        tmp_function.add(self.command_str)