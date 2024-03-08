from enum import Enum
from typing import Any
from mc_cb._block_infor import _block_list

_TMP_NAME=''

class _block_name:
    def __init__(self,name) -> None:
        self._name=name
        global _TMP_NAME
        _TMP_NAME=name
        
    def __str__(self) -> str:
        return self._name

    def _command_attr_park(self,**kwargs) ->tuple[str,str]:
        '''返回mc指令方块名称以及属性部分的字符串类型'''
        re_str=''
        kwargs={i:j for i,j in kwargs.items() if j != None}
        max=len(kwargs)
        for id,args in enumerate(kwargs.items()):
            _attr,index=args
            options=self.__getattribute__(_attr)
            option=options.optional[index]
            attr=options.attr
            if isinstance(option,bool) or isinstance(option,int):
                re_str=re_str+f'''"{attr}"={option}'''
            else:
                re_str=re_str+f'''"{attr}"="{option}"'''
            if id+1 != max:  re_str=re_str+","
        return self._name,f'''[{re_str}]'''
    
class _get_block_attr:
    def __init__(self,attrs:dict) -> None:
        self.block=_TMP_NAME
        self.attr,self.optional=list(attrs.items())[0]
        
    def __getitem__(self,index:int) -> tuple[str,str]:
        return self.block,self._command_attr_park(index)
    
    def _command_attr_park(self,index:int):
        '''返回mc指令方块属性部分的字符串类型'''
        option=self.optional[index]
        if isinstance(option,bool) or isinstance(option,int):
            attr_park=f'''["{self.attr}"={option}]'''
        else:
            attr_park=f'''["{self.attr}"="{option}"]'''
        return attr_park

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

