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
	pat1 = '<a href="(http://goudidiao.com.*?)"'
	pat2 = '<a href="(http://www.pniao.com.*?)"'
	pat3 = '<a href="(http://www.languang.co.*?)"'
	pat4 = '<a href="(http://www.xunyingwang.com.*?)"'
	pat5 = '<a href="(http://www.dygod.net.*?)"'
	#这里实在不会写了，凑合看吧！
	link1 = re.compile(pat1).findall(data) 	
	link2 = re.compile(pat2).findall(data) 	
	link3 = re.compile(pat3).findall(data) 	
	link4 = re.compile(pat4).findall(data) 	
	link5 = re.compile(pat5).findall(data)
	link = link1+link2+link3+link4+link5
	link = list(set(link))
	return link

movie = input("输入电影名称：")
#将汉字转化为URL编码，避免字符报错
movie = urllib.parse.quote(movie)
url = "http://ifkdy.com/?q="+movie
url = str(url)
linklist = getlink(url)
for link in linklist:
	print(link[0:])
