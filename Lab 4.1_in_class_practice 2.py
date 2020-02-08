## Lab 4.1 in class practice 2: for loop example 
#  This program prints a table showing the growth of an investment.
#

# Define constant variables.
RATE = 0.06
INITIAL_BALANCE = 10000.0

# Obtain the number of years for the computation.
numYears = int(input("Enter number of years: "))
   
# Print the table of balances for each year.
balance = INITIAL_BALANCE
for year in range(1, numYears + 1) : # range (1,6) will print from year 1 to year 5; 6 means ending up with year 6 
   interest = balance * RATE
   balance = balance + interest
   print("Year:",year, "Balance:",balance)


