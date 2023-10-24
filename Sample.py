# Design apython program to generate and print a list except for the first five elements , where the values are the squares of numbers between 1 and 30.

# def printvalues():
#     li=[]
#     for i in range(1,31):
#         c=i**2
#         li.append(c)
#     print(li[1:10:2])
# printvalues()


# Design a Python Program to understand the working of loops.

# for loop
# n=int(input("enter the number:"))
# for i in range(1,11):
#     c=i*n
#     print(n,"x",i,"=",c)
    
# while loop
# n=int(input("enter the number:"))
# i=0
# while(i<=10):
#     c=n*i
#     print(n,"x",i,"=",c)
#     i+=1


# Design a pyhton function to find the maximum of the three numbers.

# def maxvalue():
#     a=int(input("enter the first number :"))
#     b=int(input("enter the second number :"))
#     c=int(input("enter the third number :"))
#     if(a>=b and a>=c):
#         print("maximum number is :",a)
#     elif(b>a and b>=c):
#         print("maximum number is :",b)
#     else:
#         print("the maximum number is :",c)
# maxvalue()


# Design a python program for creating a random story generator.

# import random
# sentence_starter=["About hundred years ago ,","In the 20 BC ,","Once upon a time ,"]
# character=[" there lived a king ,"," there was a man named jack ,"," there lived a farmer ,"]
# time=[" one day"," one full moon night"]
# story_plot=[" he was passing by"," he was going for a picnic to"]
# place=[" the mountain , "," the garden , "]
# second_character=["he saw a man ","he saw a lady "]
# age =["who seems to be in late 20s ","who seems very old and feeble "]
# work=["searching something.","digging a well on roadside."]
# print(random.choice(sentence_starter)+random.choice(character)+random.choice(time)+random.choice(story_plot)+random.choice(place)+random.choice(second_character)+random.choice(age)+random.choice(work))


# Design a python program using Numpy library function.

import numpy as np