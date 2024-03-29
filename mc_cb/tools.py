from typing import Callable,Any
from math import sqrt

import PIL.JpegImagePlugin
from numba import jit
from PIL import Image
import numpy as np

from .define import _TMP_FUNCTION

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
    
class cb_image:
    '''对图像进行处理'''
    def __init__(self,file:str | PIL.JpegImagePlugin.JpegImageFile,width:int=None,height:int=None,quality:int=5) -> None:
        self.file=file
        if isinstance(self.file,str):
            self.png=Image.open(file)
        else:
            self.png=file
        self.png.convert("RGB")
        png=self.png
        if width and height:
            png=png.resize((width,height),quality)
        elif width:
            height=int(png.size[1]*(width/png.size[0]))
            png=png.resize((width,height),quality)
        elif height:
            width=int(png.size[0]*(height/png.size[1]))
            png=png.resize((width,height),quality)
        self.png=png
        self.width,self.height=png.size
        self.png_data=png.getdata()
        self.RGB=np.asarray(self.png_data).reshape(self.height,self.width,3)
    
def command_str(*commands):
    '''按照给与的字符串生成指令'''
    return_data=""
    max=len(commands)
    for index,tmp in enumerate(commands):
        return_data+=str(tmp)
        if index+1<max: return_data+=" "
    return return_data

@jit(nopython=True,cache=True)
def _color_distance_formula(R_mean,R,G,B):
    return sqrt((2+R_mean/156)*(R**2)+4*(G**2)+(2+(256-R_mean)/256)*(B**2))

def color_distance(rgb_1:tuple[int] | list[int],rgb_2:tuple[int] | list[int]):
    '''颜色差异，加权欧式距离'''
    R_mean=(rgb_1[0]+rgb_2[0])/2
    R,G,B=[rgb_1[i]-rgb_2[i] for i in range(3)]
    return _color_distance_formula(R_mean,R,G,B)

