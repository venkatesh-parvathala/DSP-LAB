import matplotlib.pyplot as plt
import numpy as np
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
x=input("Enter the signal X:")
h=input("Enter the signal H:")
y=conv(x,h)
print ("The convolution=")
print y
r=time_rev(x)
print ("The time reversal=")
print r
plt.subplot(411)
plt.stem(x)
plt.subplot(412)
plt.stem(h)
plt.subplot(413)
plt.stem(y)
plt.subplot(414)
plt.stem(r)
plt.show()

