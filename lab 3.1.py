# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:45:58 2020

@author: Russell
"""

originalPrice = float(input("Original Price:"))

if originalPrice < 128 : 
    discountRate = 0.91
else :
    discountRate = 0.85
    
discountedPrice = discountRate * originalPrice
print()
print("Discounted price: $%.2f" %discountedPrice)