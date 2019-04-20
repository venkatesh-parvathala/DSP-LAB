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
x=input("Enter the signal X:")
y=input("Enter the signal Y:")
r=time_rev(y)
print ("The time reversal is")
print r
Rx_y=conv(x,r)
print("The cross corelation=")
print Rx_y 
plt.subplot(411)
plt.title("The signal X")
plt.stem(x)
plt.subplot(412)
plt.title("The signal Y")
plt.stem(y)
plt.subplot(413)
plt.title("The Time reversal of Y")
plt.stem(r)
plt.subplot(414)
plt.title("The crosscorrelation of X and Y")
plt.stem(Rx_y)
plt.show()
