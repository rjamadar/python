# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:42:03 2020

@author: Russell
"""

user = input("enter one character:")

#check and print

if len(user) == 0 or len(user) >1:
    print("ERROR: read instruction")

elif user in "AEIOUaeiou" :
    print("Its a vowel")

elif user not in "AEIOUaeiou" :
    print("its a consonant")
    
else: 
    print("neither case")