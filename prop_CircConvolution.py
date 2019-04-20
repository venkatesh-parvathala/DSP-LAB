import matplotlib.pyplot as plt
import numpy as np
import cmath as cm
j=cm.sqrt(-1)
def reverse(x):
	m=len(x)
	b=np.zeros(m)
	b[0]=x[0]
	for k in range(1,m,1):
		b[k]=x[m-k]
	return b	
def dft(x):
	N=len(x)
	Y=[]
	for k in range(0,N,1):
		sum=0
		for i in range(0,N,1):
			sum=sum+(x[i]*(np.exp(-2*j*np.pi*k*i/N)))
		Y.append(sum)
	return Y
def conv(x1,x2):
	n1=len(x1)
	n2=len(x2)
	x3=[]
	if(n1!=n2):
		if(n1>n2):
			k=n1-n2
			np.pad(n2,(0,k),'constant')
		elif(n1<n2):
			k=n2-n1
			np.pad(n1,(0,k),'constant')
	print x1
	print x2	
	x2=reverse(x2)
	for n in range(0,n1,1):
		sum=0
		for l in range(0,n1,1):
			if(n-l>0):
				sum=sum+x1[l]*x2[n-l]
		x3.append(sum)
	return x3
"""def conv(x,h):
	n=np.size(x)
	y=np.zeros(n)
	for i in range(0,n,1):
		for k in range(0,n,1):
				y[(i+k)%n]=y[(i+k)%n]+(h[i]*x[k])
	return y"""
x1=[1,2,3,4,5,6,7]
x2=[1,2,3,4,5]
x3=conv(x1,x2)
print x3

