import matplotlib.pyplot as plt
import numpy as np
import cmath as cm
j=cm.sqrt(-1)
def dft(x):
	N=len(x)
	Y=[]
	for k in range(0,N,1):
		sum=0
		for i in range(0,N,1):
			sum=sum+(x[i]*(np.exp(-2*j*np.pi*k*i/N)))
		Y.append(sum)
	return Y
n=np.linspace(-200,200,400)
x1=np.cos(2*np.pi*n*50/2000)
#x1=[1,2,3,4,5]
y1=dft(x1)
x2=np.cos(2*np.pi*n*100/2000)
x3=x1*x2
y2=dft(x3)
plt.subplot(411)
plt.plot(x1)
plt.subplot(412)
plt.plot(y1)
plt.subplot(413)
plt.plot(x2)
plt.subplot(414)
plt.plot(y2)
plt.show()
