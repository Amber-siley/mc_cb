from typing import Any
from mc_cb._block_infor import _block_list,_block_status

_TMP_NAME=''
_TMP_FUNCTION=[]

class _block_name:
    def __init__(self,name) -> None:
        self._name=name
        global _TMP_NAME
        _TMP_NAME=name
        
    def __str__(self) -> str:
        return self._name

    def _command_attr_park(self,**kwargs) ->tuple[str,str]:
        '''返回mc指令方块名称以及属性部分的字符串类型'''
        re_str=''
        kwargs={i:j for i,j in kwargs.items() if j != None}
        max=len(kwargs)
        for id,args in enumerate(kwargs.items()):
            _attr,index=args
            options=self.__getattribute__(_attr)
            option=options.optional[index]
            attr=options.attr
            if isinstance(option,bool) or isinstance(option,int):
                re_str=re_str+f'''"{attr}"={option}'''
            else:
                re_str=re_str+f'''"{attr}"="{option}"'''
            if id+1 != max:  re_str=re_str+","
        re_str=f'''[{re_str}]'''
        return f'''{self._name} {re_str}'''
    
class _get_block_attr:
    def __init__(self,attrs:dict) -> None:
        self.block=_TMP_NAME
        self.attr,self.optional=list(attrs.items())[0]
        
    def __getitem__(self,index:int) -> tuple[str,str]:
        return self._command_attr_park(index)
    
    def _command_attr_park(self,index:int):
        '''返回mc指令方块属性部分的字符串类型'''
        option=self.optional[index]
        if isinstance(option,bool) or isinstance(option,int):
            attr_park=f'''["{self.attr}"={option}]'''
        else:
            attr_park=f'''["{self.attr}"="{option}"]'''
        return f'''{self.block} {attr_park}'''

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

class block_list(_block_list):
    '''方块列表'''
    '''这里这么写是方便代码'''
    class _anvil(_block_name):
        def __init__(self, name) -> None:
            super().__init__(name)
            self.damage=_get_block_attr(_block_status.damage)
            '''破损程度由低到高 0-3'''
            self.direction=_get_block_attr(_block_status.direction)
            '''朝向 0-3'''
            self.cardinal_direction=_get_block_attr(_block_status.cardinal_direction)
            '''朝向 东南西北 0-3'''
        def set_attr(self,damage:int=None,direction:int=None,cardinal_direction:int=None) ->tuple[str,str]:
            '''- damage 破损程度由低到高 0-3
            - direction 朝向 0-3
            - cardinal_direction 朝向 东南西北 0-3'''
            return self._command_attr_park(damage=damage,direction=direction,cardinal_direction=cardinal_direction)
            
    class _amethyst_cluster(_block_name):
        def __init__(self, name) -> None:   
            super().__init__(name)
            self.facing_direction=_get_block_attr(_block_status.facing_direction)
            '''朝向 0-5'''
            self.block_face=_get_block_attr(_block_status.block_face)
            '''朝向 东南西北上下 0-5'''
        def set_attr(self,facing_direction:int=None,block_face:int=None):
            '''- facing_direction 朝向 上下东南西北 0-5
            - block_face 朝向 上下东南西北 0-5'''
            return self._command_attr_park(facing_direction=facing_direction,block_face=block_face)
    
    anvil=_anvil(_block_list.anvil)
    '''铁砧'''
    amethyst_cluster=_amethyst_cluster(_block_list.amethyst_cluster)
    '''紫水晶簇'''
    
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
        '''将源区域复制到目标区域'''
        return self._tmp("move",block)
        
class clone_handle:
    '''clone 模式'''
    fillered=_clone_handle_attr(handle="fillered",block_bit=True)
    '''仅复制符合方块ID的方块'''
    masked=_clone_handle_attr(handle="masked")
    '''仅复制非空气方块'''
    replace=_clone_handle_attr(handle="replace")
    '''复制所有方块'''