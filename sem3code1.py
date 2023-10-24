# To find the greatest number among the three numbers.
x=int(input("enter first number x:"))
y=int(input("enter second number y:"))
z=int(input("enter third number z:"))
if (x>y):
    if (x>z):
        print("x is the greatest number of all")
    elif (x==z):
        print("x and z are greater than y")
    elif (z>x):
        print("z is the greatest number of all")
elif (y>x):
    if (y>z):
        print("y is the greatest number of all")
    elif (y==z):
        print("y and z are greater than x")
    elif (y<z):
        print("z is the greatest number of all")
elif (x==y):
    if (z>y):
        print("z is the greatest number of all")
    elif (y>z):
        print("x and yare greater than z")
    elif (x==z):
        print("All htree numbers are equally")
