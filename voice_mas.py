import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
p=input("Enter the order of the Moving Average System:")
fs,data=wav.read('myspeech.wav')
print(fs,data)
l=len(data)
fs=np.float(fs)
t=np.arange(0,l/fs,1/fs)
v=np.random.rand(l)
x=v+data
sum=0
for i in range(0,l,1):
	for k in range(0,p-1,1):
		sum=sum+x[i-k]
	print sum	
	y[i]=float((sum)/(p))
	sum=0
print y
plt.subplot(411)
plt.plot(t,data)
plt.subplot(412)
plt.plot(t,v)
plt.subplot(413)
plt.plot(t,x)
plt.subplot(414)
plt.plot(t,y)
plt.show()	
