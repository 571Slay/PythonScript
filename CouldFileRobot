# -*- coding:utf-8 -*-
#Author:MercuryYe
import urllib.request
from bs4 import BeautifulSoup

keyword = input("输入要搜索的资源名称：")
#将用户输入进行URL编码，避免出现字符集报错
keyword = urllib.parse.quote(keyword)
url = "http://www.58wangpan.com/search/m1kw"+keyword
url = str(url)
print("请稍等，正在搜索中......")
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
print("----------------------------Result-----------------------------")
for link in result:
	title = link.get('title')
	linklist = link.get('href')
	print("资源标题："+str(title))
	print("资源链接：http://www.58wangpan.com"+str(linklist))
print("PS:部分资源出现被和谐属于正常情况，请尝试其他资源")
