import numpy as np
#this is the starting
m=[]
n=[]
k=[]
j=[]
x=[m,n]
y=[k,j]
n=int(input("the value of N"))
for i in range(n):
    f=int(input("enter number"))
    x.append(f)
for z in range(n):
    e=int(input("enter number"))
    y.append(e)
a=np.array([x])
b=np.array([y])
print(a,b)