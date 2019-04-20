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
#x1=input("Enter the First Input:")
#x2=input("Enter the Second Input:")
n1=np.linspace(-200,200,400)
n2=np.linspace(-200,200,400)
x1=np.sin(2*np.pi*n1*10/100)
x2=np.sin(2*np.pi*n2*20/100)
m=len(x1)
n=len(x2)
if(m>n):
	k=m-n
	for i in range(0,k,1):
		x2.append(0)
elif(m<n):
	k=n-m
	for i in range(0,k,1):
		x1.append(0)
x=np.add(x1,x2)
#print x1
#print x2
#print x
a1=dft(x1)
#X1=np.abs(a1)
a2=dft(x2)
#X2=np.abs(a2)
x31=dft(x)
X31=np.abs(x31)
x32=np.add(a1,a2)
X32=np.abs(x32)
print ("DFT of first Signal=",a1)
print ("DFT of Second Signal=",a2)
print ("DFT of Added Signal=",X31)
print ("Added DFT Signal=",X32)
print ("The Difference is:")
s=X31-X32
print s
#plt.subplot(411)
#plt.stem(X1)
#plt.subplot(412)
#plt.stem(X2)
plt.subplot(211)
plt.stem(X31)
plt.subplot(212)
plt.stem(X32)
plt.show()
"""if(s.(all)==0):
	print("The Linearity property is verified")
else:																																																																																																																																																			
	print("The linearity property is not verified")"""

