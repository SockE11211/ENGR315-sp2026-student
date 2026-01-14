"""
A simple while loop example of how to calculate compounding interest
"""

# initial bank deposit
balance = 1000

# interest rate (as a fraction) of 2.3%
rate = 0.023

# years to compound interest
years = 10

counter=0
while counter<years:
    balance = balance * (1+rate)
    counter=counter+1

    print('End of Year ',counter, ' balance is ', balance)

    