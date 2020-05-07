#! coding:utf-8

##################################
#  获取机器wifi密码
#  2020/5/7
#  By Silence
##################################

import re
import subprocess

name=[]
def get_wlan_name():
	global name
	cmd="netsh wlan show profiles"
	p=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
	result,err=p.communicate()
	p.wait()
	mymind=str(result.decode('gbk'))
	match=re.findall(': (.*?)\n',mymind)
	for i in match:
		i=i.strip('\r')
		if len(i):
			name.append(i)

num=0
def get_wlan_passwd():
	for i in name:
		global num
		num=num+1
		cmd="netsh wlan show profiles name=%s key=clear"%i
		p=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
		result,err=p.communicate()
		p.wait()
		mymind=str(result.decode('gbk'))
		match=re.findall('关键内容            :(.*?)\n',mymind)
		try:
			if match[0]:
				print("[200]"+name[num-1]+" [==>] "+match[0])
		except:
			print("[400]"+name[num-1]+" 是特殊WIFI")
		continue


def main():
	get_wlan_name()
	get_wlan_passwd()

if __name__=="__main__":
	main()