class _block_status:
    '''方块属性'''
    damage={"damage":["undamaged","slightly_damaged","very_damaged","broken"]}
    '''破损程度由低到高 0-3'''
    direction={"direction":[0,1,2,3]}
    '''朝向 0-3'''
    cardinal_direction={"minecraft:cardinal_direction":["east","south","west","north"]}
    '''朝向 东南西北 0-3'''
    facing_direction={"facing_direction":[2,3,4,5,0,1]}
    '''朝向 0-5'''
    block_face={"minecraft:block_face":["east","south","west","north","up","down"]}
    '''朝向 东南西北上下 0-5'''
    bamboo_leaf_size={"bamboo_leaf_size":["no_leaves","small_leaves","large_leaves"]}
    '''竹叶的大小 0-2'''
    bamboo_stalk_thickness={"bamboo_stalk_thickness":["thin","thick"]}
    '''竹子的粗度 0-1'''
    sapling_type={"sapling_type":["acacia","birch","dark_oak","jungle","oak","spruce"]}
    '''树苗种类 依次为金合欢,白桦,深色橡木,丛林,橡树,云杉 0-5'''
    age_bit={"age_bit":[False,True]}
    '''生长阶段 0-1'''
    ground_sign_direction={"ground_sign_direction":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]}
    '''朝向 0-15'''
    open_bit={"open_bit":[False,True]}
    '''是否有玩家使用 0-1'''
    pillar_axis={"pillar_axis":["x","y","z"]}
    '''玄武岩朝向 xyz 0-2'''
    head_piece_bit={"head_piece_bit":[False,True]}
    '''是否为床头部分 0-1'''
    occupied_bit={"occupied_bit":[False,True]}
    '''是否为使用床的状态 0-1'''
    infiniburn_bit={"infiniburn_bit":[False,True]}
    '''火焰是否能在上无限燃烧 0-1'''
    honey_level={"honey_level":[0,1,2,3,4,5]}
    '''蜂巢或蜂箱的储蜜量 0-5'''
    growth={"growth":[0,1,2,3,4,5,6,7]}
    '''作物成熟程度 0-7'''
    attachment={"attachment":["hanging","multiple","side","standing"]}
    '''钟的附着方向 "hanging","multiple","side","standing" 0-3'''
    toggle_bit={"toggle_bit":[0,1]}
    '''钟是否被鸣响 0-1'''
    big_dripleaf_head={"big_dripleaf_head":[0,1]}
    '''区分大型垂滴叶的叶片和叶茎部分 0-1'''
    big_dripleaf_tilt={"big_dripleaf_tilt":["none","partial_tilt","full_tilt"]}
    '''大型垂滴叶叶片垂下的程度 0-2'''
    deprecated={"deprecated":[0,1,2,3]}
    '''关于骨块 0-3'''
    wall_connection_type_east={"wall_connection_type_east":["none","short","tall"]}
    '''边界墙向东的延伸方式 0-2'''
    wall_connection_type_north={"wall_connection_type_north":["none","short","tall"]}
    '''边界墙向北的延伸方式 0-2'''
    wall_connection_type_south={"wall_connection_type_south":["none","short","tall"]}
    '''边界墙向南的延伸方式 0-2'''
    wall_connection_type_west={"wall_connection_type_west":["none","short","tall"]}
    '''边界墙向西的延伸方式 0-2'''
    wall_post_bit={"wall_post_bit":[False,True]}
    '''边界墙是否有中心柱 0-1'''
    brewing_stand_slot_a_bit={"brewing_stand_slot_a_bit":[False,True]}
    '''第一个槽放有药水 0-1'''
    brewing_stand_slot_b_bit={"brewing_stand_slot_b_bit":[False,True]}
    '''第二个槽放有药水 0-1'''
    brewing_stand_slot_c_bit={"brewing_stand_slot_c_bit":[False,True]}
    '''第三个槽放有药水 0-1'''
    drag_down={'drag_down':[False,True]}
    '''决定此气泡柱是涡流还是涌流 0-1'''
    button_pressed_bit={"button_pressed_bit":[0,1]}
    '''按钮是否被激活 0-1'''
    age={"age":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]}
    '''生长程度(包括火焰) 
    - 其他 0-15
    - 紫颂花 0-5
    - 可可果 0-2
    - 霜冰，下界疣 0-3'''
    bite_counter={"bite_counter":[0,1,2,3,4,5,6]}
    '''蛋糕被吃掉的片数 0-6'''
    lit={'lit':[False,True]}
    '''蜡烛是否被点燃 0-1'''
    extinguishe={"extinguished":[False,True]}
    '''营火是否熄灭 0-1'''
    candles={"candles":[0,1,2,3]}
    '''蜡烛的数量，从1开始到4 0-3'''
    color={"color":["white","orange","magenta","light_blue","yellow","lime","pink","gray","silver","cyan","purple","blue","brown","green","red","black"]}
    '''颜色 0-15
    白	0	
    橘	1	
    品红	2	
    浅蓝	3	
    黄	4	
    黄绿	5	
    粉	6	
    灰	7	
    淡灰	8	
    青	9	
    紫	10	
    蓝	11	
    褐	12	
    绿	13	
    红	14	
    黑	15'''
    fill_level={"fill_level":[0,1,2,3,4,5,6]}
    '''药锅中的水位，0为空而6为满 0-6'''
    cauldron_liquid={"cauldron_liquid":['water',"lava","powder_snow"]}
    '''炼药锅盛装的液体类型 水，岩浆，雪 0-2'''
    growing_plant_age={"growing_plant_age":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]}
    '''藤蔓的年龄 0-25'''
    books_stored={"books_stored":[0,1,2,3,4,5,6]}
    '''雕纹书架中书的数量 0-6'''
    last_interacted_slot={"last_interacted_slot":[0,1,2,3,4,5,6]}
    '''最近一次放入或取出的书在雕纹书架中的槽位号，用于确定发出的红石信号强度 0-6'''
    conditional_bit={"conditional_bit":[False,True]}
    '''当命令方块为条件制约模式时为“true” 0-1'''
    composter_fill_level={"composter_fill_level":[0,1,2,3,4,5,6,7,8]}
    '''值为8时可以从堆肥桶里收集到骨粉 0-8'''
    waterlogged={"waterlogged":[False,True]}
    '''是否含水 0-1'''
    coral_color={'coral_color':["blue","pink","purple","red","yellow"]}
    ''' 管珊瑚 脑纹珊瑚 气泡珊瑚 火珊瑚 鹿角珊瑚 0-4'''
    dead_bit={'dead_bit':[False,True]}
    '''是否失活 0-1'''
    coral_fan_direction={'coral_fan_direction':[0,1,2,3]}
    '''珊瑚扇朝向的方向，正常情况下值都为1 0-3 '''
    coral_hang_type_bit={"coral_hang_type_bit":[False,True]}
    '''墙上珊瑚扇类型 0-1'''
    coral_direction={'coral_direction':[1,2,3,0]}
    '''朝向 东南西北 0-3'''
    redstone_signal={"redstone_signal":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]}
    '''- 红石信号强度水平 0-15 
    - 压力板（木，石）只有 0-1'''
    axis={'axis':["x","y","z"]}
    '''xyz朝向 0-2'''
    dirt_type={"dirt_type":["normal","coarse"]}
    '''0为泥土，1为砂土 0-1'''
    triggered_bit={"triggered_bit":[False,True]}
    '''方块被激活时为true 0-1'''
    upper_block_bit={'upper_block_bit':[1,2,3,0]}
    '''是否为上半部分 0-1'''
    door_hinge_bit={'door_hinge_bit':[False,True]}
    '''识别门轴在哪一边（从面向门“里面”的方向看）0-1'''
    end_portal_eye_bit={"end_portal_eye_bit":[False,True]}
    '''末地传送门框架是否包含一个末影之眼 0-1'''
    moisturized_amount={'moisturized_amount':[0,1,2,3,4,5,6,7]}
    '''耕地方块的湿润程度 0-7'''
    wood_type={'wood_type':["oak","spruce","birch","jungle","acacia","dark_oak"]}
    '''橡木 云杉木 白桦木 丛林木 金合欢木 深色橡木 0-5'''
    in_wall_bit={"in_wall_bit":[False,True]}
    '''使其更贴合圆石墙和苔石墙的高度 0-1'''
    half={'half':["lower","upper"]}
    '''显示上半还是下半部分 0-1'''
    update_bit={'update_bit':[0,1]}
    '''是否检查更新 0-1'''
    multi_face_direction_bits={'multi_face_direction_bits':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63]}
    '''发光地衣的朝向 0-63'''
    monster_egg_stone_type={'monster_egg_stone_type':["chiseled_stone_brick","cobblestone","cracked_stone_brick","stone","mossy_stone_brick","stone_brick"]}
    ''' 虫蚀雕纹石砖 虫蚀圆石 虫蚀裂纹石砖 虫蚀石头	虫蚀苔石砖 虫蚀石砖 0-5'''
    north={'north':[False,True]}
    '''它的中心向北延伸'''
    south={'south':[False,True]}
    '''它的中心向南延伸'''
    east={'east':[False,True]}
    '''它的中心向东延伸'''
    west={'west':[False,True]}
    '''它的中心向西延伸'''
    item_frame_map_bit={'item_frame_map_bit':[0,1]}
    '''物品展示框是否含有地图 0-1'''
    item_frame_photo_bit={'item_frame_photo_bit':[0,1]}
    '''物品展示框是否含有相片 0-1'''
    rotation={'rotation':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]}
    '''- 生成结构时旋转的角度 n*90 0-3
    - 其他/生物头颅朝向 0-15'''
    kelp_age={"kelp_age":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]}
    '''生长程度 0-15'''
    liquid_depth={'liquid_depth':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]}
    '''液体状态 0-15'''
    old_leaf_type={'old_leaf_type':["oak","spruce","birch","jungle"]}
    '''树叶类型 0-3'''
    persistent_bit={'persistent_bit':[False,True]}
    '''是否不会枯萎 0-1'''
    new_leaf_type={'new_leaf_type':["acacia","dark_oak"]}
    '''树叶类型 0-1'''
    powered_bit={'powered_bit':[False,True]}
    '''是否有书 0-1'''
    lever_direction={'lever_direction':["down_east_west","east","west","morth","south","up_north_south","up_east_west","down_north_south"]}
    '''拉杆附着面 0-7'''
    block_light_level={"block_light_level":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]}
    '''方块亮度 0-15'''
    huge_mushroom_bits={'huge_mushroom_bits':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]}
    '''纹理朝向 0-15'''
    portal_axis={'portal_axis':["unknown","x","z"]}
    '''传送门朝向 默认，x，z 0-2'''
    instrument={'instrument':['banjo','basedrum','bass','bell','bit','chime','cow_bell','creeper','custom_head','didgeridoo','dragon','flute','guitar','harp','hat','iron_xylophone','piglin','pling','skeleton','snare','wither_skeleton','xylophone','zombie']}
    '''乐器 0-22'''
    note={'note':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]}
    '''音高 0-24'''
    powered={'powered':[False,True]}
    '''如果音符盒被激活，则为true 0-1'''
    dripstone_thickness={'dripstone_thickness':["tip","merge","frustum","middle","base"]}
    '''石锥的粗细 0-4'''
    hanging={'hanging':[False,True]}
    '''朝向 0-1'''
    prismarine_block_type={'prismarine_block_type':['bricks','dark','default']}
    '''海晶石种类 0-2'''
    chisel_type={'chisel_type':["chiseled",'default','lines','smooth']}
    '''石英柱 紫珀石种类 0-3'''
    rail_direction={"rail_direction":[0,1,2,3,4,5,6,7,8,9]}
    '''铁轨样式 0-9'''
    rail_data_bit={'rail_data_bit':[False,True]}
    '''铁轨是否被激活 0-1'''
    output_subtract_bit={'output_subtract_bit':[False,True]}
    '''定红石比较器的当前模式 0-1'''
    output_lit_bit={'output_lit_bit':[False,True]}
    '''是否为激活状态 0-1'''
    repeater_delay={'repeater_delay':[0,1,2,3]}
    '''红石中继器延迟的红石刻数减去1 0-3'''
    torch_facing_direction={'torch_facing_direction':["unknown","west","east","north","south","top"]}
    '''接触面位置 0-5'''
    respawn_anchor_charge={'respawn_anchor_charge':[0,1,2,3,4]}
    '''重生锚剩余的能量等级 0-4'''
    sand_stone_type={'sand_stone_type':["default","heiroglyphs","cut","smooth"]}
    '''砂岩类型 0-3'''
    propagule_stage={'propagule_stage':[0,1,2,3,4]}
    '''红树胎生苗悬挂时的年龄 0-4'''
    stability_check={"stability_check":[False,True]}
    '''脚手架是否稳定 0-1'''
    stability={'stability':[0,1,2,3,4,5,6,7]}
    '''距中心脚手架的水平距离。若为7，则将变为下落的方块实体 0-7'''
    bloom={'bloom':[False,True]}
    '''幽匿催发体是否处于蔓延状态 0-1'''
    active={'active':[0,1]}
    '''幽匿尖啸体是否处于激活状态 0-1'''
    can_summon={'can_summon':[False,True]}
    '''幽匿尖啸体能否召唤监守者 0-1'''
    cluster_count={'cluster_count':[0,1,3]}
    '''数量 0-3'''
    attached={'attached':[False,True]}
    '''锁链是否系于一点 0-1'''
    attached_bit={'attached_bit':[False,True]}
    '''锁链是否系于一点 0-1'''
    stone_slab_type={'stone_slab_type':["smooth_stone","sandstone","wood","cobblestone","brick","stone_brick","quartz","nether_brick"]}
    '''石砖的类型 0-7'''
    top_slot_bit={'top_slot_bit':[False,True]}
    '''此台阶是否位于上半部分 0-1'''
    stone_slab_type_2={'stone_slab_type_2':["red_sandstone","purpur","prismarine_rough","prismarine_dark","prismarine_brick","mossy_cobblestone","smooth_sandstone","red_nether_brick"]}
    '''石砖的类型 0-7'''
    stone_slab_type_3={'stone_slab_type_3':["end_stone_brick","smooth_red_sandstone","polished_andesite","andesite","diorite","polished_diorite","granite","polished_granite"]}
    '''石砖的类型 0-7'''
    stone_slab_type_4={'stone_slab_type_4':["mossy_stone_brick","smooth_quartz","stone","cut_sandstone","cut_red_sandstone"]}
    '''石砖的类型 0-4'''
    height={'height':[0,1,2,3,4,5,6,7,8]}
    '''厚度层数 0-8'''
    covered_bit={'covered_bit',[False,True]}
    '''是否有植物在此单元格含雪 0-1'''
    sponge_type={'sponge_type':["dry","wet"]}
    '''干湿海绵 0-1'''
    upside_down_bit={"upside_down_bit":[False,True]}
    '''楼梯是上下颠倒的则为true 0-1'''
    weirdo_direction={'weirdo_direction':[0,1,2,3]}
    '''楼梯整格面的朝向 0-3'''
    stone_type={'stone_type':['stone',"granite","granite_smooth","diorite","diorite_smooth","andesite","andesite"]}
    '''石头类型 0-6'''
    stone_brick_type={'stone_brick_type':['chiseled',"cracked","default","mossy","smooth"]}
    '''石砖类型 0-4'''
    structure_block_type={'structure_block_type':["corner","data","export","invalid","load","save"]}
    '''结构方块模式 0-5'''
    structure_void_type={'structure_void_type':["air","void"]}
    '''结构空位 0-1'''
    tall_grass_type={'tall_grass_type':['default','tall','fern','snow']}
    '''方块的变种，snow为是否积雪 0-3'''
    
    
