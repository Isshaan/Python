x=int(input('Please enter the Number of Elements in the List \n'))
a=x
A=[]
for i in range(1,x+1) :
    print('Please Enter value number',i)
    b=int(input())
    A.append(b)
print('Your Entered List is',A)
for i in A :
    Product=1
    Sum=0
    for j in range(1,1+i) :
        Product=Product*j
        Sum=Sum+j
    if Product%Sum==0 :
        print('The sum of Numbers from 1 to',i,'is divisible by the Product of Numbers from 1 to',i)
    else :
        print('The sum of Numbers from 1 to',i,'is not divisible by the Product of Numbers from 1 to',i)        
