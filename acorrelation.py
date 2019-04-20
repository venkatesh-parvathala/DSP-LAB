import numpy as np
import matplotlib.pyplot as plt
def conv(x,h):
	n=np.size(x)
	m=np.size(h)
	y=np.zeros(m+n-1)
	for i in range(0,m,1):
		for k in range(0,n,1):
				y[i+k]=y[i+k]+(h[i]*x[k])
	return y
def time_rev(x):
	n=np.size(x)
	r=np.zeros(n)
	for i in range(0,n,1):
		r[n-i-1]=x[i]
	return r
n=np.arange(500)			
x=np.sin(2*np.pi*20*n/4000)
l=len(x)
t1_rev=time_rev(x)
Rxx=conv(x,t1_rev)
N=np.random.rand(l)
x_n=x+N
t2_rev=time_rev(x_n)
Rxn_xn=conv(x_n,t2_rev)
a1=plt.subplot(511)
a1.plot(x)
plt.subplot(512,sharex=a1)
plt.plot(N)
plt.subplot(513,sharex=a1)
plt.plot(x_n)
plt.subplot(514,sharex=a1)
plt.plot(Rxx)
plt.subplot(515,sharex=a1)
plt.plot(Rxn_xn)
plt.show() 	
