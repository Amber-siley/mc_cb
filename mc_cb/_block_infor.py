
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
                re_str=re_str+f'''"{attr}":{option}'''
            else:
                re_str=re_str+f'''"{attr}":"{option}"'''
            if id+1 != max:  re_str=re_str+","
        re_str=f'''[{re_str}]'''
        return f'''{self._name} {re_str}'''
    
class _get_block_attr:
    def __init__(self,attrs:dict) -> None:
        self.block=_TMP_NAME
        self.attr,self.optional=list(attrs.items())[0]
        
    def __getitem__(self,index:int) -> tuple[str,str]:
        return self._command_attr_park(index)
    
    def _command_attr_park(self,index:int):
        '''返回mc指令方块属性部分的字符串类型'''
        option=self.optional[index]
        if isinstance(option,bool) or isinstance(option,int):
            attr_park=f'''["{self.attr}":{option}]'''
        else:
            attr_park=f'''["{self.attr}":"{option}"]'''
        return f'''{self.block} {attr_park}'''

class _block_list:
    stone="stone"
    '''石头'''
    grass="grass"
    '''草方块'''
    dirt="dirt"
    '''泥土'''
    cobblestone="cobblestone"
    '''圆石'''
    planks="planks"
    '''木板'''
    sapling="sapling"
    '''树苗'''
    bedrock="bedrock"
    '''基岩'''
    flowing_water="flowing_water"
    '''水'''
    water="water"
    '''水'''
    flowing_lava="flowing_lava"
    '''熔岩'''
    lava="lava"
    '''熔岩'''
    sand="sand"
    '''沙子'''
    gravel="gravel"
    '''沙砾'''
    gold_ore="gold_ore"
    '''金矿石'''
    iron_ore="iron_ore"
    '''铁矿石'''
    coal_ore="coal_ore"
    '''煤矿石'''
    oak_log="oak_log"
    '''橡木原木'''
    leaves="leaves"
    '''树叶'''
    sponge="sponge"
    '''海绵'''
    glass="glass"
    '''玻璃'''
    lapis_ore="lapis_ore"
    '''青金石矿石'''
    lapis_block="lapis_block"
    '''青金石块'''
    dispenser="dispenser"
    '''发射器'''
    sandstone="sandstone"
    '''砂岩'''
    noteblock="noteblock"
    '''音符盒'''
    bed="bed"
    '''床'''
    golden_rail="golden_rail"
    '''动力铁轨'''
    detector_rail="detector_rail"
    '''探测铁轨'''
    sticky_piston="sticky_piston"
    '''黏性活塞'''
    web="web"
    '''蜘蛛网'''
    tallgrass="tallgrass"
    '''草'''
    deadbush="deadbush"
    '''枯萎的灌木'''
    piston="piston"
    '''活塞'''
    piston_arm_collision="piston_arm_collision"
    '''活塞臂'''
    white_wool="white_wool"
    '''白色羊毛'''
    element_0="element_0"
    '''未知元素（???）'''
    yellow_flower="yellow_flower"
    '''蒲公英'''
    red_flower="red_flower"
    '''花'''
    brown_mushroom="brown_mushroom"
    '''棕色蘑菇'''
    red_mushroom="red_mushroom"
    '''红色蘑菇'''
    gold_block="gold_block"
    '''金块'''
    iron_block="iron_block"
    '''铁块'''
    double_stone_slab="double_stone_slab"
    '''双石台阶'''
    stone_slab="stone_slab"
    '''石台阶'''
    brick_block="brick_block"
    '''红砖块'''
    tnt="tnt"
    '''TNT'''
    bookshelf="bookshelf"
    '''书架'''
    mossy_cobblestone="mossy_cobblestone"
    '''苔石'''
    obsidian="obsidian"
    '''黑曜石'''
    torch="torch"
    '''火把'''
    fire="fire"
    '''火'''
    mob_spawner="mob_spawner"
    '''刷怪笼'''
    oak_stairs="oak_stairs"
    '''橡木楼梯'''
    chest="chest"
    '''箱子'''
    redstone_wire="redstone_wire"
    '''红石线'''
    diamond_ore="diamond_ore"
    '''钻石矿石'''
    diamond_block="diamond_block"
    '''钻石块'''
    crafting_table="crafting_table"
    '''工作台'''
    wheat="wheat"
    '''小麦'''
    farmland="farmland"
    '''耕地'''
    furnace="furnace"
    '''熔炉'''
    lit_furnace="lit_furnace"
    '''熔炉'''
    standing_sign="standing_sign"
    '''橡木告示牌'''
    wooden_door="wooden_door"
    '''橡木门'''
    ladder="ladder"
    '''梯子'''
    rail="rail"
    '''铁轨'''
    stone_stairs="stone_stairs"
    '''圆石楼梯'''
    wall_sign="wall_sign"
    '''墙上的橡木告示牌'''
    lever="lever"
    '''拉杆'''
    stone_pressure_plate="stone_pressure_plate"
    '''石头压力板'''
    iron_door="iron_door"
    '''铁门'''
    wooden_pressure_plate="wooden_pressure_plate"
    '''木质压力板'''
    redstone_ore="redstone_ore"
    '''红石矿石'''
    lit_redstone_ore="lit_redstone_ore"
    '''红石矿石'''
    unlit_redstone_torch="unlit_redstone_torch"
    '''熄灭的红石火把'''
    redstone_torch="redstone_torch"
    '''红石火把'''
    stone_button="stone_button"
    '''石头按钮'''
    snow_layer="snow_layer"
    '''顶层雪'''
    ice="ice"
    '''冰'''
    snow="snow"
    '''雪'''
    cactus="cactus"
    '''仙人掌'''
    clay="clay"
    '''黏土块'''
    reeds="reeds"
    '''甘蔗'''
    jukebox="jukebox"
    '''唱片机'''
    oak_fence="oak_fence"
    '''橡木栅栏'''
    pumpkin="pumpkin"
    '''南瓜'''
    netherrack="netherrack"
    '''下界岩'''
    soul_sand="soul_sand"
    '''灵魂沙'''
    glowstone="glowstone"
    '''荧石'''
    portal="portal"
    '''下界传送门'''
    lit_pumpkin="lit_pumpkin"
    '''南瓜灯'''
    cake="cake"
    '''蛋糕'''
    unpowered_repeater="unpowered_repeater"
    '''未激活的中继器'''
    powered_repeater="powered_repeater"
    '''激活的中继器'''
    invisible_bedrock="invisible_bedrock"
    '''隐形的基岩'''
    trapdoor="trapdoor"
    '''活板门'''
    monster_egg="monster_egg"
    '''虫蚀方块'''
    stonebrick="stonebrick"
    '''石砖'''
    brown_mushroom_block="brown_mushroom_block"
    '''棕色蘑菇方块'''
    red_mushroom_block="red_mushroom_block"
    '''红色蘑菇方块'''
    iron_bars="iron_bars"
    '''铁栏杆'''
    glass_pane="glass_pane"
    '''玻璃板'''
    melon_block="melon_block"
    '''西瓜'''
    pumpkin_stem="pumpkin_stem"
    '''南瓜梗'''
    melon_stem="melon_stem"
    '''西瓜梗'''
    vine="vine"
    '''藤蔓'''
    fence_gate="fence_gate"
    '''橡木栅栏门'''
    brick_stairs="brick_stairs"
    '''红砖楼梯'''
    stone_brick_stairs="stone_brick_stairs"
    '''石砖楼梯'''
    mycelium="mycelium"
    '''菌丝体'''
    waterlily="waterlily"
    '''睡莲'''
    nether_brick="nether_brick"
    '''下界砖'''
    nether_brick_fence="nether_brick_fence"
    '''下界砖栅栏'''
    nether_brick_stairs="nether_brick_stairs"
    '''下界砖楼梯'''
    nether_wart="nether_wart"
    '''下界疣'''
    enchanting_table="enchanting_table"
    '''附魔台'''
    brewing_stand="brewing_stand"
    '''酿造台'''
    cauldron="cauldron"
    '''炼药锅'''
    end_portal="end_portal"
    '''末地传送门'''
    end_portal_frame="end_portal_frame"
    '''末地传送门框架'''
    end_stone="end_stone"
    '''末地石'''
    dragon_egg="dragon_egg"
    '''龙蛋'''
    redstone_lamp="redstone_lamp"
    '''红石灯'''
    lit_redstone_lamp="lit_redstone_lamp"
    '''点亮的红石灯'''
    dropper="dropper"
    '''投掷器'''
    activator_rail="activator_rail"
    '''激活铁轨'''
    cocoa="cocoa"
    '''可可果'''
    sandstone_stairs="sandstone_stairs"
    '''砂岩楼梯'''
    emerald_ore="emerald_ore"
    '''绿宝石矿石'''
    ender_chest="ender_chest"
    '''末影箱'''
    tripwire_hook="tripwire_hook"
    '''绊线钩'''
    trip_wire="trip_wire"
    '''绊线'''
    emerald_block="emerald_block"
    '''绿宝石块'''
    spruce_stairs="spruce_stairs"
    '''云杉木楼梯'''
    birch_stairs="birch_stairs"
    '''白桦木楼梯'''
    jungle_stairs="jungle_stairs"
    '''丛林木楼梯'''
    command_block="command_block"
    '''脉冲型命令方块'''
    beacon="beacon"
    '''信标'''
    cobblestone_wall="cobblestone_wall"
    '''墙'''
    flower_pot="flower_pot"
    '''花盆'''
    carrots="carrots"
    '''胡萝卜'''
    potatoes="potatoes"
    '''马铃薯'''
    wooden_button="wooden_button"
    '''橡木按钮'''
    skull="skull"
    '''生物头颅'''
    anvil="anvil"
    '''铁砧'''
    trapped_chest="trapped_chest"
    '''陷阱箱'''
    light_weighted_pressure_plate="light_weighted_pressure_plate"
    '''测重压力板'''
    heavy_weighted_pressure_plate="heavy_weighted_pressure_plate"
    '''测重压力板'''
    unpowered_comparator="unpowered_comparator"
    '''未激活的比较器'''
    powered_comparator="powered_comparator"
    '''激活的比较器'''
    daylight_detector="daylight_detector"
    '''阳光探测器'''
    redstone_block="redstone_block"
    '''红石块'''
    quartz_ore="quartz_ore"
    '''下界石英矿石'''
    hopper="hopper"
    '''漏斗'''
    quartz_block="quartz_block"
    '''石英块'''
    quartz_stairs="quartz_stairs"
    '''石英楼梯'''
    double_wooden_slab="double_wooden_slab"
    '''双层木台阶'''
    wooden_slab="wooden_slab"
    '''木质台阶'''
    stained_hardened_clay="stained_hardened_clay"
    '''染色陶瓦'''
    white_terracotta="white_terracotta"
    '''白色陶瓦'''
    orange_terracotta="orange_terracotta"
    '''橙色陶瓦'''
    magenta_terracotta="magenta_terracotta"
    '''品红色陶瓦'''
    light_blue_terracotta="light_blue_terracotta"
    '''淡蓝色陶瓦'''
    yellow_terracotta="yellow_terracotta"
    '''黄色陶瓦'''
    lime_terracotta="lime_terracotta"
    '''黄绿色陶瓦'''
    pink_terracotta="pink_terracotta"
    '''粉红色陶瓦'''
    gray_terracotta="gray_terracotta"
    '''灰色陶瓦'''
    light_gray_terracotta="light_gray_terracotta"
    '''淡灰色陶瓦'''
    cyan_terracotta="cyan_terracotta"
    '''青色陶瓦'''
    purple_terracotta="purple_terracotta"
    '''紫色陶瓦'''
    blue_terracotta="blue_terracotta"
    '''蓝色陶瓦'''
    brown_terracotta="brown_terracotta"
    '''棕色陶瓦'''
    green_terracotta="green_terracotta"
    '''绿色陶瓦'''
    red_terracotta="red_terracotta"
    '''红色陶瓦'''
    black_terracotta="black_terracotta"
    '''黑色陶瓦'''
    stained_glass_pane="stained_glass_pane"
    '''染色玻璃板'''
    leaves2="leaves2"
    '''树叶2'''
    acacia_log="acacia_log"
    '''金合欢原木'''
    acacia_stairs="acacia_stairs"
    '''金合欢木楼梯'''
    dark_oak_stairs="dark_oak_stairs"
    '''深色橡木楼梯'''
    slime="slime"
    '''黏液块'''
    iron_trapdoor="iron_trapdoor"
    '''铁活板门'''
    prismarine="prismarine"
    '''海晶石'''
    sea_lantern="sea_lantern"
    '''海晶灯'''
    hay_block="hay_block"
    '''干草捆'''
    white_carpet="white_carpet"
    '''白色地毯'''
    hardened_clay="hardened_clay"
    '''陶瓦'''
    coal_block="coal_block"
    '''煤炭块'''
    packed_ice="packed_ice"
    '''浮冰'''
    double_plant="double_plant"
    '''双层植物'''
    standing_banner="standing_banner"
    '''旗帜'''
    wall_banner="wall_banner"
    '''旗帜'''
    daylight_detector_inverted="daylight_detector_inverted"
    '''反向阳光探测器'''
    red_sandstone="red_sandstone"
    '''红砂岩'''
    red_sandstone_stairs="red_sandstone_stairs"
    '''红砂岩楼梯'''
    double_stone_block_slab2="double_stone_block_slab2"
    '''双石台阶2'''
    stone_slab2="stone_slab2"
    '''石台阶2'''
    spruce_fence_gate="spruce_fence_gate"
    '''云杉木栅栏门'''
    birch_fence_gate="birch_fence_gate"
    '''白桦木栅栏门'''
    jungle_fence_gate="jungle_fence_gate"
    '''丛林木栅栏门'''
    dark_oak_fence_gate="dark_oak_fence_gate"
    '''深色橡木栅栏门'''
    acacia_fence_gate="acacia_fence_gate"
    '''金合欢木栅栏门'''
    repeating_command_block="repeating_command_block"
    '''循环型命令方块'''
    chain_command_block="chain_command_block"
    '''连锁型命令方块'''
    hard_glass_pane="hard_glass_pane"
    '''强化玻璃板'''
    hard_stained_glass_pane="hard_stained_glass_pane"
    '''染色强化玻璃板'''
    chemical_heat="chemical_heat"
    '''加热块'''
    spruce_door="spruce_door"
    '''云杉木门'''
    birch_door="birch_door"
    '''白桦木门'''
    jungle_door="jungle_door"
    '''丛林木门'''
    acacia_door="acacia_door"
    '''金合欢木门'''
    dark_oak_door="dark_oak_door"
    '''深色橡木门'''
    grass_path="grass_path"
    '''草径'''
    frame="frame"
    '''物品展示框'''
    chorus_flower="chorus_flower"
    '''紫颂花'''
    purpur_block="purpur_block"
    '''紫珀块'''
    colored_torch_rg="colored_torch_rg"
    '''红色火把'''
    purpur_stairs="purpur_stairs"
    '''紫珀楼梯'''
    colored_torch_bp="colored_torch_bp"
    '''蓝色火把'''
    undyed_shulker_box="undyed_shulker_box"
    '''潜影盒'''
    end_bricks="end_bricks"
    '''末地石砖'''
    frosted_ice="frosted_ice"
    '''霜冰'''
    end_rod="end_rod"
    '''末地烛'''
    end_gateway="end_gateway"
    '''末地折跃门'''
    allow="allow"
    '''允许方块'''
    deny="deny"
    '''拒绝方块'''
    border_block="border_block"
    '''边界方块'''
    magma="magma"
    '''岩浆块'''
    nether_wart_block="nether_wart_block"
    '''下界疣块'''
    red_nether_brick="red_nether_brick"
    '''红色下界砖块'''
    bone_block="bone_block"
    '''骨块'''
    structure_void="structure_void"
    '''结构空位'''
    shulker_box="shulker_box"
    '''潜影盒'''
    purple_glazed_terracotta="purple_glazed_terracotta"
    '''紫色带釉陶瓦'''
    white_glazed_terracotta="white_glazed_terracotta"
    '''白色带釉陶瓦'''
    orange_glazed_terracotta="orange_glazed_terracotta"
    '''橙色带釉陶瓦'''
    magenta_glazed_terracotta="magenta_glazed_terracotta"
    '''品红色带釉陶瓦'''
    light_blue_glazed_terracotta="light_blue_glazed_terracotta"
    '''淡蓝色带釉陶瓦'''
    yellow_glazed_terracotta="yellow_glazed_terracotta"
    '''黄色带釉陶瓦'''
    lime_glazed_terracotta="lime_glazed_terracotta"
    '''黄绿色带釉陶瓦'''
    pink_glazed_terracotta="pink_glazed_terracotta"
    '''粉红色带釉陶瓦'''
    gray_glazed_terracotta="gray_glazed_terracotta"
    '''灰色带釉陶瓦'''
    silver_glazed_terracotta="silver_glazed_terracotta"
    '''淡灰色带釉陶瓦'''
    cyan_glazed_terracotta="cyan_glazed_terracotta"
    '''青色带釉陶瓦'''
    chalkboard="chalkboard"
    '''黑板'''
    blue_glazed_terracotta="blue_glazed_terracotta"
    '''蓝色带釉陶瓦'''
    brown_glazed_terracotta="brown_glazed_terracotta"
    '''棕色带釉陶瓦'''
    green_glazed_terracotta="green_glazed_terracotta"
    '''绿色带釉陶瓦'''
    red_glazed_terracotta="red_glazed_terracotta"
    '''红色带釉陶瓦'''
    black_glazed_terracotta="black_glazed_terracotta"
    '''黑色带釉陶瓦'''
    concrete="concrete"
    '''混凝土'''
    concrete_powder="concrete_powder"
    '''混凝土粉末'''
    chemistry_table="chemistry_table"
    '''化合物创建器'''
    underwater_torch="underwater_torch"
    '''水下火把'''
    chorus_plant="chorus_plant"
    '''紫颂植株'''
    stained_glass="stained_glass"
    '''染色玻璃'''
    camera="camera"
    '''相机'''
    podzol="podzol"
    '''灰化土'''
    beetroot="beetroot"
    '''甜菜根'''
    stonecutter="stonecutter"
    '''切石机'''
    glowingobsidian="glowingobsidian"
    '''发光的黑曜石'''
    netherreactor="netherreactor"
    '''下界反应核'''
    info_update="info_update"
    '''数据更新方块'''
    info_update2="info_update2"
    '''数据更新方块2'''
    moving_block="moving_block"
    '''被活塞推动的方块'''
    observer="observer"
    '''侦测器'''
    structure_block="structure_block"
    '''结构方块'''
    hard_glass="hard_glass"
    '''强化玻璃'''
    hard_stained_glass="hard_stained_glass"
    '''强化染色玻璃'''
    reserved6="reserved6"
    '''reserved6'''
    prismarine_stairs="prismarine_stairs"
    '''海晶石楼梯'''
    dark_prismarine_stairs="dark_prismarine_stairs"
    '''暗海晶石楼梯'''
    prismarine_bricks_stairs="prismarine_bricks_stairs"
    '''海晶石砖楼梯'''
    stripped_spruce_log="stripped_spruce_log"
    '''去皮云杉原木'''
    stripped_birch_log="stripped_birch_log"
    '''去皮白桦原木'''
    stripped_jungle_log="stripped_jungle_log"
    '''去皮丛林原木'''
    stripped_acacia_log="stripped_acacia_log"
    '''去皮金合欢原木'''
    stripped_dark_oak_log="stripped_dark_oak_log"
    '''去皮深色橡木原木'''
    stripped_oak_log="stripped_oak_log"
    '''去皮橡木原木'''
    blue_ice="blue_ice"
    '''蓝冰'''
    element_1="element_1"
    '''氢'''
    element_2="element_2"
    '''氦'''
    element_3="element_3"
    '''锂'''
    element_4="element_4"
    '''铍'''
    element_5="element_5"
    '''硼'''
    element_6="element_6"
    '''碳'''
    element_7="element_7"
    '''氮'''
    element_8="element_8"
    '''氧'''
    element_9="element_9"
    '''氟'''
    element_10="element_10"
    '''氖'''
    element_11="element_11"
    '''钠'''
    element_12="element_12"
    '''镁'''
    element_13="element_13"
    '''铝'''
    element_14="element_14"
    '''硅'''
    element_15="element_15"
    '''磷'''
    element_16="element_16"
    '''硫'''
    element_17="element_17"
    '''氯'''
    element_18="element_18"
    '''氩'''
    element_19="element_19"
    '''钾'''
    element_20="element_20"
    '''钙'''
    element_21="element_21"
    '''钪'''
    element_22="element_22"
    '''钛'''
    element_23="element_23"
    '''钒'''
    element_24="element_24"
    '''铬'''
    element_25="element_25"
    '''锰'''
    element_26="element_26"
    '''铁'''
    element_27="element_27"
    '''钴'''
    element_28="element_28"
    '''镍'''
    element_29="element_29"
    '''铜'''
    element_30="element_30"
    '''锌'''
    element_31="element_31"
    '''镓'''
    element_32="element_32"
    '''锗'''
    element_33="element_33"
    '''砷'''
    element_34="element_34"
    '''硒'''
    element_35="element_35"
    '''溴'''
    element_36="element_36"
    '''氪'''
    element_37="element_37"
    '''铷'''
    element_38="element_38"
    '''锶'''
    element_39="element_39"
    '''钇'''
    element_40="element_40"
    '''锆'''
    element_41="element_41"
    '''铌'''
    element_42="element_42"
    '''钼'''
    element_43="element_43"
    '''锝'''
    element_44="element_44"
    '''钌'''
    element_45="element_45"
    '''铑'''
    element_46="element_46"
    '''钯'''
    element_47="element_47"
    '''银'''
    element_48="element_48"
    '''镉'''
    element_49="element_49"
    '''铟'''
    element_50="element_50"
    '''锡'''
    element_51="element_51"
    '''锑'''
    element_52="element_52"
    '''碲'''
    element_53="element_53"
    '''碘'''
    element_54="element_54"
    '''氙'''
    element_55="element_55"
    '''铯'''
    element_56="element_56"
    '''钡'''
    element_57="element_57"
    '''镧'''
    element_58="element_58"
    '''铈'''
    element_59="element_59"
    '''镨'''
    element_60="element_60"
    '''钕'''
    element_61="element_61"
    '''钷'''
    element_62="element_62"
    '''钐'''
    element_63="element_63"
    '''铕'''
    element_64="element_64"
    '''钆'''
    element_65="element_65"
    '''铽'''
    element_66="element_66"
    '''镝'''
    element_67="element_67"
    '''钬'''
    element_68="element_68"
    '''铒'''
    element_69="element_69"
    '''铥'''
    element_70="element_70"
    '''镱'''
    element_71="element_71"
    '''镥'''
    element_72="element_72"
    '''铪'''
    element_73="element_73"
    '''钽'''
    element_74="element_74"
    '''钨'''
    element_75="element_75"
    '''铼'''
    element_76="element_76"
    '''锇'''
    element_77="element_77"
    '''铱'''
    element_78="element_78"
    '''铂'''
    element_79="element_79"
    '''金'''
    element_80="element_80"
    '''汞'''
    element_81="element_81"
    '''铊'''
    element_82="element_82"
    '''铅'''
    element_83="element_83"
    '''铋'''
    element_84="element_84"
    '''钋'''
    element_85="element_85"
    '''砹'''
    element_86="element_86"
    '''氡'''
    element_87="element_87"
    '''钫'''
    element_88="element_88"
    '''镭'''
    element_89="element_89"
    '''锕'''
    element_90="element_90"
    '''钍'''
    element_91="element_91"
    '''镤'''
    element_92="element_92"
    '''铀'''
    element_93="element_93"
    '''镎'''
    element_94="element_94"
    '''钚'''
    element_95="element_95"
    '''镅'''
    element_96="element_96"
    '''锔'''
    element_97="element_97"
    '''锫'''
    element_98="element_98"
    '''锎'''
    element_99="element_99"
    '''锿'''
    element_100="element_100"
    '''镄'''
    element_101="element_101"
    '''钔'''
    element_102="element_102"
    '''锘'''
    element_103="element_103"
    '''铹'''
    element_104="element_104"
    '''鑪'''
    element_105="element_105"
    '''𨧀'''
    element_106="element_106"
    '''𨭎'''
    element_107="element_107"
    '''𨨏'''
    element_108="element_108"
    '''𨭆'''
    element_109="element_109"
    '''䥑'''
    element_110="element_110"
    '''鐽'''
    element_111="element_111"
    '''錀'''
    element_112="element_112"
    '''鎶'''
    element_113="element_113"
    '''鉨'''
    element_114="element_114"
    '''鈇'''
    element_115="element_115"
    '''镆'''
    element_116="element_116"
    '''鉝'''
    element_117="element_117"
    '''Tennessine'''
    element_118="element_118"
    '''Oganesson'''
    seagrass="seagrass"
    '''海草'''
    tube_coral="tube_coral"
    '''管珊瑚'''
    coral_block="coral_block"
    '''珊瑚块'''
    coral_fan="coral_fan"
    '''珊瑚扇'''
    coral_fan_dead="coral_fan_dead"
    '''失活的珊瑚扇'''
    coral_fan_hang="coral_fan_hang"
    '''墙上的珊瑚扇'''
    coral_fan_hang2="coral_fan_hang2"
    '''墙上的珊瑚扇2'''
    coral_fan_hang3="coral_fan_hang3"
    '''墙上的珊瑚扇3'''
    kelp="kelp"
    '''海带'''
    dried_kelp_block="dried_kelp_block"
    '''干海带块'''
    acacia_button="acacia_button"
    '''金合欢木按钮'''
    birch_button="birch_button"
    '''白桦木按钮'''
    dark_oak_button="dark_oak_button"
    '''深色橡木按钮'''
    jungle_button="jungle_button"
    '''丛林木按钮'''
    spruce_button="spruce_button"
    '''云杉木按钮'''
    acacia_trapdoor="acacia_trapdoor"
    '''金合欢木活板门'''
    birch_trapdoor="birch_trapdoor"
    '''白桦木活板门'''
    dark_oak_trapdoor="dark_oak_trapdoor"
    '''深色橡木活板门'''
    jungle_trapdoor="jungle_trapdoor"
    '''丛林木活板门'''
    spruce_trapdoor="spruce_trapdoor"
    '''云杉木活板门'''
    acacia_pressure_plate="acacia_pressure_plate"
    '''金合欢木压力板'''
    birch_pressure_plate="birch_pressure_plate"
    '''白桦木压力板'''
    dark_oak_pressure_plate="dark_oak_pressure_plate"
    '''深色橡木压力板'''
    jungle_pressure_plate="jungle_pressure_plate"
    '''丛林木压力板'''
    spruce_pressure_plate="spruce_pressure_plate"
    '''云杉木压力板'''
    carved_pumpkin="carved_pumpkin"
    '''雕刻南瓜'''
    sea_pickle="sea_pickle"
    '''海泡菜'''
    conduit="conduit"
    '''潮涌核心'''
    air="air"
    '''空气'''
    turtle_egg="turtle_egg"
    '''海龟蛋'''
    bubble_column="bubble_column"
    '''气泡柱'''
    barrier="barrier"
    '''屏障'''
    stone_slab3="stone_slab3"
    '''石台阶3'''
    bamboo="bamboo"
    '''竹子'''
    bamboo_sapling="bamboo_sapling"
    '''竹笋'''
    scaffolding="scaffolding"
    '''脚手架'''
    stone_slab4="stone_slab4"
    '''石台阶4'''
    double_stone_block_slab3="double_stone_block_slab3"
    '''双石台阶3'''
    double_stone_block_slab4="double_stone_block_slab4"
    '''双石台阶4'''
    granite_stairs="granite_stairs"
    '''花岗岩楼梯'''
    diorite_stairs="diorite_stairs"
    '''闪长岩楼梯'''
    andesite_stairs="andesite_stairs"
    '''安山岩楼梯'''
    polished_granite_stairs="polished_granite_stairs"
    '''磨制花岗岩楼梯'''
    polished_diorite_stairs="polished_diorite_stairs"
    '''磨制闪长岩楼梯'''
    polished_andesite_stairs="polished_andesite_stairs"
    '''磨制安山岩楼梯'''
    mossy_stone_brick_stairs="mossy_stone_brick_stairs"
    '''苔石砖楼梯'''
    smooth_red_sandstone_stairs="smooth_red_sandstone_stairs"
    '''平滑红砂岩楼梯'''
    smooth_sandstone_stairs="smooth_sandstone_stairs"
    '''平滑砂岩楼梯'''
    end_brick_stairs="end_brick_stairs"
    '''末地石砖楼梯'''
    mossy_cobblestone_stairs="mossy_cobblestone_stairs"
    '''苔石楼梯'''
    normal_stone_stairs="normal_stone_stairs"
    '''石头楼梯'''
    spruce_standing_sign="spruce_standing_sign"
    '''云杉木告示牌'''
    spruce_wall_sign="spruce_wall_sign"
    '''云杉木告示牌'''
    smooth_stone="smooth_stone"
    '''平滑石头'''
    red_nether_brick_stairs="red_nether_brick_stairs"
    '''红色下界砖楼梯'''
    smooth_quartz_stairs="smooth_quartz_stairs"
    '''平滑石英楼梯'''
    birch_standing_sign="birch_standing_sign"
    '''白桦木告示牌'''
    birch_wall_sign="birch_wall_sign"
    '''白桦木告示牌'''
    jungle_standing_sign="jungle_standing_sign"
    '''丛林木告示牌'''
    jungle_wall_sign="jungle_wall_sign"
    '''丛林木告示牌'''
    acacia_standing_sign="acacia_standing_sign"
    '''金合欢木告示牌'''
    acacia_wall_sign="acacia_wall_sign"
    '''金合欢木告示牌'''
    darkoak_standing_sign="darkoak_standing_sign"
    '''深色橡木告示牌'''
    darkoak_wall_sign="darkoak_wall_sign"
    '''深色橡木告示牌'''
    lectern="lectern"
    '''讲台'''
    grindstone="grindstone"
    '''砂轮'''
    blast_furnace="blast_furnace"
    '''高炉'''
    stonecutter_block="stonecutter_block"
    '''切石机'''
    smoker="smoker"
    '''烟熏炉'''
    lit_smoker="lit_smoker"
    '''烟熏炉'''
    cartography_table="cartography_table"
    '''制图台'''
    fletching_table="fletching_table"
    '''制箭台'''
    smithing_table="smithing_table"
    '''锻造台'''
    barrel="barrel"
    '''木桶'''
    loom="loom"
    '''织布机'''
    bell="bell"
    '''钟'''
    sweet_berry_bush="sweet_berry_bush"
    '''甜浆果丛'''
    lantern="lantern"
    '''灯笼'''
    campfire="campfire"
    '''营火'''
    lava_cauldron="lava_cauldron"
    '''炼药锅'''
    jigsaw="jigsaw"
    '''拼图方块'''
    wood="wood"
    '''木头'''
    composter="composter"
    '''堆肥桶'''
    lit_blast_furnace="lit_blast_furnace"
    '''高炉'''
    light_block="light_block"
    '''光源方块'''
    wither_rose="wither_rose"
    '''凋灵玫瑰'''
    sticky_piston_arm_collision="sticky_piston_arm_collision"
    '''黏性活塞臂'''
    bee_nest="bee_nest"
    '''蜂巢'''
    beehive="beehive"
    '''蜂箱'''
    honey_block="honey_block"
    '''蜂蜜块'''
    honeycomb_block="honeycomb_block"
    '''蜜脾块'''
    lodestone="lodestone"
    '''磁石'''
    crimson_roots="crimson_roots"
    '''绯红菌索'''
    warped_roots="warped_roots"
    '''诡异菌索'''
    crimson_stem="crimson_stem"
    '''绯红菌柄'''
    warped_stem="warped_stem"
    '''诡异菌柄'''
    warped_wart_block="warped_wart_block"
    '''诡异疣块'''
    crimson_fungus="crimson_fungus"
    '''绯红菌'''
    warped_fungus="warped_fungus"
    '''诡异菌'''
    shroomlight="shroomlight"
    '''菌光体'''
    weeping_vines="weeping_vines"
    '''垂泪藤'''
    crimson_nylium="crimson_nylium"
    '''绯红菌岩'''
    warped_nylium="warped_nylium"
    '''诡异菌岩'''
    basalt="basalt"
    '''玄武岩'''
    polished_basalt="polished_basalt"
    '''磨制玄武岩'''
    soul_soil="soul_soil"
    '''灵魂土'''
    soul_fire="soul_fire"
    '''灵魂火'''
    nether_sprouts="nether_sprouts"
    '''下界苗'''
    target="target"
    '''标靶'''
    stripped_crimson_stem="stripped_crimson_stem"
    '''去皮绯红菌柄'''
    stripped_warped_stem="stripped_warped_stem"
    '''去皮诡异菌柄'''
    crimson_planks="crimson_planks"
    '''绯红木板'''
    warped_planks="warped_planks"
    '''诡异木板'''
    crimson_door="crimson_door"
    '''绯红木门'''
    warped_door="warped_door"
    '''诡异木门'''
    crimson_trapdoor="crimson_trapdoor"
    '''绯红木活板门'''
    warped_trapdoor="warped_trapdoor"
    '''诡异木活板门'''
    crimson_standing_sign="crimson_standing_sign"
    '''绯红木告示牌'''
    warped_standing_sign="warped_standing_sign"
    '''诡异木告示牌'''
    crimson_wall_sign="crimson_wall_sign"
    '''墙上的绯红木告示牌'''
    warped_wall_sign="warped_wall_sign"
    '''墙上的诡异木告示牌'''
    crimson_stairs="crimson_stairs"
    '''绯红木楼梯'''
    warped_stairs="warped_stairs"
    '''诡异木楼梯'''
    crimson_fence="crimson_fence"
    '''绯红木栅栏'''
    warped_fence="warped_fence"
    '''诡异木栅栏'''
    crimson_fence_gate="crimson_fence_gate"
    '''绯红木栅栏门'''
    warped_fence_gate="warped_fence_gate"
    '''诡异木栅栏门'''
    crimson_button="crimson_button"
    '''绯红木按钮'''
    warped_button="warped_button"
    '''诡异木按钮'''
    crimson_pressure_plate="crimson_pressure_plate"
    '''绯红木压力板'''
    warped_pressure_plate="warped_pressure_plate"
    '''诡异木压力板'''
    crimson_slab="crimson_slab"
    '''绯红木台阶'''
    warped_slab="warped_slab"
    '''诡异木台阶'''
    crimson_double_slab="crimson_double_slab"
    '''双层绯红木台阶'''
    warped_double_slab="warped_double_slab"
    '''双层诡异木台阶'''
    soul_torch="soul_torch"
    '''灵魂火把'''
    soul_lantern="soul_lantern"
    '''灵魂灯笼'''
    netherite_block="netherite_block"
    '''下界合金块'''
    ancient_debris="ancient_debris"
    '''远古残骸'''
    respawn_anchor="respawn_anchor"
    '''重生锚'''
    blackstone="blackstone"
    '''黑石'''
    polished_blackstone_bricks="polished_blackstone_bricks"
    '''磨制黑石砖'''
    polished_blackstone_brick_stairs="polished_blackstone_brick_stairs"
    '''磨制黑石砖楼梯'''
    blackstone_stairs="blackstone_stairs"
    '''黑石楼梯'''
    blackstone_wall="blackstone_wall"
    '''黑石墙'''
    polished_blackstone_brick_wall="polished_blackstone_brick_wall"
    '''磨制黑石砖墙'''
    chiseled_polished_blackstone="chiseled_polished_blackstone"
    '''雕纹磨制黑石'''
    cracked_polished_blackstone_bricks="cracked_polished_blackstone_bricks"
    '''裂纹磨制黑石砖'''
    gilded_blackstone="gilded_blackstone"
    '''镶金黑石'''
    blackstone_slab="blackstone_slab"
    '''黑石台阶'''
    blackstone_double_slab="blackstone_double_slab"
    '''双层黑石台阶'''
    polished_blackstone_brick_slab="polished_blackstone_brick_slab"
    '''磨制黑石砖台阶'''
    polished_blackstone_brick_double_slab="polished_blackstone_brick_double_slab"
    '''双层磨制黑石砖台阶'''
    chain="chain"
    '''锁链'''
    twisting_vines="twisting_vines"
    '''缠怨藤'''
    nether_gold_ore="nether_gold_ore"
    '''下界金矿石'''
    crying_obsidian="crying_obsidian"
    '''哭泣的黑曜石'''
    soul_campfire="soul_campfire"
    '''灵魂营火'''
    polished_blackstone="polished_blackstone"
    '''磨制黑石'''
    polished_blackstone_stairs="polished_blackstone_stairs"
    '''磨制黑石楼梯'''
    polished_blackstone_slab="polished_blackstone_slab"
    '''磨制黑石台阶'''
    polished_blackstone_double_slab="polished_blackstone_double_slab"
    '''双层磨制黑石台阶'''
    polished_blackstone_pressure_plate="polished_blackstone_pressure_plate"
    '''磨制黑石压力板'''
    polished_blackstone_button="polished_blackstone_button"
    '''磨制黑石按钮'''
    polished_blackstone_wall="polished_blackstone_wall"
    '''磨制黑石墙'''
    warped_hyphae="warped_hyphae"
    '''诡异菌核'''
    crimson_hyphae="crimson_hyphae"
    '''绯红菌核'''
    stripped_crimson_hyphae="stripped_crimson_hyphae"
    '''去皮绯红菌核'''
    stripped_warped_hyphae="stripped_warped_hyphae"
    '''去皮诡异菌核'''
    chiseled_nether_bricks="chiseled_nether_bricks"
    '''雕纹下界砖块'''
    cracked_nether_bricks="cracked_nether_bricks"
    '''裂纹下界砖块'''
    quartz_bricks="quartz_bricks"
    '''石英砖'''
    unknown="unknown"
    '''未知'''
    powder_snow="powder_snow"
    '''细雪'''
    sculk_sensor="sculk_sensor"
    '''幽匿感测体'''
    pointed_dripstone="pointed_dripstone"
    '''滴水石锥'''
    copper_ore="copper_ore"
    '''铜矿石'''
    lightning_rod="lightning_rod"
    '''避雷针'''
    dripstone_block="dripstone_block"
    '''滴水石块'''
    dirt_with_roots="dirt_with_roots"
    '''缠根泥土'''
    hanging_roots="hanging_roots"
    '''垂根'''
    moss_block="moss_block"
    '''苔藓块'''
    spore_blossom="spore_blossom"
    '''孢子花'''
    cave_vines="cave_vines"
    '''洞穴藤蔓'''
    big_dripleaf="big_dripleaf"
    '''大型垂滴叶'''
    azalea_leaves="azalea_leaves"
    '''杜鹃树叶'''
    azalea_leaves_flowered="azalea_leaves_flowered"
    '''盛开的杜鹃树叶'''
    calcite="calcite"
    '''方解石'''
    amethyst_block="amethyst_block"
    '''紫水晶块'''
    budding_amethyst="budding_amethyst"
    '''紫水晶母岩'''
    amethyst_cluster="amethyst_cluster"
    '''紫水晶簇'''
    large_amethyst_bud="large_amethyst_bud"
    '''大型紫晶芽'''
    medium_amethyst_bud="medium_amethyst_bud"
    '''中型紫晶芽'''
    small_amethyst_bud="small_amethyst_bud"
    '''小型紫晶芽'''
    tuff="tuff"
    '''凝灰岩'''
    tinted_glass="tinted_glass"
    '''遮光玻璃'''
    moss_carpet="moss_carpet"
    '''覆地苔藓'''
    small_dripleaf="small_dripleaf"
    '''小型垂滴叶'''
    azalea="azalea"
    '''杜鹃花丛'''
    flowering_azalea="flowering_azalea"
    '''盛开的杜鹃花丛'''
    glow_frame="glow_frame"
    '''荧光物品展示框'''
    copper_block="copper_block"
    '''铜块'''
    exposed_copper="exposed_copper"
    '''斑驳的铜块'''
    weathered_copper="weathered_copper"
    '''锈蚀的铜块'''
    oxidized_copper="oxidized_copper"
    '''氧化的铜块'''
    waxed_copper="waxed_copper"
    '''涂蜡的铜块'''
    waxed_exposed_copper="waxed_exposed_copper"
    '''涂蜡的斑驳铜块'''
    waxed_weathered_copper="waxed_weathered_copper"
    '''涂蜡的锈蚀铜块'''
    cut_copper="cut_copper"
    '''切制铜块'''
    exposed_cut_copper="exposed_cut_copper"
    '''斑驳的切制铜块'''
    weathered_cut_copper="weathered_cut_copper"
    '''锈蚀的切制铜块'''
    oxidized_cut_copper="oxidized_cut_copper"
    '''氧化的切制铜块'''
    waxed_cut_copper="waxed_cut_copper"
    '''涂蜡的切制铜块'''
    waxed_exposed_cut_copper="waxed_exposed_cut_copper"
    '''涂蜡的斑驳切制铜块'''
    waxed_weathered_cut_copper="waxed_weathered_cut_copper"
    '''涂蜡的锈蚀切制铜块'''
    cut_copper_stairs="cut_copper_stairs"
    '''切制铜楼梯'''
    exposed_cut_copper_stairs="exposed_cut_copper_stairs"
    '''斑驳的切制铜楼梯'''
    weathered_cut_copper_stairs="weathered_cut_copper_stairs"
    '''锈蚀的切制铜楼梯'''
    oxidized_cut_copper_stairs="oxidized_cut_copper_stairs"
    '''氧化的切制铜楼梯'''
    waxed_cut_copper_stairs="waxed_cut_copper_stairs"
    '''涂蜡的切制铜楼梯'''
    waxed_exposed_cut_copper_stairs="waxed_exposed_cut_copper_stairs"
    '''涂蜡的斑驳切制铜楼梯'''
    waxed_weathered_cut_copper_stairs="waxed_weathered_cut_copper_stairs"
    '''涂蜡的锈蚀切制铜楼梯'''
    cut_copper_slab="cut_copper_slab"
    '''切制铜台阶'''
    exposed_cut_copper_slab="exposed_cut_copper_slab"
    '''斑驳的切制铜台阶'''
    weathered_cut_copper_slab="weathered_cut_copper_slab"
    '''锈蚀的切制铜台阶'''
    oxidized_cut_copper_slab="oxidized_cut_copper_slab"
    '''氧化的切制铜台阶'''
    waxed_cut_copper_slab="waxed_cut_copper_slab"
    '''涂蜡的切制铜台阶'''
    waxed_exposed_cut_copper_slab="waxed_exposed_cut_copper_slab"
    '''涂蜡的斑驳切制铜台阶'''
    waxed_weathered_cut_copper_slab="waxed_weathered_cut_copper_slab"
    '''涂蜡的锈蚀切制铜台阶'''
    double_cut_copper_slab="double_cut_copper_slab"
    '''双切制铜台阶'''
    exposed_double_copper_slab="exposed_double_copper_slab"
    '''斑驳的双切制铜台阶'''
    weathered_double_cut_copper_slab="weathered_double_cut_copper_slab"
    '''锈蚀的双切制铜台阶'''
    oxidized_double_cut_copper_slab="oxidized_double_cut_copper_slab"
    '''氧化的双切制铜台阶'''
    waxed_double_cut_copper_slab="waxed_double_cut_copper_slab"
    '''涂蜡双切制铜台阶'''
    waxed_exposed_double_cut_copper_slab="waxed_exposed_double_cut_copper_slab"
    '''斑驳的涂蜡双切制铜台阶'''
    waxed_weathered_double_cut_copper_slab="waxed_weathered_double_cut_copper_slab"
    '''锈蚀的涂蜡双切制铜台阶'''
    cave_vines_body_berries="cave_vines_body_berries"
    '''洞穴藤蔓（带浆果）'''
    cave_vines_head_berries="cave_vines_head_berries"
    '''洞穴藤蔓首部（带浆果）'''
    smooth_basalt="smooth_basalt"
    '''平滑玄武岩'''
    deepslate="deepslate"
    '''深板岩'''
    cobbled_deepslate="cobbled_deepslate"
    '''深板岩圆石'''
    cobbled_deepslate_slab="cobbled_deepslate_slab"
    '''深板岩圆石台阶'''
    cobbled_deepslate_stairs="cobbled_deepslate_stairs"
    '''深板岩圆石楼梯'''
    cobbled_deepslate_wall="cobbled_deepslate_wall"
    '''深板岩圆石墙'''
    polished_deepslate="polished_deepslate"
    '''磨制深板岩'''
    polished_deepslate_slab="polished_deepslate_slab"
    '''磨制深板岩台阶'''
    polished_deepslate_stairs="polished_deepslate_stairs"
    '''磨制深板岩楼梯'''
    polished_deepslate_wall="polished_deepslate_wall"
    '''磨制深板岩墙'''
    deepslate_tiles="deepslate_tiles"
    '''深板岩瓦'''
    deepslate_tile_slab="deepslate_tile_slab"
    '''深板岩瓦台阶'''
    deepslate_tile_stairs="deepslate_tile_stairs"
    '''深板岩瓦楼梯'''
    deepslate_tile_wall="deepslate_tile_wall"
    '''深板岩瓦墙'''
    deepslate_bricks="deepslate_bricks"
    '''深板岩砖'''
    deepslate_brick_slab="deepslate_brick_slab"
    '''深板岩砖台阶'''
    deepslate_brick_stairs="deepslate_brick_stairs"
    '''深板岩砖楼梯'''
    deepslate_brick_wall="deepslate_brick_wall"
    '''深板岩砖墙'''
    chiseled_deepslate="chiseled_deepslate"
    '''雕纹深板岩'''
    cobbled_deepslate_double_slab="cobbled_deepslate_double_slab"
    '''双层深板岩圆石台阶'''
    polished_deepslate_double_slab="polished_deepslate_double_slab"
    '''双层磨制深板岩台阶'''
    deepslate_tile_double_slab="deepslate_tile_double_slab"
    '''双层深板岩瓦台阶'''
    deepslate_brick_double_slab="deepslate_brick_double_slab"
    '''双层深板岩砖台阶'''
    deepslate_lapis_lazuli_ore="deepslate_lapis_lazuli_ore"
    '''深层青金石矿石'''
    deepslate_iron_ore="deepslate_iron_ore"
    '''深层铁矿石'''
    deepslate_gold_ore="deepslate_gold_ore"
    '''深层金矿石'''
    deepslate_redstone_ore="deepslate_redstone_ore"
    '''深层红石矿石'''
    lit_deepslate_redstone_ore="lit_deepslate_redstone_ore"
    '''发光的深层红石矿石'''
    deepslate_diamond_ore="deepslate_diamond_ore"
    '''深层钻石矿石'''
    deepslate_coal_ore="deepslate_coal_ore"
    '''深层煤矿石'''
    deepslate_emerald_ore="deepslate_emerald_ore"
    '''深层绿宝石矿石'''
    deepslate_copper_ore="deepslate_copper_ore"
    '''深层铜矿石'''
    cracked_deepslate_tiles="cracked_deepslate_tiles"
    '''裂纹深板岩瓦'''
    cracked_deepslate_bricks="cracked_deepslate_bricks"
    '''裂纹深板岩砖'''
    glow_lichen="glow_lichen"
    '''发光地衣'''
    candle="candle"
    '''蜡烛'''
    white_candle="white_candle"
    '''白色蜡烛'''
    orange_candle="orange_candle"
    '''橙色蜡烛'''
    magenta_candle="magenta_candle"
    '''品红色蜡烛'''
    light_blue_candle="light_blue_candle"
    '''淡蓝色蜡烛'''
    yellow_candle="yellow_candle"
    '''黄色蜡烛'''
    lime_candle="lime_candle"
    '''黄绿色蜡烛'''
    pink_candle="pink_candle"
    '''粉红色蜡烛'''
    gray_candle="gray_candle"
    '''灰色蜡烛'''
    light_gray_candle="light_gray_candle"
    '''淡灰色蜡烛'''
    cyan_candle="cyan_candle"
    '''青色蜡烛'''
    purple_candle="purple_candle"
    '''紫色蜡烛'''
    blue_candle="blue_candle"
    '''蓝色蜡烛'''
    brown_candle="brown_candle"
    '''棕色蜡烛'''
    green_candle="green_candle"
    '''绿色蜡烛'''
    red_candle="red_candle"
    '''红色蜡烛'''
    black_candle="black_candle"
    '''黑色蜡烛'''
    candle_cake="candle_cake"
    '''插上蜡烛的蛋糕'''
    white_candle_cake="white_candle_cake"
    '''插上白色蜡烛的蛋糕'''
    orange_candle_cake="orange_candle_cake"
    '''插上橙色蜡烛的蛋糕'''
    magenta_candle_cake="magenta_candle_cake"
    '''插上品红色蜡烛的蛋糕'''
    light_blue_candle_cake="light_blue_candle_cake"
    '''插上淡蓝色蜡烛的蛋糕'''
    yellow_candle_cake="yellow_candle_cake"
    '''插上黄色蜡烛的蛋糕'''
    lime_candle_cake="lime_candle_cake"
    '''插上黄绿色蜡烛的蛋糕'''
    pink_candle_cake="pink_candle_cake"
    '''插上粉红色蜡烛的蛋糕'''
    gray_candle_cake="gray_candle_cake"
    '''插上灰色蜡烛的蛋糕'''
    light_gray_candle_cake="light_gray_candle_cake"
    '''插上淡灰色蜡烛的蛋糕'''
    cyan_candle_cake="cyan_candle_cake"
    '''插上青色蜡烛的蛋糕'''
    purple_candle_cake="purple_candle_cake"
    '''插上紫色蜡烛的蛋糕'''
    blue_candle_cake="blue_candle_cake"
    '''插上蓝色蜡烛的蛋糕'''
    brown_candle_cake="brown_candle_cake"
    '''插上棕色蜡烛的蛋糕'''
    green_candle_cake="green_candle_cake"
    '''插上绿色蜡烛的蛋糕'''
    red_candle_cake="red_candle_cake"
    '''插上红色蜡烛的蛋糕'''
    black_candle_cake="black_candle_cake"
    '''插上黑色蜡烛的蛋糕'''
    waxed_oxidized_copper="waxed_oxidized_copper"
    '''涂蜡的氧化铜块'''
    waxed_oxidized_cut_copper="waxed_oxidized_cut_copper"
    '''涂蜡的氧化切制铜块'''
    waxed_oxidized_cut_copper_stairs="waxed_oxidized_cut_copper_stairs"
    '''涂蜡的氧化切制铜楼梯'''
    waxed_oxidized_cut_copper_slab="waxed_oxidized_cut_copper_slab"
    '''涂蜡的氧化切制铜台阶'''
    waxed_oxidized_double_cut_copper_slab="waxed_oxidized_double_cut_copper_slab"
    '''涂蜡的氧化双切制铜台阶'''
    raw_iron_block="raw_iron_block"
    '''粗铁块'''
    raw_copper_block="raw_copper_block"
    '''粗铜块'''
    raw_gold_block="raw_gold_block"
    '''粗金块'''
    infested_deepslate="infested_deepslate"
    '''虫蚀深板岩'''
    sculk="sculk"
    '''幽匿块'''
    sculk_vein="sculk_vein"
    '''幽匿脉络'''
    sculk_catalyst="sculk_catalyst"
    '''幽匿催发体'''
    sculk_shrieker="sculk_shrieker"
    '''幽匿尖啸体'''
    client_request_placeholder_block="client_request_placeholder_block"
    '''客户端请求占位符方块'''
    reinforced_deepslate="reinforced_deepslate"
    '''强化深板岩'''
    frog_spawn="frog_spawn"
    '''青蛙卵'''
    pearlescent_froglight="pearlescent_froglight"
    '''珠光蛙明灯'''
    verdant_froglight="verdant_froglight"
    '''青翠蛙明灯'''
    ochre_froglight="ochre_froglight"
    '''赭黄蛙明灯'''
    mangrove_leaves="mangrove_leaves"
    '''红树树叶'''
    mud="mud"
    '''泥巴'''
    mangrove_propagule="mangrove_propagule"
    '''红树胎生苗'''
    mud_bricks="mud_bricks"
    '''泥砖'''
    packed_mud="packed_mud"
    '''泥坯'''
    mud_brick_slab="mud_brick_slab"
    '''泥砖台阶'''
    mud_brick_double_slab="mud_brick_double_slab"
    '''双层泥砖台阶'''
    mud_brick_stairs="mud_brick_stairs"
    '''泥砖楼梯'''
    mud_brick_wall="mud_brick_wall"
    '''泥砖墙'''
    mangrove_roots="mangrove_roots"
    '''红树根'''
    muddy_mangrove_roots="muddy_mangrove_roots"
    '''沾泥的红树根'''
    mangrove_log="mangrove_log"
    '''红树原木'''
    stripped_mangrove_log="stripped_mangrove_log"
    '''去皮红树原木'''
    mangrove_planks="mangrove_planks"
    '''红树木板'''
    mangrove_button="mangrove_button"
    '''红树木按钮'''
    mangrove_stairs="mangrove_stairs"
    '''红树木楼梯'''
    mangrove_slab="mangrove_slab"
    '''红树木台阶'''
    mangrove_pressure_plate="mangrove_pressure_plate"
    '''红树木压力板'''
    mangrove_fence="mangrove_fence"
    '''红树木栅栏'''
    mangrove_fence_gate="mangrove_fence_gate"
    '''红树木栅栏门'''
    mangrove_door="mangrove_door"
    '''红树木门'''
    mangrove_standing_sign="mangrove_standing_sign"
    '''红树木告示牌'''
    mangrove_wall_sign="mangrove_wall_sign"
    '''墙上的红树木告示牌'''
    mangrove_trapdoor="mangrove_trapdoor"
    '''红树木活板门'''
    mangrove_wood="mangrove_wood"
    '''红树木'''
    stripped_mangrove_wood="stripped_mangrove_wood"
    '''去皮红树木'''
    mangrove_double_slab="mangrove_double_slab"
    '''双层红树木台阶'''
    oak_hanging_sign="oak_hanging_sign"
    '''橡木悬挂式告示牌'''
    spruce_hanging_sign="spruce_hanging_sign"
    '''云杉木悬挂式告示牌'''
    birch_hanging_sign="birch_hanging_sign"
    '''白桦木悬挂式告示牌'''
    jungle_hanging_sign="jungle_hanging_sign"
    '''丛林木悬挂式告示牌'''
    acacia_hanging_sign="acacia_hanging_sign"
    '''金合欢木悬挂式告示牌'''
    dark_oak_hanging_sign="dark_oak_hanging_sign"
    '''深色橡木悬挂式告示牌'''
    crimson_hanging_sign="crimson_hanging_sign"
    '''绯红木悬挂式告示牌'''
    warped_hanging_sign="warped_hanging_sign"
    '''诡异木悬挂式告示牌'''
    mangrove_hanging_sign="mangrove_hanging_sign"
    '''红树木悬挂式告示牌'''
    bamboo_mosaic="bamboo_mosaic"
    '''竹马赛克'''
    bamboo_planks="bamboo_planks"
    '''竹板'''
    bamboo_button="bamboo_button"
    '''竹按钮'''
    bamboo_stairs="bamboo_stairs"
    '''竹楼梯'''
    bamboo_slab="bamboo_slab"
    '''竹台阶'''
    bamboo_pressure_plate="bamboo_pressure_plate"
    '''竹压力板'''
    bamboo_fence="bamboo_fence"
    '''竹栅栏'''
    bamboo_fence_gate="bamboo_fence_gate"
    '''竹栅栏门'''
    bamboo_door="bamboo_door"
    '''竹门'''
    bamboo_standing_sign="bamboo_standing_sign"
    '''竹告示牌'''
    bamboo_wall_sign="bamboo_wall_sign"
    '''墙上的竹告示牌'''
    bamboo_trapdoor="bamboo_trapdoor"
    '''竹活板门'''
    bamboo_double_slab="bamboo_double_slab"
    '''竹板'''
    bamboo_hanging_sign="bamboo_hanging_sign"
    '''悬挂式竹告示牌'''
    bamboo_mosaic_stairs="bamboo_mosaic_stairs"
    '''竹马赛克楼梯'''
    bamboo_mosaic_slab="bamboo_mosaic_slab"
    '''竹马赛克台阶'''
    bamboo_mosaic_double_slab="bamboo_mosaic_double_slab"
    '''双层竹马赛克台阶'''
    chiseled_bookshelf="chiseled_bookshelf"
    '''雕纹书架'''
    bamboo_block="bamboo_block"
    '''竹块'''
    stripped_bamboo_block="stripped_bamboo_block"
    '''去皮竹块'''
    suspicious_sand="suspicious_sand"
    '''可疑的沙子'''
    cherry_button="cherry_button"
    '''樱花木按钮'''
    cherry_door="cherry_door"
    '''樱花木门'''
    cherry_fence="cherry_fence"
    '''樱花木栅栏'''
    cherry_fence_gate="cherry_fence_gate"
    '''樱花木栅栏门'''
    cherry_hanging_sign="cherry_hanging_sign"
    '''悬挂式樱花木告示牌'''
    stripped_cherry_log="stripped_cherry_log"
    '''去皮樱花原木'''
    cherry_log="cherry_log"
    '''樱花原木'''
    cherry_planks="cherry_planks"
    '''樱花木板'''
    cherry_pressure_Plate="cherry_pressure_Plate"
    '''樱花木压力板'''
    cherry_slab="cherry_slab"
    '''樱花木台阶'''
    cherry_double_slab="cherry_double_slab"
    '''双层樱花木台阶'''
    cherry_stairs="cherry_stairs"
    '''樱花木楼梯'''
    cherry_standing_sign="cherry_standing_sign"
    '''樱花木告示牌'''
    cherry_trapdoor="cherry_trapdoor"
    '''樱花木活板门'''
    cherry_wall_sign="cherry_wall_sign"
    '''墙上的樱花木告示牌'''
    stripped_cherry_wood="stripped_cherry_wood"
    '''去皮樱花木'''
    cherry_wood="cherry_wood"
    '''樱花木'''
    cherry_sapling="cherry_sapling"
    '''樱花树苗'''
    cherry_leaves="cherry_leaves"
    '''樱花树叶'''
    pink_petals="pink_petals"
    '''粉红色花簇'''
    decorated_pot="decorated_pot"
    '''饰纹陶罐'''
    light_gray_wool="light_gray_wool"
    '''淡灰色羊毛'''
    gray_wool="gray_wool"
    '''灰色羊毛'''
    black_wool="black_wool"
    '''黑色羊毛'''
    brown_wool="brown_wool"
    '''棕色羊毛'''
    red_wool="red_wool"
    '''红色羊毛'''
    orange_wool="orange_wool"
    '''橙色羊毛'''
    yellow_wool="yellow_wool"
    '''黄色羊毛'''
    lime_wool="lime_wool"
    '''黄绿色羊毛'''
    green_wool="green_wool"
    '''绿色羊毛'''
    cyan_wool="cyan_wool"
    '''青色羊毛'''
    light_blue_wool="light_blue_wool"
    '''淡蓝色羊毛'''
    blue_wool="blue_wool"
    '''蓝色羊毛'''
    purple_wool="purple_wool"
    '''紫色羊毛'''
    magenta_wool="magenta_wool"
    '''品红色羊毛'''
    pink_wool="pink_wool"
    '''粉红色羊毛'''
    torchflower_crop="torchflower_crop"
    '''火把花植株'''
    torchflower="torchflower"
    '''火把花'''
    spruce_log="spruce_log"
    '''云杉原木'''
    birch_log="birch_log"
    '''白桦原木'''
    jungle_log="jungle_log"
    '''丛林原木'''
    dark_oak_log="dark_oak_log"
    '''深色橡木原木'''
    suspicious_gravel="suspicious_gravel"
    '''可疑的沙砾'''
    pitcher_crop="pitcher_crop"
    '''瓶子草植株'''
    acacia_fence="acacia_fence"
    '''金合欢木栅栏'''
    birch_fence="birch_fence"
    '''白桦木栅栏'''
    dark_oak_fence="dark_oak_fence"
    '''深色橡木栅栏'''
    jungle_fence="jungle_fence"
    '''丛林木栅栏'''
    spruce_fence="spruce_fence"
    '''云杉木栅栏'''
    calibrated_sculk_sensor="calibrated_sculk_sensor"
    '''校频幽匿感测体'''
    brain_coral="brain_coral"
    '''脑纹珊瑚'''
    bubble_coral="bubble_coral"
    '''气泡珊瑚'''
    fire_coral="fire_coral"
    '''火珊瑚'''
    horn_coral="horn_coral"
    '''鹿角珊瑚'''
    dead_tube_coral="dead_tube_coral"
    '''失活的管珊瑚'''
    dead_brain_coral="dead_brain_coral"
    '''失活的脑纹珊瑚'''
    dead_bubble_coral="dead_bubble_coral"
    '''失活的气泡珊瑚'''
    dead_fire_coral="dead_fire_coral"
    '''失活的火珊瑚'''
    dead_horn_coral="dead_horn_coral"
    '''失活的鹿角珊瑚'''
    sniffer_egg="sniffer_egg"
    '''嗅探兽蛋'''
    orange_carpet="orange_carpet"
    '''橙色地毯'''
    magenta_carpet="magenta_carpet"
    '''品红色地毯'''
    light_blue_carpet="light_blue_carpet"
    '''淡蓝色地毯'''
    yellow_carpet="yellow_carpet"
    '''黄色地毯'''
    lime_carpet="lime_carpet"
    '''黄绿色地毯'''
    pink_carpet="pink_carpet"
    '''粉红色地毯'''
    gray_carpet="gray_carpet"
    '''灰色地毯'''
    light_gray_carpet="light_gray_carpet"
    '''淡灰色地毯'''
    cyan_carpet="cyan_carpet"
    '''青色地毯'''
    purple_carpet="purple_carpet"
    '''紫色地毯'''
    blue_carpet="blue_carpet"
    '''蓝色地毯'''
    brown_carpet="brown_carpet"
    '''棕色地毯'''
    green_carpet="green_carpet"
    '''绿色地毯'''
    red_carpet="red_carpet"
    '''红色地毯'''
    black_carpet="black_carpet"
    '''黑色地毯'''
    pitcher_plant="pitcher_plant"
    '''瓶子草'''

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
    covered_bit={'covered_bit':[False,True]}
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
    double_plant_type={'double_plant_type':['fern','grass','paeonia','rose','sunflower','syringa']}
    '''高草丛的类型 0-5'''
    allow_underwater_bit={"allow_underwater_bit":[False,True]}
    '''tnt type 0-1'''
    explode_bit={'explode_bit':[False,True]}
    '''是否具备普通TNT/水下TNT的所有特性，还能被处于生存模式的玩家以破坏的方式点燃 0-1'''
    disarmed_bit={"disarmed_bit":[False,True]}
    '''是否被拆除 0-1'''
    suspended_bit={'suspended_bit':[False,True]}
    '''如果绊线没有连接到有效的绊线钩，则为true，但是一旦连接到有效的绊线钩后，此值永远都为false，即使它再次与绊线钩断开，该值也不会发生改变 0-1'''
    turtle_egg_count={"turtle_egg_count":[0,1,2,3]}
    '''蛋的数量 0-3'''
    cracked_state={'cracked_state':['no_cracks','cracked',"max_cracked"]}
    '''蛋的碎裂程度 0-2'''
    twisting_vines_age={'twisting_vines_age':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]}
    '''生长程度 0-25'''
    vine_direction_bits={"vine_direction_bits":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]}
    '''附着的方向 0-15'''
    weeping_vines_age={'weeping_vines_age':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]}
    '''生长程度 0-25'''
    stripped_bit={"stripped_bit":[False,True]}
    '''是否被去皮 0-1'''

