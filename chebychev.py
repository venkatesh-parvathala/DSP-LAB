import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
import math
"""dp=input("Enter Dp:")
ds=input("Enter Ds:")
wp=input("Enter Wp:")
ws=input("Enter ws:")"""
dp=0.8
ds=0.2
wp=6283.18
ws=31415.92
k=np.ceil(wp/ws)
a=(1.0/(dp**2))-1
b=(1.0/(ds**2))-1
ep=np.sqrt(a)
N=np.ceil((np.arccosh(np.sqrt(b/a)))/(np.arccosh(ws/wp)))
print("order of the system=",N)
"""cn=(1/ep)*(np.sqrt(b))
c=np.zeros(20)
c[0]=1
c[1]=k
for i in range(2,20,1):
	c[i]=2*c[1]*c[i-1]-c[i-2]
	if(c[i]>=cn):
		break
print i"""
w=2*np.pi*np.asarray(range(10000),'float32')
Hc=[]
for w in range(1,10000,1):
	if(2*np.pi*w<wp):	
		mag=1.0/np.sqrt(1+(ep*(np.cos(N*np.arccos(2*np.pi*w/wp))))**2)
		Hc=np.append(Hc,mag)
	else:
		mag1=1.0/np.sqrt(1+(ep*(np.cosh(N*np.arccosh(2*np.pi*w/wp))))**2)
		Hc=np.append(Hc,mag1)
h=1.0/1+(ep**2*Hc**2)
plt.plot(Hc)
plt.show()
