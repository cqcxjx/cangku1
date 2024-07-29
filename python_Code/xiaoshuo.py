# 导入发送请求的包
import requests
# 解析响应内容
from lxml import etree


# 发送给谁
url = 'https://www.luoxia123.com/douluodalu/448925.html'

while True:
    #伪装自己
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }

    # 发送请求
    res = requests.get(url, headers=headers)
    print(res.text)

    # 设置编码
    res.encoding = 'utf-8'

    # 打印响应内容
    #print(res.text)

    e = etree.HTML(res.text)

    # 提取标题
    title = e.xpath('//h1/text()')[0]

    # 提取内容
    content = e.xpath('//div[@class="panel-body"]/p/text()')

    # 获取下一章内容

    url = e.xpath('//div[@class = "m-page"]/a[3]/@href')[0]

    # print(title)
    # 以追加的方式保存到文件里面

    with open('斗罗大陆.txt', 'a', encoding='utf-8') as f:
        f.write(title + '\n')
        for p in content:
            f.write(p + '\n')

        f.write('\n')

        if url == "https://www.luoxia123.com/douluodalu/448925.html" :
            break



      