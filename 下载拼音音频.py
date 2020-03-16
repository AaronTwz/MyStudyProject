import requests
from bs4 import BeautifulSoup

拼音网址 = 'http://du.hanyupinyin.cn/'
拼音节点类型 = 'button expanded chinesepinyin3'

声调网址 = 'http://du.hanyupinyin.cn/shengdiao.html'
声调节点类型 = 'button chinesepinyin3'

type = 2

if (type == 1):
    网址 = 拼音网址
    节点类型 = 拼音节点类型
    名称标记 = 'pinyin_'
elif (type == 2):
    网址 = 声调网址
    节点类型 = 声调节点类型
    名称标记 = 'shengdiao_'

r = requests.get(网址)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'lxml')
result = soup.find_all('a', {'class': 节点类型})
for i in result:
    r = requests.get('http://du.hanyupinyin.cn/du/pinyin/' + i['mp3'])
    with open('pinyin/' + 名称标记 + i.get_text() + '.mp3', 'wb') as f:
        f.write(r.content)

print("下载完毕！")
