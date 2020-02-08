# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:39:54 2020

@author: Russell
"""

#1.1: format the output position of a float number 1.2199715155151

#- shows the first two digits after the decimal
#- shows the first six digits after the decimal
#- insert 20 spaces before showing the first five digits after the decimal
#- insert 30 spaces before showing the first four digits after the decimal


a = 1.2199715155151

print("shows the first two digits after the decimal %.2f" %(a))

print("shows the first six digits after the decimal %.6f" %(a))

print("insert 20 spaces before showing the first five digits"+ 
      "after the decimal %20.5f" %(a))

print("insert 30 spaces before showing the first five digits"+ 
      "after the decimal %30.4f" %(a))


#1.2: format the output position of a string “Quality” along with an integer 
#- insert 10 spaces before a string and 5 spaces before an integer and print the result
#- insert 20 spaces for a string, insert 10 spaces for an integer, and then print the result

title = "Quality"

print("insert 10 spaces before a string and 5 spaces before an integer" +
      "and print the result %10s %5d" %(title, a))

print("insert 20 spaces before a string and 10 spaces before an integer" +
      "and print the result %20s %10d" %(title, a))


####### IN CLASS PRACTICE 2

#input() allows the users to have the  input

#define constant

PENNIES_PER_DOLLAR = 100

PENNIES_PER_QUARTER = 25

#obtain input from users

userInput = input("Enter bill values in dollars: ")

billValue = int(userInput) #converts userInput into integer

userInput = input("Enter item price in cents: ")

itemPrice = int(userInput)

#computation for change

changeDue = PENNIES_PER_DOLLAR * billValue - itemPrice

dollarCoin = changeDue // PENNIES_PER_DOLLAR

changeDue = changeDue % PENNIES_PER_DOLLAR

quarter = changeDue // PENNIES_PER_QUARTER


print("Dollar coin: %4d" % (dollarCoin))
print("Quarter coin: %4d" %(quarter))





# In class practise for EZGRAPHICS

from ezgraphics import GraphicsWindow


win = GraphicsWindow(400, 200) # width and height

canvas = win.canvas() #drawing practise starts from here

#draw on canvas

canvas.setColor("red") # choosing color
canvas.drawRect(0, 10, 200, 10) # x position, y position, width, height

#making a green square

canvas.Color("green")
canvas.drawRect(0, 30, 50, 50)


#putting a blue square inside green square
canvas.Color("blue")
canvas.drawRect(0, 50, 25, 25)

# making a circle

canvas.Color("gray")
canvas.setOutline("yellow") # setting outline for the circle
canvas.drawText(150, 80, "This is a gray circle") #x, y, text
canvas.drawOval(70, 80, 60, 60) #x,y,size, 

# wait for the user to close the window

win.wait()
































