colors = ["red", "blue", "black",34]
chocolates = ["5 Star","Munch","fruit and nut"]
numbers = [1,2,3,4,5]
chocolates.sort
numbers.sort


[print(x) for x in chocolates]

newlist = [x for x in chocolates if x =="fruit and nut"]
print(newlist)
 



# colors.insert(2,"dark chocolate")
# colors.append("dairy milk")
# colors.pop
# print(colors)
# for x in range(len(chocolates)):
#     print(chocolates[x])
# while x < len(chocolates):
#     print(chocolates[x])
#     x+=1

#1. list can contain multiple type of data.....it can be int.. it is a type of heterogenous ["Shaily", "dangerous"]
#list are ordered..... append adds to the end of the list ..list allows dupliacate values...
# list are mutable=we can make changes  to the values in the list 
#Tuple and list are very similar but tuples are imutable.
# #Imutable= cannot make any changes to the values in the tuple. 
# insert is used to add an item to the position 
# append is used to add an item to the end of the list
# extend list by adding the given list
# remove is used to remove an item from the list 
# pop is used to remove an item to the specified position 
# delete  is used to delete the item at specified index 
# clear...clears the list 
# HENCE THANK YOU  