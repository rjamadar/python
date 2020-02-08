# -*- coding: utf-8 -*-
"""
Lab 2
Created on Wed Jan 15 15:57:09 2020

@author: Russell
"""


#In class practice 1: assign variables, do simple calculations, and print them 
#outTask: Write a program that displays the volume of two six-packs of cans and
#the total volume of the six-pack and four two-liter bottles. (note: assign the 
#volume of one can (0.355) and the volume of one two-litter 
#bottle (2) as the constant)
ONE_CAN=0.355
TWO_LITERS=2

print("Two six-packs of 12-ounce cans contains", 2*6*ONE_CAN, "liters")
print("A six-pack and a two-liter bottle contain", 
      6*ONE_CAN+TWO_LITERS, "liters")


#In class practice 2: get familiar with basic arithmetic operations and some 
#specific characteristic Task 2.1: Write a program tocreate a new variable 
#called basic_arti with the value of 2034 and do the following calculations 
#using division related operations.
#1: the reminder of 2034/10
#2: the reminder of 2034/100
#3: the reminder of 2034/1000
#4: the floating value of 2034/10
#5: floor division of 2034/10
#(note: division (/); floor division (//); reminder (%))
print("the reminder of 2034/10 is:", 2034%10)



#Task 2.2: Write a program to create a variable called pennies with the value 
#of 1829, apply for some calculations, and display the following output. 
pennies = 1829
dollars = pennies//100  #floor division
cents=pennies%100       #reminder division

print("I have", dollars, "dollars and", cents,"cents")


#Task 2.3: Leverage some special characteristics in Python to finish the 
#following tasks. 
#1: repeat “-“ 50 times 
#2: repeat “War Eagle” 20 times 
#3: include a “ “ in your display 
#4: display “Hello” “Super Bowl” in two lines

#Note: 
#    - string repetition: *
#    - print out “ “ in a string: \ \
#    - output a newline: \n
war="WarEagle "*20
print(war)

print("Hello\nSuper Bowl")
#In class practice 3: index practice and use input() function 
#Task 3.1: Leverage the index system in Python to extract the element from your
# Create two variables called first_name and last_name and assign your own 
# first and last name to these variables respectively. Then, display the initial 
# of your name and also display the last words of your first_name and last_name. 

first_name = "Russell"
last_name = "Jamadar"

initial = first_name[0] + last_name[0]
print('My Initial is:',initial)
last_word=first_name[6]+last_name[6]
print("Last two letters are:"last_word)

#Task 3.2: Use the input() function to answer “Who will be the champion of the 
#Super Bowl this year?” And then display the first three letters of your answer. 


