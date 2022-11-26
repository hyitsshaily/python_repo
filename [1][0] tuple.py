tuple1=(1,[6,7],2,3,4,5)
list=list(tuple1)
list[1][0]=8
tuple1=tuple(list)
print(tuple1)