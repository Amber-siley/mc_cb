from typing import Callable,Any

from .define import _TMP_FUNCTION,_TMP_STORAGE_FUNCTION_1,_TMP_STORAGE_FUNCTION_2

class _attr_value:
    '''通过index进行设置'''
    def __init__(self,attr:str,format:Callable,default,inherited:bool = False) -> None:
        '''- attr 属性
        - format 通过__getitem__获取参数进行处理的函数
        - default 默认值
        - inherited 是否继承最后一次设置的值'''
        self.attr=attr
        self.getitem=format
        self.default=default
        self.inherited=inherited
        self.final_value=None
    
    def __getitem__(self,key=None):
        if isinstance(key,tuple):
            self.final_value=self.getitem(*key)
            return _attr_value(self.attr,lambda x:x,self.getitem(*key))
        else:
            self.final_value=self.getitem(key)
            return _attr_value(self.attr,lambda x:x,self.getitem(key))

    @property
    def get(self) -> Any:
        if self.inherited and self.final_value:
            return self.final_value
        return self.default

    def __str__(self) -> str:
        return str(self.get)

class tmp_function:
    '''暂时存储指令列表'''
    @staticmethod
    def add(command_str:str):
        '''添加'''
        global _TMP_FUNCTION
        _TMP_FUNCTION.append(command_str)
        
    @staticmethod
    def cls():
        '''清除'''
        global _TMP_FUNCTION
        _TMP_FUNCTION.clear()

    @staticmethod
    def cut(start:int=None,stop:int=None):
        global _TMP_FUNCTION
        if start and stop == None:
            del _TMP_FUNCTION[:start]
        elif start == None and stop:
            del _TMP_FUNCTION[stop:]
        else:
            raise ValueError("only on variable")
    
    @staticmethod
    def Del(index:int):
        global _TMP_FUNCTION
        del _TMP_FUNCTION[index]
    
    @staticmethod
    def Tmp_storage():
        global _TMP_FUNCTION,_TMP_STORAGE_FUNCTION_1,_TMP_STORAGE_FUNCTION_2
        _TMP_STORAGE_FUNCTION_2.clear()
        _TMP_STORAGE_FUNCTION_2.extend(_TMP_FUNCTION)
        _TMP_FUNCTION.clear()
        _TMP_FUNCTION.extend(_TMP_STORAGE_FUNCTION_1)
        _TMP_STORAGE_FUNCTION_1.clear()
        _TMP_STORAGE_FUNCTION_1.extend(_TMP_STORAGE_FUNCTION_2)
    
def command_str(*commands):
    '''按照给与的字符串生成指令'''
    return_data=""
    max=len(commands)
    for index,tmp in enumerate(commands):
        return_data+=str(tmp)
        if index+1<max: return_data+=" "
    return return_data

def overloadfunc(*args, **kwargs):
    def _(function:Callable):
        ...
