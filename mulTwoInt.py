#!/bin/bash/env python3
def mul(number1,number2):
    multiply = number1 * number2
    return multiply


num1 = float(input("Enter the first number : " ))
while(num1 < 0):
    print("-----Enter positive number-----")
    num1 = float(input("Enter the first number : " ))
print()
num2 = float(input("Enter the second number : " ))
while (num2 < 0):
    print("-----Enter positive number-----")
    num2 = float(input("Enter the second number : " ))
print(mul(num1, num2))
