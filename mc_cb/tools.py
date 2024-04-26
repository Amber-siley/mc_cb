"""
通过function执行更改游戏的类与方法
"""

from math import sqrt
import PIL.JpegImagePlugin
from functools import cache
from PIL import Image
import numpy as np
from tqdm import tqdm

from .game import position_list
from ._block_infor import color_block_62
from .commands import setblock

class cb_image:
    '''对图像进行处理'''
    def __init__(self,file:str | PIL.JpegImagePlugin.JpegImageFile,width:int=None,height:int=None,quality:int=5) -> None:
        self.file=file
        self.image_quality=quality
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
    
    def setblock(self,pos_1: str | list[int],pos_2: str | list[int]=None,need_cut:bool=False,color_dict:dict=color_block_62,map_mode:bool=False):
        '''在世界中放置像素画
        - pos_1 起始坐标
        - pos_2 终点坐标
        - need_cut 是否裁切超出范围的图像部分
        - color_dict 方块名称与方块颜色RGB值的对照字典 {"block_name":(R,B,G)} r,g,b：int
        - map_mode 是否启用在手持地图上显示更加真实的模式'''
        tmp_dis = None
        pos_1 = position_list.parse_pos(pos_1)
        pos_2 = position_list.parse_pos(pos_2)
        poss = position_list(pos_1,pos_2)
        
        if not poss.isSamePlane:
            raise ValueError(f"{pos_1},{pos_2}坐标不在一个平面")
        if poss.vector()[1] != 0:
            height = poss.len_y
            width = poss.len_z if poss.len_x == 1 else poss.len_x
        else:
            height = poss.len_x
            width = poss.len_z
        
        png = cb_image(self.png)
        if need_cut:
            #裁切
            png.RGB = png.RGB[:height-1,:width-1]
        else:
            #不剪切
            height = png.height
            width = png.width
            x,y,z = 0,0,0
            
            if tmp := poss.vector_y()[1]:
                y = tmp/abs(tmp)*(height-1)
                if tmp := poss.vector_x()[0]:
                    x = tmp/abs(tmp)*(width-1)
                
            if tmp := poss.vector_z()[2]:
                z = tmp/abs(tmp)*(height-1)
                if tmp := poss.vector_x()[0]:
                    x = tmp/abs(tmp)*(width-1)
            
            pos_2 = list(map(int,[x + pos_1[0],y + pos_1[1],z + pos_1[2]]))
            poss = position_list(pos_1,pos_2)

            if poss.vector()[1]:
                positions = iter(poss.positions[-1::-1])
            else:
                positions = iter([j for i in poss.lines for j in i])
        
        if map_mode:
            if poss.vector()[1] == 0:
                raise ValueError(f"地图模式需平铺像素画，而不是垂直于水平面")
            ...
        else:
            for i in tqdm(range(height)):
                for j in tqdm(range(width),leave=False):
                    rgb_1 = tuple(png.RGB[i][j])
                    for name,rgb in color_dict.items():
                        co_dis = self.color_distance(rgb_1,rgb)
                        if tmp_dis == None:
                            tmp_dis = co_dis
                            tmp_name = name
                        if tmp_dis  > co_dis:
                            tmp_dis = co_dis
                            tmp_name = name
                    tmp_dis = None
                    pos = next(positions)
                    setblock(pos,tmp_name)

    @staticmethod
    @cache
    def _color_distance_formula(R_mean,R,G,B):
        return sqrt((2+R_mean/156)*(R**2)+4*(G**2)+(2+(256-R_mean)/256)*(B**2))

    @staticmethod
    @cache
    def color_distance(rgb_1:tuple[int],rgb_2:tuple[int]):
        '''颜色差异，加权欧式距离'''
        R_mean=(rgb_1[0]+rgb_2[0])/2
        R,G,B=[rgb_1[i]-rgb_2[i] for i in range(3)]
        return cb_image._color_distance_formula(R_mean,R,G,B)