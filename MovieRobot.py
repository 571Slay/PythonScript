# -*- coding: UTF-8 -*-
#Author:MercuryYe
import re
import urllib.request

def getlink(url):
	#模拟浏览器请求，防止IP被拉入黑名单
	headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
	opener = urllib.request.build_opener()
	opener.addheaders = [headers]
	#将opener设置为全局使用
	urllib.request.install_opener(opener)
	file = urllib.request.urlopen(url)
	data = str(file.read())
	#构造正则表达式来搜索内容
	pat = '<a href="(http://www..*?|http://goudidiao.com.*?)"'
	link = re.compile(pat).findall(data)  	
	link = list(set(link))
	return link

movie = input("输入电影名称：")
print('请稍等，正在搜索中......')
#将汉字转化为URL编码，避免字符报错
movie = urllib.parse.quote(movie)
url = "http://ifkdy.com/?q="+movie
url = str(url)
linklist = getlink(url)
print('----------------------------Result-----------------------------')
for link in linklist:
	print("观看地址："+link[0:])
print('PS：任一观看地址都可以观看哦～')
