numbers=[1,2,3,4,5,6,7,8,9]
flag=False
newlist=[]
for x in numbers:
    if x!=2:
        newlist.append(x)
    elif x==2 and flag==False:
        newlist.append(x*100)
        flag=True
    elif x==2 and flag==True:
        newlist.append(x)
print(newlist)