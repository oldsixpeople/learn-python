#-*- coding: utf-8 -*-
import random

yushu=[x for x in range(0,11)] 
ma=['1','0','X','9','8','7','6','5','4','3','2','1']

def yanzheng(nid):

	dicma=dict(zip(yushu,ma))

	sum=0

	for x,y in enumerate(nid[:-1]):

		sum+=((2**(18-x-1))%11)*int(y) #17λ��Ӧϵ����˵ĺ�

	if nid[-1]==dicma[sum%11]: #У�������
		return '%s ��'%nid
	else:
		return '%s α'%nid
def readfile(fname):
	f=open('id.txt','rb')
	for line in f.readlines():
		print  yanzheng(line.strip())
	f.close()
def randnum():
	idstr=''
	for i in range(17): #ǰ17λ���
		idstr+=str(random.randint(0,9))

	idstr+=random.choice(ma) #���һλ���б�������һ������Ϊ��X
	return idstr


if __name__=="__main__":
	nid=raw_input('�������������֤�ţ�') #�û��������֤�ţ�û���κ���֤
	print yanzheng(nid)  #��֤���֤
	readfile('id.txt')   #���ļ�����������֤
	print yanzheng(randnum())  #���һ������֤