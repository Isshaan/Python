x=int(input('Enter the number of Values in the List\n'))
if x<0:
    print('Please Enter a Positive Integer')
List=[]
i=0
while x>0 :
    print('Please Enter value number', i+1)
    value=int(input())
    List.append(value)
    i=i+1
    x=x-1
y=List[0]
for j in List:
    if y>j:
        continue
    else:
        y=j
print('The greatest number from your entered list is', y)
