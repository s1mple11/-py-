import requests

from lxml import html
import json
headers={"user_agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
url="https://bj.loupan.com/xinfang"
resp=requests.get(url,headers=headers)
page=resp.text
etree = html.etree
html = etree.HTML(page)

divs=html.xpath('/html/body/div[7]/div[3]/div[3]/div[1]/ul/li')
for div in divs:
    name=div.xpath("./div[1]/h2/a/text()")
    area=div.xpath("./div[1]/div[2]/span[2]/a/text()")
    room=div.xpath("./div[1]/div[2]/span[1]/a[1]/text()")
    json_str = json.dumps(name, ensure_ascii=False) + "\n"
    with open("爬虫1.json", "a", encoding="utf-8") as fp:
        fp.write(json_str)

    json_str = json.dumps(area, ensure_ascii=False) + "\n"
    with open("爬虫1.json", "a", encoding="utf-8") as fp:
        fp.write(json_str)

    json_str = json.dumps(room, ensure_ascii=False) + "\n"
    with open("爬虫1.json", "a", encoding="utf-8") as fp:
        fp.write(json_str)

print("over")