from typing import Literal

from .base import _attr_value,command_str
from ._entity_infor import entity_type


class target_attrs:
    X=_attr_value("x",lambda x : x,"~")
    Y=_attr_value("y",lambda y : y,"~")
    Z=_attr_value("z",lambda z : z,"~")
    r=_attr_value("r",lambda r : r,0)
    l=_attr_value("r",lambda l : l,0)
    rm=_attr_value("rm",lambda rm : rm,0)
    lm=_attr_value("lm",lambda lm : lm,0)
    c=_attr_value("c",lambda c : c,0)
    name=_attr_value("name",lambda name="steve",alive=True : name if alive else f"!{name}","steve")
    class m:
        adventure=_attr_value("m",lambda x:"adventure" if x else f"!adventure","adventure")
        creative=_attr_value("m",lambda x:"creative" if x else f"!creative","creative")
        default=_attr_value("m",lambda x:"default" if x else f"!default","default")
        spectator=_attr_value("m",lambda x:"spectator" if x else f"!spectator","spectator")        
        survival=_attr_value("m",lambda x:"survival" if x else f"!survival","survival")
    dx=_attr_value("dx",lambda dx : dx,0)
    dy=_attr_value("dy",lambda dy : dy,0)
    dz=_attr_value("dz",lambda dz : dz,0)
    rx=_attr_value("rx",lambda x : x,0)
    rxm=_attr_value("rxm",lambda x : x,0)
    ry=_attr_value("ry",lambda x : x,0)
    rym=_attr_value("rym",lambda x : x,0)
    class Type(entity_type):
        ...
    tag=_attr_value("tag",lambda x:x,"admin")

    def _score(*attr_and_value,**attr_and_value_dict) -> None:
        '''Use:
        >>> score(attr_1,value_1)
        >>> score(attr_1,value_1,attr_2,value_2)
        >>> score(attr_1=value_1,attr_2=value_2)
        >>> test={
            "scoreboard_1":"!..5",
            "scoreboard_2":1,
            }
            score(**test)
        '''
        attr_str=""
        if attr_and_value:
            for i in range(0,len(attr_and_value),2):
                score_name=attr_and_value[i]
                score=attr_and_value[i+1]
                attr_str+=f"{score_name}={score},"
            attr_str="{"+attr_str[:-1]+"}"
        return attr_str

    score = _attr_value("scores",_score,"？你发现了盲点")
            
    
    #待实现
    class familly:
        ...
    class hasitem:
        ...

for i in dir(entity_type):
    if i.startswith("__"):
        continue
    else:
        setattr(target_attrs.Type,i,_attr_value("type",lambda x:x,i))

target_obj=Literal["@e","@a","@s","@r","@p","*"]
score_oper_hanld=Literal["%=","*=","+=","-=","/=","<","=",">","><"]

class target(target_attrs):
    '''目标选择器'''
    def __init__(self,obj:target_obj,*args:target_attrs) -> None:
        attr=""
        if args:
            for i in args:
                i:_attr_value
                attr+=f'''{i.attr}={i},'''
            attr = f"[{attr[:-1]}]"
        self.target_str=command_str(obj,attr)
