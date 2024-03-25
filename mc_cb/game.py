"""
和游戏相关，但不直接使用function操作游戏，同时类提供一些功能
"""
from re import findall

class _position:
    def __init__(self,pos:str | list[tuple[str,str]]) -> None:
        self.pos=self.real_pos(pos)
    
    @staticmethod
    def return_pos(pos:list[int],format:list[tuple[str,str]]) ->list[tuple[str,str]]:
        return [(format[index][0],str(value)) for index,value in enumerate(pos)]
    
    @staticmethod
    def pos_type(pos):
        tmp=[i for i,j in pos if i in ["~","^"]]
        if len(tmp) == 3:
            pos_type="relative"
        elif len(tmp) == 0:
            pos_type="absolute"
        else:
            pos_type="unknown"
        return pos_type
        
    @staticmethod
    def real_pos(pos):
        if isinstance(pos,list):
            return pos
        pos_rule="([~,^]?)([-,+]?\d*)"
        postions=findall(pos_rule,pos)
        postions=[(i,j) for i,j in postions if i != "" or j !=""]
        return postions
    
    @staticmethod
    def parse_pos(pos:list[tuple[str,str]]) ->list[int]:
        '''解析坐标（并非真实坐标） -> [x,y,z]'''
        if isinstance(pos[0],int):
            return pos
        return [int(j) if j != "" else 0 for i,j in pos]

class chunk(_position):
    def __init__(self,pos:str | list[tuple[str,str]] | list[int],_chunk_value:int=16,_point_0:list[int]=[0,0]) -> None:
        '''- pos:坐标
        - _chunk_value:想要分割的区块大小'''
        self.pos=self.parse_pos(self.real_pos(pos))
        self._value=_chunk_value
        self._point_0=_point_0

    @property
    def chunk_pos(self) -> tuple[tuple[int],tuple[int]]:
        '''返回当前位置的区块坐标范围'''
        x=self.pos[0]
        y=self.pos[1]
        z=self.pos[2]
        value=self._value
        min_x=x-(x%value) if x >=0 else (-x)%value-1+x
        min_z=z-(z%value) if z >=0 else (-z)%value-1+z
        max_x=min_x+value-1 if min_x >= 0 else min_x-value-1
        max_z=min_z+value-1 if min_z >= 0 else min_z-value-1
        min_pos=(min_x,y,min_z)
        max_pos=(max_x,y,max_z)
        return min_pos,max_pos
    
class Map(_position):
    '''地图'''
    def __init__(self,pos:str | list[tuple[str,str]] | list[int],level:int=0) -> None:
        '''- pos:坐标
        - level:地图等级 0-4'''
        self.pos=self.parse_pos(self.real_pos(pos))
        if level in range(5):
            self.level=level
        else:
            raise ValueError("应为0~4")
    
    @property
    def map_pos(self):
        chunk_value=4*2**self.level
        min_pos,max_pos = chunk(self.pos,chunk_value).chunk_pos
        