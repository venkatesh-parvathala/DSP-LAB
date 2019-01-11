import numpy as np
print("Enter the matrix as shown:[[1,2,3],[4,5,6],[7,8,9]]")
a=input("Enter your Matrix:")
rev=np.linalg.inv(a)
print("The inverse of the matrix is:\n")
print rev
