# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 16:36:30 2020

@author: Russell
"""

initialBalance = float(input("Initial balance: ")) #prompt for initial balance

yearlyRate = float(input("Annual interest rate in percent: ")) # prompt for interest rate

interestRate = (yearlyRate/100) / 12 # calculating yearly interest rate to month

firstMonth = initialBalance + (initialBalance * interestRate) #calculating first month's balance

secondMonth = firstMonth + (firstMonth * interestRate) #calculating second month's balance

thirdMonth = secondMonth + (secondMonth * interestRate) #calculating third month's balance

#printing first three months balance in float with 3 decimal places.

print("After fist month: %.3f" %firstMonth)

print("After second month: %.3f" %secondMonth)

print("After third month: %.3f" %thirdMonth)


