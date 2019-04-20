import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
j=cm.sqrt(-1)
n=np.linspace(-200,200,400)
x=np.sin(2*np.pi*n*10/1000)
#x=input("Enter the input:")
N=len(x)
X=[]
Y=[]
Z=[]
for k in range(0,N,1):
	sum=0
	for i in range(0,N,1):
		sum=sum+(x[i]*(np.exp(-2*j*np.pi*k*i/N)))
	X.append(sum)
	Y.append(np.abs(sum))
	Z.append(np.angle(sum))
#print X
a1=plt.subplot(411)
a1.plot(n,x)
plt.subplot(412,sharex=a1)
plt.stem(X)
plt.subplot(413,sharex=a1)
plt.stem(Y)
plt.subplot(414,sharex=a1)
plt.stem(Z)
plt.show()
