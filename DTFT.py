import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
j=cm.sqrt(-1)
n=np.linspace(-200,200,400)
x=np.sin(2*np.pi*10/50*n)
N=len(x)
w=np.linspace(-np.pi,np.pi,1000)
X=[]
Y=[]
Z=[]
for i in range(0,1000,1):
	sum=0
	for k in range(0,N,1):
		sum=sum+(x[k]*(cm.exp(-1*j*w[i]*k)))
	X.append(sum)
	Y.append(np.abs(sum))
	Z.append(np.angle(sum))
plt.subplot(411)
plt.plot(x)
a1=plt.subplot(412)
a1.plot(w,X)
plt.subplot(413,sharex=a1)
plt.plot(w,Y)
plt.subplot(414,sharex=a1)
plt.plot(w,Z)
plt.show()
