from typing import Callable,Any
from math import sqrt
from .define import _TMP_FUNCTION
from numba import jit

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
        self.final_value=self.getitem(key)
        return self.getitem(key)

    @property
    def get(self) -> Any:
        if self.inherited and self.final_value:
            return self.final_value
        return self.default

    def __str__(self) -> str:
        return str(self.get)
    
def command_str(*commands):
    '''按照给与的字符串生成指令'''
    return_data=""
    max=len(commands)
    for index,tmp in enumerate(commands):
        return_data+=str(tmp)
        if index+1<max: return_data+=" "
    return return_data

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

@jit(nopython=True,cache=True)
def _color_distance_formula(R_mean,R,G,B):
    return sqrt((2+R_mean/156)*(R**2)+4*(G**2)+(2+(256-R_mean)/256)*(B**2))

def color_distance(rgb_1:tuple[int] | list[int],rgb_2:tuple[int] | list[int]):
    '''颜色差异，加权欧式距离'''
    R_mean=(rgb_1[0]+rgb_2[0])/2
    R,G,B=[rgb_1[i]-rgb_2[i] for i in range(3)]
    return _color_distance_formula(R_mean,R,G,B)