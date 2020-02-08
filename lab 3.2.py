# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:23:49 2020

@author: Russell
"""

#read the number from user input

userInput = float(input("Enter a number:"))

#nested condition


if userInput == 0.0 :
    print("zero")
else :
    #display positive or negative
    if userInput > 0:
        print("positive")
    else :
        print("negative")
        
        #display the absolute
    if abs(userInput) > 1000000:
            print("Its a large number")
    elif abs(userInput < 1) :
            print("Its a small number")
    else: 
            print("Not too big or not too small")