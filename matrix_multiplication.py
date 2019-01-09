def mul_mat(a,b):
	f={}
	for i in range(0,m1,1):
		for j in range(0,n2,1):
			f[i,j]=0
	for i in range(0,m1,1):
		for j in range(0,n2,1):
			for k in range(0,n1,1):
				f[i,j]=f[i,j]+(a[i,k]*b[k,j])
	return f
a={}
b={}
print("Note:The columns of the first matrix should match the rows of the second matrix")
print("Enter the rows and columns of a first matrix")
m1=input("Rows:")
n1=input("Columns:")
print("Enter the values into the first matrix")
for i in range(0,m1,1):
	for j in range(0,n1,1):
		a[i,j]=input("")
print("Enter the rows and columns of a second matrix")
m2=input("Rows:")
n2=input("Columns:")
if(n1==m2):
	print("Enter the values into the second matrix")
	for i in range(0,m2,1):
		for j in range(0,n2,1):
			b[i,j]=input("")
	res=mul_mat(a,b)
	print (res)
else:
	print("Invalid attempt...Can't multiply these matrices")
