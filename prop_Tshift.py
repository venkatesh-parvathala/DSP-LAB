import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
def delay(x):
	m=len(x)
	b=np.zeros(m)
	b[0]=x[m-1]
	for k in range(0,m-1,1):
		b[k+1]=x[k]
	return b	
x=input("Enter the input signal:")
n=input("Enter the dealy Time:")
for i in range(0,n,1):
	x=delay(x)
print x
	
