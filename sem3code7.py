#Design the python functionto find the maximum of three numbers.

def max_value():
    a=int(input("Enter the First Number:"))
    b=int(input("Enter the Second Number:"))
    c=int(input("Enter the Third Number:"))

    if (a>=b and a>=c):
        print("Maximum Number is :",a)

    elif (b>=c and b>=a):
        print ("Maximum Number is :",b)

    else:
        print("Maximum Number is:", c)

max_value()
