# Python Practice Warmup Exercises
# --------------------------------
#
# 1) Create 2 variables. Swap them and print their values.
#
# 2) Write an if statement that compares two numbers and prints the larger
#
# 3) Write an if statement that compares two strings and prints the string with larger length
#
# 4) Write a for loop that prints the evens numbers from 1-100
#
# 5) Rewrite the for loop using a while loop
#
# 6) Create a loop that prints the following pattern:
#
# * * *
# * * *
# * * *
#
# HINT: Think nested loops.
#
# 7) Create a list that with 10 numbers. Loop through the list and sum them
#
# 8) Create a dictionary that contains a shopping cart of 5 items.
#
# 9) Create a string which holds the name of your city as the residence
#
# 10) Create a function named 'summation' that accepts an arbitrary number of arguments and prints the summation of all the values.



print("#1")
a = "hello"
b = "world"
print(a,b)
a,b = b,a
print(a,b)
print("---")


print("#2")
num1 = 2
num2 = 3
print("---")

if num1 > num2:
    print("larger number is:  {}".format(num1))
else:
    print("larger number is:  {}".format(num2))
print("---")


print("#3")
string1 = "string"
string2 = "longer string"
if len(string1) > len(string2):
    print("longer string:  {}".format(string1))
else:
    print("longest string:  {}".format(string2))
print("---")


print("#4")
for i in range(2,100,2):
    print(i)
print("---")


print("#5")
i = 2
while i < 100:
    print(i)
    i += 2
print("---")


print("#6")
for x in range(3):
    print("***")
print("---")


print("#7")
