import matplotlib.pyplot as plt
import numpy as np
F=input("Frequency of Signal:")
fs=input("Sampling frequency:")
n=np.arange(0,2000,1)
t=np.arange(0,2000,50)
x=np.sin(2* np.pi *F*n/fs)
plt.subplot(211)
plt.plot(n,x,'b')
x=np.sin(2* np.pi *F*t/fs)
plt.subplot(212)
plt.stem(t,x)
plt.show()
