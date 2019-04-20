import numpy as np
import matplotlib.pyplot as plt
Fs=4000
f=10
y=np.zeros(20)
t= np.linspace(0,400,20)
x=np.sin(2*np.pi*f*t/Fs)
print x
y[0]=x[0]
for i in range(1,20,1):
	y[i]=y[i-1]+x[i]
print y
v=np.linspace(0,20,20)
plt.subplot(211)
plt.stem(v,x)
plt.subplot(212)
plt.stem(v,y)
plt.show()

