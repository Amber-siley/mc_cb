from math import sqrt
import PIL.JpegImagePlugin
from functools import cache
from PIL import Image
import numpy as np
from typing import Callable,overload,Literal

from .game import position
from ._block_infor import color_block_62

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
    
    @property
    def png_data(self):
        return self.png.getdata()
    
    @property
    def width(self):
        return self.png.size[0]
    
    @property
    def height(self):
        return self.png.size[1]
    
    @property
    def RGB(self):
        return np.asarray(self.png_data).reshape(self.height,self.width,3)
    
    image_direction=Literal["x+","x-","y+","y-","z+","z-"]
    image_setblock_mode=Literal["cut","not_cut","resize",""]
    
    def setblock(self,point_1: str | list[int]="~~~",point_2: str | list[int]="~~~",mode:image_setblock_mode="no_cut",direction:image_direction="y+",color_dict:dict=color_block_62,map_mode:bool=False):
        '''在世界中放置像素画
        - point_1,point_2 坐标
        - mode 模式，
            - cut 超出坐标范围剪切
            - not_cut 默认模式，不剪切超出范围的区域
            - resize 缩放，缩放图片大小符合区域大小
        - direction 图像正方向
        - color_dict 方块名称与方块颜色RGB值的对照字典
        - map_mode 是否启用在手持地图上显示更加真实的模式'''
        point_1 = str(position(point_1))
        point_2 = str(position(point_2))
        if mode == "cut":
            self.png = self.png.resize(())
        
    @staticmethod
    def _color_distance_formula(R_mean,R,G,B):
        return sqrt((2+R_mean/156)*(R**2)+4*(G**2)+(2+(256-R_mean)/256)*(B**2))

    @staticmethod
    @cache
    def color_distance(rgb_1:tuple[int],rgb_2:tuple[int]):
        '''颜色差异，加权欧式距离'''
        R_mean=(rgb_1[0]+rgb_2[0])/2
        R,G,B=[rgb_1[i]-rgb_2[i] for i in range(3)]
        return cb_image._color_distance_formula(R_mean,R,G,B)