class block_list(_block_list):
    class _anvil(_block_name):
        def __init__(self, name) -> None:
            super().__init__(name)
            self.damage=_get_block_attr(_block_status.damage)
            '''破损程度由低到高 0-3'''
            self.direction=_get_block_attr(_block_status.direction)
            '''朝向 0-3'''
            self.cardinal_direction=_get_block_attr(_block_status.cardinal_direction)
            '''朝向 东南西北 0-3'''
        def set_attr(self,damage:int=None,direction:int=None,cardinal_direction:int=None) ->tuple[str,str]:
            '''- damage 破损程度由低到高 0-3
            - direction 朝向 0-3
            - cardinal_direction 朝向 东南西北 0-3'''
            return self._command_attr_park(damage=damage,direction=direction,cardinal_direction=cardinal_direction)
            
    class _amethyst_cluster(_block_name):
        def __init__(self, name) -> None:   
            super().__init__(name)
            self.facing_direction=_get_block_attr(_block_status.facing_direction)
            '''朝向 0-5'''
            self.block_face=_get_block_attr(_block_status.block_face)
            '''朝向 东南西北上下 0-5'''
        def set_attr(self,facing_direction:int=None,block_face:int=None):
            '''- facing_direction 朝向 上下东南西北 0-5
            - block_face 朝向 上下东南西北 0-5'''
            return self._command_attr_park(facing_direction=facing_direction,block_face=block_face)
    
    anvil=_anvil(_block_list.anvil)
    '''铁砧'''
    amethyst_cluster=_amethyst_cluster(_block_list.amethyst_cluster)
    '''紫水晶簇'''