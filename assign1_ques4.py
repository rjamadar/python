# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 17:55:14 2020

@author: Russell
"""

name = str (input("Enter employee name: ")) #prompt for name
rate = float(input("Enter the hourly rate: ")) #prompt for hourly rate
totalHours = float(input("Enter the number of hours worked: ")) # prompt for hours

#if worked over time 

if totalHours > 40 :
    overTime = totalHours - 40 # over time is total hours worked minus 40
    BASE_HOURS = 40 * rate # base hourly pay
    OVER_TIME = overTime * rate * 1.5 # over time hourly pay
    pay = BASE_HOURS + OVER_TIME # total pay = 40 hours pay + over time pay
    
    print("Employee: ", name) # printing employee name

    #printing total pay with hours worked
    print("The pay will be %.2f for %.1f hours of work." %(pay, totalHours))
  
# if did not work over time then
else :
    pay = totalHours * rate # hours worked time regular rate
    print("Employee: ", name) # printing employee name
    
    #printing total pay with hours worked
    print("The pay will be %.2f for %.1f hours of work." %(pay, totalHours))

