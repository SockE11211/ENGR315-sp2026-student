# this exercise is on break and continue - two statements
# used in loops that alter its flow.

# a break statement stops and exits the loop
# when a certain condition is identified.
# an example is given below:
numbers = [5, 10, 17, 3, 6]
total = None
for number in numbers:
    if total is None:
        total = 0
    if number > 10:
        print ("too big!")
        break
    total = total + number

print("Total of numbers: " + str(total))
# notice how the total only involves the 5 and 15,
# and does not include the rest of the numbers

# a continue statement restarts the loop if the condition
# is fulfilled

n = 0 # an iterator
while n < 10:
    n = n + 1
    if n == 7:
        print("7 is a lucky number!")
        continue

    if n == 9:
        print(str(n) + "!")
        print("That's almost the last number!")
        continue
    print("Number: " + str(n))

# in this example, the numbers 7 and 9 are selected specially,
# and are not printed in the loop with the "Number: "


# To try using break on your own, write a break in a for loop
# that comes after the print statement and
# detects if the word "hit" is in the list, and sets the
# variable "violence" to true

colors = ["blue", "green", "red", "hit", "orange"]
violence = None
for color in colors:
    print(color)

# to use continue, write a for loop that adds up only even numbers.
# you can detect even numbers by detecting if x % 2 == 0,
# where x is the variable.

adds = [1,2,3,4,5,6]
total_adds = 0
for x in adds:
    if total_adds is None:
        total_adds = 0

    total_adds = total_adds + x

print(total_adds)

# this for loop adds each element of "stuff" to the new list
# "new_stuff".
# However, add if statements to the list to change its function.
# Use continue if a word is ever detected, and
# use break to stop adding numbers if the number 10 is found.
# Use isinstance(things, str) to determine if something is a word.
# example:
# if isinstance(things, str):

stuff = ["red", 5, "blue", 7, 9, "orange", 30, 5, 5, 5]
new_stuff = []
for things in stuff:
    new_stuff.append(things)

print(new_stuff)

