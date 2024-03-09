from mc_cb import Define
from mc_cb.variable import block_list,fill_handle,_get_block_attr

class fill:
    '''fill 指令'''
    def __init__(self,xyz_1:str="~~~",xyz_2:str="~~~",block:block_list=block_list.iron_block,fill_handle:fill_handle=fill_handle.replace) -> None:
        if isinstance(block,tuple):
            block,attr_park=block
            self.command_str=f'''fill {xyz_1} {xyz_2} {block} {attr_park} {fill_handle}'''
        else:
            block=str(block)
            self.command_str=f"fill {xyz_1} {xyz_2} {block} {fill_handle}"

class setblock:
    '''setblock'''
    def __init__(self,xyz:str="~~~",block:block_list=block_list.iron_block,fill_handle:fill_handle=fill_handle.replace) -> None:
        if isinstance(block,tuple):
            block,attr_park=block
            self.command_str=f'''setblock {xyz} {block} {attr_park} {fill_handle}'''
        else:
            block=str(block)
            self.command_str=f"setblock {xyz} {block} {fill_handle}"

class clone:
    '''clone'''
    def __init__(self) -> None:
        pass