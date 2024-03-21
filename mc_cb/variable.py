from ._block_infor import block_list
from .tools import command_str,_attr_value
from typing import Callable

class fill_handle:
    '''填充时旧方块的处理方式'''
    destory='destory'
    '''破坏原有方块变为掉落物'''
    hollow='hollow'
    '''填充未空心长方体'''
    keep='keep'
    '''仅替换空气方块'''
    outline='outline'
    '''仅替换外层方块'''
    replace='replace'
    '''替换指定方块'''        
    
class _clone_handle_attr:
    '''clone 模式副属性'''
    def __init__(self,handle:str=None,block_bit:bool=False) -> None:
        self._handle=handle
        self._block_bit=block_bit
    
    def _tmp(self,handle_attr,block:block_list):
        if self._block_bit:  return f"{self._handle} {handle_attr} {block}"
        else:   return f"{self._handle} {handle_attr}"
        
    def normal(self,block:block_list=block_list.iron_block):
        '''不执行force 与 move'''
        return self._tmp("normal",block)
    
    def force(self,block:block_list=block_list.iron_block):
        '''强制复制'''
        return self._tmp("force",block)

    def move(self,block:block_list=block_list.iron_block):
        '''将源区域移动到目标区域'''
        return self._tmp("move",block)
        
class clone_handle:
    '''clone 模式'''
    fillered=_clone_handle_attr(handle="fillered",block_bit=True)
    '''仅复制符合方块ID的方块'''
    masked=_clone_handle_attr(handle="masked")
    '''仅复制非空气方块'''
    replace=_clone_handle_attr(handle="replace")
    '''复制所有方块'''

class target_attrs:
    X=_attr_value("x",lambda x : x,"~")
    Y=_attr_value("y",lambda y : y,"~")
    Z=_attr_value("z",lambda z : z,"~")
    r=_attr_value("r",lambda r : r,0)
    l=_attr_value("r",lambda l : l,0)
    rm=_attr_value("rm",lambda rm : rm,0)
    lm=_attr_value("lm",lambda lm : lm,0)
    c=_attr_value("c",lambda c : c,0)
    name=_attr_value("name",lambda name : name,"steve")
    not_name=_attr_value("name",lambda name : f'!{name}',"steve")
    class m:
        adventure=_attr_value("m",lambda:"adventure","adventure")
        creative=_attr_value("m",lambda:"creative","creative")
        default=_attr_value("m",lambda:"default","default")
        spectator=_attr_value("m",lambda:"spectator","spectator")
        survival=_attr_value("m",lambda:"survival","survival")
        not_adventure=_attr_value("m",lambda:"!adventure","!adventure")
        not_creative=_attr_value("m",lambda:"!creative","!creative")
        not_default=_attr_value("m",lambda:"!default","!default")
        not_spectator=_attr_value("m",lambda:"!spectator","!spectator")
        not_survival=_attr_value("m",lambda:"!survival","!survival")

class target:
    '''目标选择器'''
    def __init__(self,*args:target_attrs) -> None:
        pass

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
        
    class As:
        ...