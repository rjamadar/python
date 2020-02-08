# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:34:14 2020

@author: Russell
"""

userInput = input("Type something:")

#checking for letters

if userInput.isalpha() :
    print("The input only contains letters")
    
if userInput.isupper() :
    print("The input contains only upper case")

if userInput.islower() :
     print("The input contains only lower case")

if userInput.isdigit() :
    print("The input contains only digits")

if userInput.endswith(".") :
     print("The input ends with period")