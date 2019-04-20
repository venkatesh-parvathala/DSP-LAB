import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
fs,data=wav.read('myspeech.wav')
fs=np.float(fs)
#fs2=2*fs
#n=data.shape[0]
#d=500
#atam=np.zeros((n+d,2))
#print (n,data,shape)
#datam[0:n,0]=data[:,0]
#datam[d:n+d,1]=data[:,1]
print(fs,data,len(data))
t=np.arange(0,len(data)/fs,1/fs)
#t2=np.arange(0,len(data)/fs2,1/fs2)
#plt.subplot(211)
plt.plot(t,data)
#plt.subplot(212)
#plt.plot(t2,data)
wav.write('new_myvoice.wav',2*fs,data)
plt.show()
#datam=np.asarray(datam,dtype='int16')
#wav.write('mynewvoice.wav',fs,datam)
"""a1=plt.subplot(211)
a1.plot(datam[:,0])
plt.subplot(212,sharex=a1)
plt.plot(datam[:1])
plt.show()"""

