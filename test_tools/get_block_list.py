import requests
from lxml import html

content=requests.get("https://minecraft.fandom.com/zh/wiki/%E5%9F%BA%E5%B2%A9%E7%89%88%E6%95%B0%E6%8D%AE%E5%80%BC/%E6%96%B9%E5%9D%97ID",timeout=10).text
content_action=html.fromstring(content)
e_name=content_action.xpath("//table[@class='data-table']/tbody/tr/td[position()=4]//text()")
c_name=content_action.xpath("//table[@class='data-table']/tbody/tr/td[last()]/a//text()")
e_name=[i[:-1] if i.endswith("\n") else i for i in e_name if i != '\n']
c_name=[i[:-1] if i.endswith(" ") else i for i in c_name]
with open("only_block.txt","w",encoding='utf-8') as fp:
    index,max=0,len(e_name)
    for i in range(index,max):
        fp.write(f'{e_name[i]}="{e_name[i]}"\n\'\'\'{c_name[i]}\'\'\'\n')