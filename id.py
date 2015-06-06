#-*- coding: utf-8 -*-
import random

yushu=[x for x in range(0,11)] 
ma=['1','0','X','9','8','7','6','5','4','3','2','1']

def yanzheng(nid):

	dicma=dict(zip(yushu,ma))

	sum=0

	for x,y in enumerate(nid[:-1]):

		sum+=((2**(18-x-1))%11)*int(y) #17位对应系数相乘的和

	if nid[-1]==dicma[sum%11]: #校验码对照
		return '%s 真'%nid
	else:
		return '%s 伪'%nid
def readfile(fname):
	f=open('id.txt','rb')
	for line in f.readlines():
		print  yanzheng(line.strip())
	f.close()
def randnum():
	idstr=''
	for i in range(17): #前17位随机
		idstr+=str(random.randint(0,9))

	idstr+=random.choice(ma) #最后一位从列表种随意一个，因为有X
	return idstr


if __name__=="__main__":
	nid=raw_input('请输入您的身份证号：') #用户输入身份证号，没做任何验证
	print yanzheng(nid)  #验证身份证
	readfile('id.txt')   #从文件读出来再验证
	print yanzheng(randnum())  #随机一个在验证