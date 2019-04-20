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
n=np.arange(0,500)
#x=input("Enter the signal x:")
x1=np.sin(2*np.pi*20*n/4000)
l=len(x1)
x2=np.random.rand(l)
x=x1+x2
a=input("Enter the order of the Moving Average System:")
h=np.zeros(a)
for i in range(0,a,1):
	h[i]=1.0/a
print h
r=conv(x,h)
plt.subplot(511)
plt.plot(x1)
plt.subplot(512)
plt.plot(x2)
plt.subplot(513)
plt.plot(x)
plt.subplot(514)
plt.stem(h)
plt.subplot(515)
plt.plot(r)
plt.show()
