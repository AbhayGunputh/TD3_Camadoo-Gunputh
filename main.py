#!/bin/bash/env pyhon3
number1 = []
number2 = []
def mul(a,b):
	result = a*b
	return result
def inputnum():
	first = int(input("Enter the first number : "))
	sec = int(input("Enter the second number : "))
	num1 = number1.append(first)
	num2 = number2.append(sec)
	
def main():
	while True:
		try:
			inputnum()
			print(mul(number1[0],number2[0]))
			break
		except:
			print("You have enter more than one number or 0 number")


check = str(raw_input("Do you want to multiply 2 integers ? (Y/N): ")).lower().strip()
try:
        if check[0] == 'y':
            print("-----MULTIPLICATION OF 2 NUMBERS-----")
  	    main()
        else:
            print("Bye")
except Exception as error:
        print("Please enter valid inputs")
