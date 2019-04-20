import numpy as np
import matplotlib.pyplot as plt
p=input("Enter the order of the Moving Average System:")
Fs=4000
f1=30
#f2=400
y=np.zeros(400)
#t=np.linspace(0,20,20)
t= np.linspace(0,800,400)
u=np.sin(2*np.pi*f1*t/Fs)
#v=np.sin(2*np.pi*f2*t/Fs)
v=np.random.rand(400)
#x=[0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]
x=u+v
sum=0
for i in range(0,400,1):
	for k in range(0,p-1,1):
		sum=sum+x[i-k]
	print sum	
	y[i]=float((sum)/(p))
	sum=0
print y
plt.subplot(411)
plt.plot(t,u)
plt.subplot(412)
plt.plot(t,v)
plt.subplot(413)
plt.plot(t,x)
plt.subplot(414)
plt.plot(t,y)
plt.show()	
