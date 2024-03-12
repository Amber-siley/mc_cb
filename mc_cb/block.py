################################################################
#计划实现position类（可能）
################################################################


from .variable import block_list,fill_handle,clone_handle
from .tools import command_str,tmp_function

class _pos_transformation:
    '''坐标变换，使方块操作更加优雅 32768'''
    def __init__(self,xyz_1,Xyz_2) -> None:
        
        pass
    
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