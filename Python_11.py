List=[1,2,3,4,60,6,7,8,9,10]
y=List[0]
for x in List:
    if y>x:
      continue
    else:
      y=x
print('The greatest number in the List is', y)
