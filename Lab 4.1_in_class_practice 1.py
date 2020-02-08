## Lab 4.1 in class practice 1
#  This program computes the time required to double an investment.
#

# Create constant variables.

RATE = 0.06 # interest rate is constant 
INITIAL_BALANCE = float(input("What is your initial investment?"))
TARGET = 3 * INITIAL_BALANCE # TARGET is constant as well 
      
# Initialize variables used with the loop.
balance = INITIAL_BALANCE
year = 0

# Count the years required for the investment to double.
while balance < TARGET :  # the statement under the while loop will be executed only if "balance < TARGET is true"
   interest = balance * RATE  
   balance = balance + interest
   year = year + 1

# Print the results.   
print("The investment tripled after", year, "years.")




