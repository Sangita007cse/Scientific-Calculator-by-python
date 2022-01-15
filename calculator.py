"""
Please select operation - 
1. Add
2. Subtraction
3. Multiplication
4. dividision
5. modulo 
6. sin 
7. cos
8. tan 
9. power
10. sqrt
11. log
12. prime
13. e^
14. 

"""

from math import *


def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def modulo(x,y):
    return x%y

def power(x,y):
    return x**y

def squareroot(x):
    return sqrt(x)

def primenum():
    x = int(input("Enter 1st number: "))
    y = int(input("Enter 2nd number: "))
    sum =0
    for num in range(x,y+1):
        count = 0
        for i in range(2,(num//2+1)):
            if((num%i) == 0):
                count = count +1
                break
        if (count == 0 and num != 1):
            sum += num
    print("Sum of all prime numbers between", x ,"and", y, ":", sum)

def sinfunc(x):
    rad = (pi/180)*x
    return sin(rad)


def cosfunc(x):
    rad = (pi/180)*x
    return cos(rad)


def tanfunc(x):
    rad = (pi/180)*x
    return tan(rad)

def logfunc(x):
    return log10(x)

def exponential(x):
    return e**x

print("Please Select operation : ")
print("1. Add")
print("2. Subtraction")
print("3. Multiplication")
print("4. dividision")
print("5. modulo ")
print("6. power ")
print("7. squareroot ")
print("8. prime number ")
print("9. sin ")
print("10. cos ")
print("11. tan ")
print("12. log ")
print("13. exponential ")

select = int(input("select input between 1 to 13 -> "))

if select == 1 :
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1, "+", num2, "=", add(num1,num2))
elif select == 2 :
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1, "-", num2, "=", subtract(num1,num2))
elif select == 3 :
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1, "*", num2, "=", multiply(num1,num2))
elif select == 4 :
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1, "/", num2, "=", divide(num1,num2))
elif select == 5 :
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1, "%", num2, "=", modulo(num1,num2))
elif select == 6 :
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1, "^", num2, "=", power(num1,num2))
elif select == 7 :
    num1 = int(input("Enter first number: "))
    print(num1, "=", sqrt(num1))
elif select == 8 :
    primenum()
elif select == 9 :
    num1 = int(input("Enter degree: "))
    print("sin of ", num1 , "is", sinfunc(num1))
elif select == 10 :
    num1 = int(input("Enter degree: "))
    print("cos of ", num1 , "is", cosfunc(num1))
elif select == 11 :
    num1 = int(input("Enter degree: "))
    print("tan of ", num1 , "is", tanfunc(num1))
elif select == 12 :
    num1 = int(input("Enter the number: "))
    print("log base 10 of", num1, logfunc(num1))
elif select == 13 :
    num1 = int(input("Enter the number: "))
    print("exponential of", num1, exponential(num1))