#!/bin/bash/env python3

def addint(number1,number2):
    result = number1 + number2;
    return result;

num1 = float(input("Enter the first number : "))
while (num1 < 0):
        print("-----please enter positive number ONLY-----")
        num1 = float(input("Enter the first number : "))
print()
num2 = float(input("Enter the second number : "))
while(num2 < 0):
        print("-----(Please enter positive numbers ONLY-----")
        num2 = float(input("Enter the second number : "))
print (addint(num1,num2))

