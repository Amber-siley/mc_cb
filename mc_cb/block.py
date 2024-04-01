################################################################
#_pos_transformation可以将坐标进行分割，使函数中的fill操作没有参数限制
#fill 参数上限为 32768 （fill指令坐标以这个上限进行分割）
#clone 参数上限为 655360 （已经很大了，就不进行坐标分割【不是因为懒】）
################################################################


from ._block_infor import block_list
from .define import _TMP_POS
from .tools import command_str,tmp_function
from .game import position_list,position

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

class _pos_transformation(position_list):
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
    
    @property
    def count(self) ->int:
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
        if self.count <= 32768:
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
    
    def max(self,pos:list[tuple[str,str]]):
        pos=self.parse_pos(pos)
        _pos=[abs(i) for i in pos]
        index=_pos.index(max(_pos))
        return pos[index]
    
    def __str__(self):
        postion=self.xyz_1+self.xyz_2
        postion=["".join(i) for i in postion]
        return " ".join(postion)
    
class fill(fill_handle):
    '''fill 指令'''
    def __init__(self,xyz_1:str | list[int]="~~~",xyz_2:str | list[int]="~~~",block:block_list=block_list.iron_block,fill_handle:fill_handle=fill_handle.replace) -> None:
        _command_str=""
        for pos in _pos_transformation(xyz_1,xyz_2):
            _command_str+=command_str("fill",pos,block,fill_handle)+'\n'
        self.command_str=_command_str[:-1]
        tmp_function.add(self.command_str)

    class block_list(block_list):
        ...
        
class setblock(fill_handle):
    '''setblock'''
    def __init__(self,xyz:str | list[int]="~~~",block:block_list=block_list.iron_block,fill_handle:fill_handle=fill_handle.replace) -> None:
        xyz=str(position(xyz))
        self.command_str=command_str("setblock",xyz,block,fill_handle)
        tmp_function.add(self.command_str)
    
    class block_list(block_list):
        ...
    
    
class clone(clone_handle):
    '''clone'''
    def __init__(self,xyz_1:str | list[int]="~~~",xyz_2:str | list[int]="~~~",xyz_pos:str | list[int]="~~~",handle:clone_handle=clone_handle.replace.normal()) -> None:
        xyz_1=str(position(xyz_1))
        xyz_2=str(position(xyz_2))
        xyz_pos=str(position(xyz_pos))
        self.command_str=command_str("clone",xyz_1,xyz_2,xyz_pos,handle)
        tmp_function.add(self.command_str)
    
    class block_list(block_list):
        ...