class block_list(_block_list):
    '''方块列表'''
    '''这里这么写是方便代码'''
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
    
    class _mushroom_block(_block_name):
        def __init__(self, name) -> None:   
            super().__init__(name)
            self.huge_mushroom_bits=_get_block_attr(_block_status.huge_mushroom_bits)
            '''方块朝向 1-15'''
        def set_attr(self,huge_mushroom_bits:int=None):
            return self._command_attr_park(huge_mushroom_bits=huge_mushroom_bits)
        
    anvil=_anvil(_block_list.anvil)
    '''铁砧'''
    amethyst_cluster=_amethyst_cluster(_block_list.amethyst_cluster)
    '''紫水晶簇'''
    brown_mushroom_block=_mushroom_block(_block_list.brown_mushroom_block)
    '''棕色蘑菇块'''
    red_mushroom_block=_mushroom_block(_block_list.red_mushroom_block)
    '''红色蘑菇块'''
    
color_block_62 = {
    block_list.glass: (0, 0, 0),
    block_list.slime: (127, 178, 56),
    block_list.sandstone: (247, 233, 163),
    block_list.brown_mushroom_block.huge_mushroom_bits[15]: (199, 199, 199),
    block_list.redstone_block: (255, 0, 0),
    block_list.blue_ice: (160, 160, 255),
    block_list.iron_block: (167, 167, 167),
    block_list.leaves: (0, 124, 0),
    block_list.white_wool: (255, 255, 255),
    block_list.clay: (164, 168, 184),
    block_list.dirt: (151, 109, 77),
    block_list.cobblestone: (112, 112, 112),
    block_list.water: (64, 64, 255),
    block_list.planks: (143, 119, 72),
    block_list.quartz_block: (255, 252, 245),
    block_list.orange_wool: (216, 127, 51),
    block_list.magenta_wool: (178, 76, 216),
    block_list.light_blue_wool: (102, 153, 216),
    block_list.yellow_wool: (229, 229, 51),
    block_list.lime_wool: (127, 204, 25),
    block_list.pink_wool: (242, 127, 165),
    block_list.gray_wool: (76, 76, 76),
    block_list.light_gray_wool: (153, 153, 153),
    block_list.cyan_wool: (76, 127, 153),
    block_list.purple_wool: (127, 63, 178),
    block_list.blue_wool: (51, 76, 178),
    block_list.brown_wool: (102, 76, 51),
    block_list.green_wool: (102, 127, 51),
    block_list.red_wool: (153, 51, 51),
    block_list.black_wool: (25, 25, 25),
    block_list.gold_block: (250, 238, 77),
    block_list.diamond_block: (92, 219, 213),
    block_list.lapis_block: (74, 128, 255),
    block_list.emerald_block: (0, 217, 58),
    block_list.podzol: (129, 86, 4),
    block_list.netherrack: (112, 2, 0),
    block_list.cherry_planks: (209, 177, 161),
    block_list.brown_terracotta: (159, 82, 36),
    block_list.magenta_terracotta: (149, 87, 108),
    block_list.light_blue_terracotta: (112, 108, 138),
    block_list.yellow_terracotta: (186, 133, 36),
    block_list.lime_terracotta: (103, 117, 53),
    block_list.pink_terracotta: (160, 77, 78),
    block_list.gray_terracotta: (57, 41, 35),
    block_list.light_gray_terracotta: (135, 107, 98),
    block_list.cyan_terracotta: (87, 92, 92),
    block_list.purple_terracotta: (122, 73, 88),
    block_list.blue_terracotta: (76, 62, 92),
    block_list.brown_terracotta: (76, 50, 35),
    block_list.green_terracotta: (76, 82, 42),
    block_list.red_terracotta: (142, 60, 46),
    block_list.black_terracotta: (37, 22, 16),
    block_list.crimson_nylium: (189, 48, 49),
    block_list.crimson_planks: (148, 63, 97),
    block_list.crimson_hyphae: (92, 25, 29),
    block_list.warped_nylium: (22, 126, 134),
    block_list.warped_planks: (58, 142, 140),
    block_list.warped_hyphae: (86, 44, 62),
    block_list.warped_wart_block: (20, 180, 133),
    block_list.deepslate: (100, 100, 100),
    block_list.raw_iron_block: (216, 175, 147),
    block_list.verdant_froglight: (127, 167, 150)
}
'''62色的颜色对应字典{block_name:(RGB)...}'''

