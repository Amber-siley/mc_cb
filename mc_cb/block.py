################################################################
#计划实现position类（可能）
################################################################


from .variable import block_list,fill_handle,clone_handle
from .tools import command_str,tmp_function
from re import findall

class _pos_transformation:
    '''坐标变换，使方块操作更加优雅 32768'''
    def __init__(self,xyz_1,xyz_2) -> None:
        self.xyz_1=self.real_pos(xyz_1)
        self.xyz_2=self.real_pos(xyz_2)
    
    def count(self):
        xyz_1_type=self.pos_type(self.xyz_1)
        xyz_2_type=self.pos_type(self.xyz_2)
        if xyz_1_type != xyz_2_type:
            return 0
        else:
            pos_1=[int(j) if j != "" else 0 for i,j in self.xyz_1]
            pos_2=[int(j) if j != "" else 0 for i,j in self.xyz_2]
            AB=[pos_2[index]-value_1 if pos_2[index]-value_1>=0 else value_1-pos_2[index] for index,value_1 in enumerate(pos_1)]
            count_AB=AB[0]*AB[1]*AB[2]
            return count_AB
        
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
        pos_rule="([~,^]?)(\d*)"
        postions=findall(pos_rule,pos)
        postions=[(i,j) for i,j in postions if i != "" or j !=""]
        return postions
    
class fill:
    '''fill 指令'''
    def __init__(self,xyz_1:str="~~~",xyz_2:str="~~~",block:block_list=block_list.iron_block,fill_handle:fill_handle=fill_handle.replace) -> None:
        self.command_str=command_str("fill",xyz_1,xyz_2,block,fill_handle)
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