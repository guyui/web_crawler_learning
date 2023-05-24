#! /usr/bin/python
# author jiang
# 2023年05月24日

#获取单张图片

# import re
#
# import requests
# url="http://www.netbian.com/desk/31131.htm"
#
# response=requests.get(url)
# response.encoding='gbk'
#
# img,title= re.findall('<img src="(.*?)" alt="(.*?)"',response.text)[0]
# print(img,title)
#
# img_content=requests.get(img).content
# with open('img\\'+title+'.jpg',mode='wb') as f:
#     f.write(img_content)

#获取多张图片



# import requests
# import re
# for page in range(2,20):
#     link=f'http://www.netbian.com/index_{page}.htm'
#     html_data=requests.get(link).text
#
#     img_id_list=re.findall('<a href="/desk/(\d+)\.htm" title=',html_data)
#     print(img_id_list)
#     print(len(img_id_list))
#
#     for img_id in img_id_list:
#         url = f"http://www.netbian.com/desk/{img_id}.htm"
#         response=requests.get(url)
#         response.encoding='gbk'
#         img,title= re.findall('<img src="(.*?)" alt="(.*?)"',response.text)[0]
#         print(img,title)
#         img_content=requests.get(img).content
#         with open('img\\'+title+'.jpg',mode='wb') as f:
#             f.write(img_content)


# 设置壁纸
import os
import ctypes
import time
import random
path='E:\\wd_python_l\\爬虫学习\\1.自动获取壁纸&更换壁纸\\img\\'
files=os.listdir(path)

img_file_list=[path+file for file in files]
while True:
    time.sleep(3)
    img_file=random.choice(img_file_list)
    print(img_file)
    ctypes.windll.user32.SystemParametersInfoW(20,0,img_file,3)

for file in files:
    img_file=path+file
    print(img_file)
    ctypes.windll.user32.SystemParameterInfoW(20,0,img_file,3)