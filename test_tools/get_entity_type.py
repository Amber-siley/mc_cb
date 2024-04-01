import pandas as pd

exl=pd.read_csv(r".\infor\entity_type.csv",delimiter='\t')

with open("entity_type.txt",encoding="utf-8",mode="w+") as fp:
    for i in range(len(exl)):
        data_list=exl.iloc[i,0].split(",")
        if len(data_list) == 4:
            en=data_list[2]
            zh=data_list[3]
            fp.write(f"""{en} = "{en}"\n '''{zh}'''\n""")
        continue