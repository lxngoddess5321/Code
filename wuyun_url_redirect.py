#! -*-coding="utf-8" -*-

'''
分析了乌云URL跳转漏洞链接 规则很简单
http://wooyun.2xss.cc/searchbug.php?q=URL%E8%B7%B3%E8%BD%AC&page=17
page参数可控 范围为1-17； 且无反爬虫。 
刚好最近就在学习，就试试手
'''

import requests
import re
import time
from threading import Thread 



def wooyun_url_redirect_download_html(Id):
	url="http://wooyun.2xss.cc/searchbug.php?q=URL%E8%B7%B3%E8%BD%AC&page="+ str(Id)
	r=requests.get(url)
	hack=re.findall('(bug_detail.*?)<',r.text)
	for i in hack:
		with open ("url.txt","a+",encoding="utf-8") as f:
			f.write("http://wooyun.2xss.cc/"+i+"\n")
	print("第"+str(Id)+"页的链接已经爬取完毕！")

if __name__=="__main__":
	AAA=input("请按回车键启动..")
	t1=time.time()
	threads=[]
	for Id in range(1,18):
		t=Thread(target=wooyun_url_redirect_download_html,args=(Id,))
		t.start()
		threads.append(t)
	t.join()
	t2=time.time()
	print("时间消耗:"+str(t2-t1)+"s")
	exit()


