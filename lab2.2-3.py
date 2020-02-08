# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:26:23 2020

@author: Russell
"""

tank_amount = float(input("Enter the amount of gas:"))
mpg = float(input("Enter the MPG info:"))
price = float(input("Enter the price of gas:"))

#compute

cost100 = 100 / mpg*price

distance = tank_amount * mpg

#display the results
print()#empty line
print("It takes $%.2f of fuels to drive 100 miles," %cost100)

print("The car travel,", distance, "miles with the gas in the tank")