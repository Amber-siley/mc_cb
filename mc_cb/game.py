"""
和游戏相关，但不直接使用function操作游戏，同时类提供一些功能
"""
from re import findall

class position:
    def __init__(self,pos:str | list[tuple[str,str]] | list[int]) -> None:
        self.pos=self.real_pos(pos)
    
    @staticmethod
    def return_pos(pos:list[int],format:list[tuple[str,str]]) ->list[tuple[str,str]]:
        '''返回坐标列表'''
        return [(format[index][0],str(value)) for index,value in enumerate(pos)]
    
    @staticmethod
    def pos_type(pos):
        '''返回坐标类型'''
        tmp=[i for i,j in pos if i in ["~","^"]]
        if len(tmp) == 3:
            pos_type="relative"
        elif len(tmp) == 0:
            pos_type="absolute"
        else:
            pos_type="unknown"
        return pos_type
        
    @staticmethod
    def real_pos(pos) ->list[tuple[str,str]]:
        '''真实坐标,返回坐标列表'''
        if isinstance(pos,list) or isinstance(pos,tuple):
            if isinstance(pos[0],tuple):
                return pos
            return position.return_pos(pos,[("",""),("",""),("","")])
        pos_rule="([~,^]?)([-,+]?\d*)"
        postions=findall(pos_rule,pos)
        postions=[(i,j) for i,j in postions if i != "" or j !=""]
        return postions
    
    @staticmethod
    def parse_pos(pos:list[tuple[str,str]] | str) ->list[int]:
        '''解析坐标（并非真实坐标） -> [x,y,z]'''
        if isinstance(pos,str):
            pos = position.real_pos(pos)
        if isinstance(pos[0],int):
            return pos
        return [int(j) if j != "" else 0 for i,j in pos]

    def __str__(self) -> str:
        postion=["".join(i) for i in self.pos]
        return " ".join(postion)

class position_list(position):
    def __init__(self,pos_1,pos_2) -> None:
        self.pos_1=pos_1
        self.pos_2=pos_2
        self._index=0
        self.min_x=min(pos_1[0],pos_2[0])
        self.min_y=min(pos_1[1],pos_2[1])
        self.min_z=min(pos_1[2],pos_2[2])
        self.max_x=max(pos_1[0],pos_2[0])
        self.max_y=max(pos_1[1],pos_2[1])
        self.max_z=max(pos_1[2],pos_2[2])

        self._positions_list=[]
        lines=[]
        surface=[]
        for y in range(self.min_y,self.max_y+1):
            for i in range(self.min_x,self.max_x+1):
                for j in range(self.min_z,self.max_z+1):
                    lines.append((i,y,j))
                surface.append(lines)
                lines=[]
            self._positions_list.append(surface)
            surface=[]
        self.positions=[m for i in self._positions_list for j in i for m in j]
    
    def get_position(self,x_index=0,y_index=0,z_index=0):
        return self._positions_list[y_index][z_index][x_index]

    def get_positions_list(self,mode:str="y",index:int=0):
        '''mode:
        - y or face
        - z or cols
        - x or line'''
        if mode == "y" or mode == "face":
            return [j for i in self._positions_list[index] for j in i]
        elif mode == "z" or mode == "cols":
            return [j[index] for i in self._positions_list for j in i]
        elif mode == "x" or mode == "line":
            return [m for i in self._positions_list for _index,m in enumerate(i) if _index == index]
    
    def vector(self,pos_1:list[tuple[str,str]],pos_2:list[tuple[str,str]]) -> list[int]:
        '''向量坐标'''
        pos_1=self.parse_pos(pos_1)
        pos_2=self.parse_pos(pos_2)
        AB=[pos_2[index]-value_1 for index,value_1 in enumerate(pos_1)]
        return AB
    
    @property
    def count(self):
        AB=self.vector(self.pos_1,self.pos_2)
        AB=[i+1 if i>=0 else i-1 for i in AB]
        count_AB=abs(AB[0]*AB[1]*AB[2])
        return count_AB
        
class chunk(position_list):
    def __init__(self,pos:str | list[tuple[str,str]] | list[int],_chunk_len:int=16,_point_0:list[int]=[0,0]) -> None:
        '''- pos:坐标
        - _chunk_value:想要分割的区块大小'''
        self.pos=self.parse_pos(pos)
        self._value=_chunk_len
        self._point_0=_point_0
        position_list.__init__(self, *self.chunk_pos)

    @property
    def chunk_pos(self) -> tuple[tuple[int],tuple[int]]:
        '''返回当前位置的区块坐标范围'''
        x=self.pos[0]
        y=self.pos[1]
        z=self.pos[2]
        value=self._value
        x_0=self._point_0[0]
        z_0=self._point_0[1]
        min_x=x-(x%value)+x_0 if x >= x_0 else (x_0-x)%value-1+x
        min_z=z-(z%value)+z_0 if z >= z_0 else (z_0-z)%value-1+z
        max_x=min_x+value-1 if min_x >= x_0 else min_x-value+1
        max_z=min_z+value-1 if min_z >= z_0 else min_z-value+1
        min_pos=(min_x,y,min_z)
        max_pos=(max_x,y,max_z)
        return min_pos,max_pos

class Map(position):
    '''地图'''
    def __init__(self,pos:str | list[tuple[str,str]] | list[int],level:int=0) -> None:
        '''- pos:坐标
        - level:地图等级 0-4'''
        self.pos=self.parse_pos(pos)
        if level in range(5):
            self.level=level
        else:
            raise ValueError("应为0~4")
    
    @property
    def map_pos(self):
        chunk_sum=2**(self.level+3)
        chunk_len=16*chunk_sum
        return chunk(self.pos,chunk_len,[-8*chunk_sum,-8*chunk_sum]).chunk_pos

    