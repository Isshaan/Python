x=int(input('Please enter the number of Integers for the List \n'))
A=list()
for i in range(1,x+1):
    print('Please enter the value number', i)
    y=int(input())
    A.append(y)
print('The list entered by you is', A)
B=list()
for j in range(10000):
    z=j*j
    B.append(z)
#print(B)
C=list()
for k in range(1,x+1):
    if(A[k-1] in B) :
        C.append('Yes')
    else:
        C.append('No')
print('The results are as follows', C)
