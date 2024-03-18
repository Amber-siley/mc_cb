################################################################
#_pos_transformation可以将坐标进行分割，使函数中的fill操作没有参数限制
#fill 参数上限为 32768 （fill指令坐标以这个上限进行分割）
#clone 参数上限为 655360 （已经很大了，就不进行坐标分割【不是因为懒】）
################################################################


from .variable import block_list,fill_handle,clone_handle
from .define import _TMP_POS
from .tools import command_str,tmp_function
from re import findall

class _pos_transformation:
    '''坐标变换，使方块操作更加优雅'''
    def __init__(self,xyz_1:str | list[tuple[str,str]],xyz_2:str | list[tuple[str,str]]) -> None:
        self.xyz_1=self.real_pos(xyz_1)
        self.xyz_2=self.real_pos(xyz_2)
        self._index=0
    
    @property
    def split_postions(self) -> list[str]:
        global _TMP_POS
        self.split_pos(self.xyz_1,self.xyz_2)
        re_data=_TMP_POS
        _TMP_POS=[]
        return re_data
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self.split_postions):
            re_data=self.split_postions[self._index]
            self._index+=1
            return re_data
        else:
            self._index=0
            raise StopIteration
        
    def count(self,jump_check=False) ->int:
        xyz_1_type=self.pos_type(self.xyz_1)
        xyz_2_type=self.pos_type(self.xyz_2)
        if xyz_1_type != xyz_2_type or xyz_1_type == "unknown":
            return 0
        else:
            AB=self.vector(self.xyz_1,self.xyz_2)
            AB=[i+1 if i>=0 else i-1 for i in AB]
            count_AB=abs(AB[0]*AB[1]*AB[2])
            return count_AB
    
    def split_pos(self,pos_1:list[tuple[str,str]],pos_2:list[tuple[str,str]]):
        global _TMP_POS
        if self.count() <= 32768:
            _TMP_POS.append(self.__str__())
            return True
        A=pos_1
        B=pos_2
        AB=self.vector(A,B)
        max_index=AB.index(self.max(AB))
        AC=[int(value/2) if index == max_index else value for index,value in enumerate(AB)]
        C=[value+self.parse_pos(A)[index] for index,value in enumerate(AC)]
        D=self.parse_pos(A)
        D[max_index]=C[max_index]
        C=self.return_pos(C,B)
        D=self.return_pos(D,A)
        _pos_transformation(A,C).split_pos(A,C)
        _pos_transformation(D,B).split_pos(D,B)
               
    def vector(self,pos_1:list[tuple[str,str]],pos_2:list[tuple[str,str]]) -> list[int]:
        '''向量坐标'''
        pos_1=self.parse_pos(pos_1)
        pos_2=self.parse_pos(pos_2)
        AB=[pos_2[index]-value_1 for index,value_1 in enumerate(pos_1)]
        return AB
    
    def max(self,pos:list[tuple[str,str]]):
        pos=self.parse_pos(pos)
        _pos=[abs(i) for i in pos]
        index=_pos.index(max(_pos))
        return pos[index]
    
    @staticmethod
    def parse_pos(pos:list[tuple[str,str]]) ->list[int]:
        '''解析坐标（并非真实坐标） -> [x,y,z]'''
        if isinstance(pos[0],int):
            return pos
        return [int(j) if j != "" else 0 for i,j in pos]
    
    def __str__(self):
        postion=self.xyz_1+self.xyz_2
        postion=["".join(i) for i in postion]
        return " ".join(postion)

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
    
class fill:
    '''fill 指令'''
    def __init__(self,xyz_1:str="~~~",xyz_2:str="~~~",block:block_list=block_list.iron_block,fill_handle:fill_handle=fill_handle.replace) -> None:
        _command_str=""
        for pos in _pos_transformation(xyz_1,xyz_2):
            _command_str+=command_str("fill",pos,block,fill_handle)+'\n'
        self.command_str=_command_str[:-1]
        tmp_function.add(self.command_str)

class setblock:
    '''setblock'''
    def __init__(self,xyz:str="~~~",block:block_list=block_list.iron_block,fill_handle:fill_handle=fill_handle.replace) -> None:
        self.command_str=command_str("setblock",xyz,block,fill_handle)
        tmp_function.add(self.command_str)
        
class clone:
    '''clone'''
    def __init__(self,xyz_1:str="~~~",xyz_2:str="~~~",xyz_pos="~~~",handle:clone_handle=clone_handle.replace.normal()) -> None:
        self.command_str=command_str("clone",xyz_1,xyz_2,xyz_pos,handle)
        tmp_function.add(self.command_str)