import requests
from lxml import html

content=requests.get("https://zh.minecraft.wiki/w/%E6%96%B9%E5%9D%97%E7%8A%B6%E6%80%81",timeout=10).text
content_action=html.fromstring(content)

tables=content_action.xpath("//table[@class='wikitable']")
all_status=set()
for table in tables:
    title="".join(table.xpath("./tbody/tr[position()=1]/th[position()=1]//text()"))
    if title == '名称':
        status="".join(table.xpath("./tbody/tr[position()=2]/th[position()=1]//text()"))
        all_status.add(status)
print(all_status,'\n',len(all_status))