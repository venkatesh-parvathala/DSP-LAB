import numpy as np
import matplotlib.pyplot as plt
import math
Dp=input("Enter the value of Dp:")
Ds=input("Enter the value of Ds:")
Wp=input("Enter the value of Wp:")
Ws=input("Enter the value of Ws:")
#Dp=0.707
#Ds=0.01
#Wp=3141.59
#Ws=6283.18
m=math.log((1/(Dp*Dp)-1)/(1/(Ds*Ds)-1))
n=math.log(Wp/Ws)
N=math.ceil(0.5*(m/n))
print N
s=math.pow((1/(Dp*Dp)-1),1/(2*N))
Wc=Wp/s
print Wc
w=np.arange(np.pi*2*2000)
x=1/(1+(w/Wc)**(2*N))**(0.5)
plt.plot(x)
plt.show()

