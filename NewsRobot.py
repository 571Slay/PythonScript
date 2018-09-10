# -*- coding:utf-8 -*-
#Author:MercuryYe
import urllib.request
import numpy as np
import pandas as pd
import jieba.analyse
from bs4 import BeautifulSoup


###爬虫部分###
url = "http://www.bishijie.com/kuaixun"
print("请稍等，正在爬行中......")
#模拟浏览器请求
headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read()
data = data.decode('utf-8')
#将获取到内容扔进BeautifulSoup中转换格式
soup = BeautifulSoup(data, 'html.parser')
result = soup.find_all('a', target='_blank')
result = list(set(result))
filter(None, result)
for link in result:
	title = str(link.get('title'))
	filewrite = open('vaule.txt','a+')
	filewrite.write(title)
	filewrite.close()

###提取关键词部分###
#定义函数
def read_from_file(directions):
	decode_set=['utf-8','gb18030','ISO-8859-2','gb2312','gbk','Error']
	for k in decode_set:
		file = open(directions,"r",encoding=k)
		readfile = file.read()
		file.close()
		break
	return readfile
#读取文件
file_data = str(read_from_file('vaule.txt'))
print("请稍等，正在提权关键词中......\n")
#使用TextRank算法提取关键词
textrank=jieba.analyse.textrank
keywords_TR=textrank(file_data)
print('今日关键词：',set(keywords_TR))
