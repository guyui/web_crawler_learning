#! /usr/bin/python
# author jiang
# 2023年05月24日
import requests
import parsel
for page in range(1,20):
    url=f'http://www.66ip.cn/{page}.html'#在字符串前面加f，是为了允许在字符串的大括号内添加python表达式
    response=requests.get(url=url)
    response.encoding='gb2312'
    html_data=response.text
    select=parsel.Selector(html_data)
    trs=select.css('#main > div.containerbox.boxindex > div.layui-row.layui-col-space15 > div > table tr')
    for tr in trs[1:]:
    # print(tr.css('td::text').getall())
        ip = tr.css('td::text').getall()[0]
        port = tr.css('td::text').getall()[1]
        text = 'IP地址:' + ip + '------port端口号:' + port + '\n'
        open('ip.txt', mode='a', encoding='utf-8').write(text)
    # for tr in trs[1:]:
    #     ip=tr.css('td::text').getall()[0]
    #     port = tr.css('td::text').getall()[1]
    #     text='IP地址:'+ip+'------port端口号:'+port+'\n'
    #     open('ip.txt',mode='a',encoding='utf-8').write(text)