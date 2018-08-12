#Author:MercuryYe
import os
import re
import urllib.request
from bs4 import BeautifulSoup

#定义核心函数
def getlink(url):
	file = urllib.request.urlopen(url)
	data = str(file.read())
	#构造正则表达式来匹配章节链接
	pat = '<a style="" href="(/book/.*?)"'
	link = re.compile(pat).findall(data)  	
	link = list(link)
	#将章节链接由小到大排序，避免出现章节混乱
	link.sort()
	return link
	
def getbook(link):
	#设置代理信息
	headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
	opener = urllib.request.build_opener()
	opener.addheaders = [headers]
	urllib.request.install_opener(opener)
	data = urllib.request.urlopen(link).read()
	data = data.decode('utf-8')
	soup = BeautifulSoup(data, 'html.parser')
	title = soup.find('h1')
	value = soup.find('div', id="content")
	#使用list.get_text()函数获取文本
	book = title.get_text()+value.get_text()
	print(title.get_text()+" 下载完成...")
	return book

#从用户处获取基本变量
bookid = input("请输入书籍编号（www.qu.la/book/书籍编号/）：")
url = "https://www.qu.la/book/"+bookid
url = str(url)

#生成links.txt
print('================================================')
print('请稍等，正在生成章节链接......')
link = getlink(url)
for linklist in link:
	links = "https://www.qu.la"+linklist[0:]
	filewrite = open('links.txt','a+')
	filewrite.write(links+'\n')
	filewrite.close()
filewrite = open('links.txt','a+')
filewrite.write('end')
filewrite.close()
print('章节链接生成完毕！')

#生成books.txt
print('================================================')
print('请稍等，正在下载小说内容......')
print('等待时间较长，请勿关闭程序或中断网络！')
i = open('links.txt','r')
booklink = i.readlines()
for links in booklink:
	booklinks = links[0:] 
	if booklinks != 'end':
		book = getbook(booklinks)
		filewrite = open('Book.txt','a+')
		filewrite.write(book)
	else:
		filewrite.close()
		os.remove('links.txt')
		print('================================================')
		print('小说下载完成！请在本目录查找Book.txt')
