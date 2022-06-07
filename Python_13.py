x=int(input('Please enter the number of Elements in the Arithmetic Sequence. \n'))
List=[]
b=x
i=1
while x>0 :
    print('Please Enter value number',i,'in the list.')
    a=int(input())
    List.append(a)
    i=i+1
    x=x-1
print('The entered Sequence is',List)
if(List[1]-List[0]==List[2]-List[1]) :
    Difference = List[1]-List[0]
elif(List[2]-List[1]==List[3]-List[2]) :
    Difference = List[2]-List[1]
else :
    Difference = (List[3]-List[0])/3
m=List[0]
for j in range(1,b) :
    if (m+Difference==List[j]) :
        m=m+Difference    
    else :
        print(List[j], 'is a Wrong Term for Airthmetic Sequence.')
        break
