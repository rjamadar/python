# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 16:59:27 2020

@author: Russell
"""

firstNumber = float (input("Enter a number: ")) #prompt for first number

secondNumber = float (input("Enter a number: ")) #prompt for second number

thirdNumber = float (input("Enter a number: ")) #prompt for third number
print() #empty line

if firstNumber > secondNumber and secondNumber > thirdNumber : #checking condition 1
    print("The largest number is: %.1f" %firstNumber)
    
elif secondNumber > firstNumber and secondNumber > thirdNumber : #checking condition 2
    print("The largest number is: %.1f" %secondNumber)
    
else: # printing thirdNumber as largest if upper two condition does not meet.
    print("The largest number is: %.1f" %thirdNumber)