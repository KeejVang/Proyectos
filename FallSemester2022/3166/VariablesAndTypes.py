#Variables and Types 

# (Numbers)
# Integers (whole numbers))
myint = 7
print(myint)

# Floating point numbers (decimals)
# Two types of notations

# Notation 1
myfloat = 7.1
print(myfloat)
# Notation 2
myfloat = float(7)
print(myfloat)

# Strings
# Can be defined with single or double quotes -> '' or ""
mystring ='hello'
print(mystring)
mystring = "Hello"
print(mystring)

# Double Strings make it easy to include apostraphes
mystring = "Don't worry about apostrophes"
print(mystring)

# Simple Operations can be executed on numbers and strings
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
hellowworld = hello + " " + world
print(hellowworld)

#Assignments can be done on more than one variable 
# "simultaneously" on the same line:
a, b = 3, 4
print(a, b)

#Mixing operators between numbers and strings are not supported
# one = 1
# two = 2
# hello = "hello"
# print(one + two + hello)

#Exercise
# The target of this exercise is to create a string, an integer, and a floating point number. 
# The string should be named mystring and should contain the word "hello".
# The floating point number should be named myfloat and should contain the number 10.0,
# and the integer should be named myint and should contain the number 20.

mystring = "hello"
myfloat = 10.0
myint = 20

#test code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %F" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)