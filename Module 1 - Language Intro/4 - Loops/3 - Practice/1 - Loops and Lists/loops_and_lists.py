# this will test your ability to write a for loop
# use the print() statement to determine whether your number is correct

# an example for loop is given below
list = [5, 10, 15, 20]
for multiple in list:
    print("A multiple of 5 is " + str(multiple))

# instead of using a counter like while loops,
# for loops initialize a variable in their condition, and that
# variable is used in the rest of the loop.
# for example, the variable "multiple" in the above loop is initialized,
# and then used in the list to identify each integer

# first, write the body of a for loop that tells how many
# entries are in a loop.
# hint: create an incrementer inside of the for loop
words = ["cat", "hat", "bat", "rat"]
increment = 0
for word in words:
    increment = 0

# now, write your own for loop that
# adds up the contents of a given list in a variable "total".
# hint: you will need to add "num" to "total"
numbers = [4, 9, 26, 3]
total = 0