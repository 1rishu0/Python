# Write a program to apply methametical operations
def main():
    print ("To add two numbers enter 1:")
    print ("To sub two numbers enter 2:")
    print ("To mult two numbers enter 3:")
    print ("To div two numbers enter 4:")
    print ("To exit the program 5:")
def print_line():
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
def add_num():  #function to add two numbers
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    sum= a+b
    print(sum)
def sub_num():  #function to subtract two numbers
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    sub=a-b
    print(sub)
def mult_num():  #function to multiply two numbers
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    mult= a*b
    print(mult)
def div_num():  #function to divide two numbers
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    div= a/b
    print(div)
n=True
while n==True:
    main()
    print_line()
    c=int(input("enter the number:"))
    print_line()
    if c==1:
        add_num()
        print_line()
    elif c==2:
        sub_num()
        print_line()
    elif c==3:
        mult_num()
        print_line()
    elif c==4:
        div_num()
        print_line()
    elif c==5:
        n=False
