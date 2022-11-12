print("Simple Calaculator Python Program")
c=int(input("Enter 1 for Addition\nEnter 2 for Subtraction\nEnter 3 for Multiplication\nEnter 4 for Division\nEnter Your Choice : "))
a=int(input("enter first number: "))
b=int(input("enter second number: "))
def simplecalc(x,y,z):
    if z==1:
        print("the sum is:", x+y)
    elif z==2:
        print("the sub is:",x-y)
    elif z==3:
        print("the product is:",x*y)
    elif z==4:
        print("the divion is:",x/y)
    else:
        print("enter any number")
simplecalc(a,b,c)

