# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 17:17:38 2020

@author: Russell
"""
# displaying satisfaction level at the begining 
print("Please use the following scale: ")
print("  1: Totally satisfied")
print("  2: Satisfied")
print("  3: Dissatiesfied")

#promting for satisfaction level between 1-3
scale = float(input("What was your level of satisfaction? "))

#promting for bill amount
bill = float(input("How much was your bill? "))

if scale == 1 : # if totally satiesfied 
    tip = bill * 0.20 # tip is 20% of the bill
    print("Because you were totally satisfied, your tip " +
          "should be $%.2f." %tip)
if scale == 2 : # if satisfied
    tip = bill * 0.15 # tip is 15% of the bill
    print("Because you were satisfied, your tip " +
          "should be $%.2f." %tip)
if scale == 3 : # if dissatiesfied
    tip = bill * 0.10 #tip is 10% of the bill
    print("Because you were dissatisfied, your tip " +
          "should be $%.2f." %tip)
    
    
    
    
    