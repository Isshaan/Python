print('Welcome to the Common Factors Calculator')
x=int(input('Please enter the first Integer\n'))
y=int(input('Please enter the second Integer\n'))
i=1
j=0
a=x
b=y
Numbers=[]
if x<0 :
    x=-x
if y<0 :
    y=-y
while i<x :
  if x%i==0 :
      if y%i==0 :
          j=j+1
          Numbers.append(i)
  i=i+1
print('The numbers',a,'&',b,'are divisible by',len(Numbers),'common Integers')
print('The common integers are',Numbers)
