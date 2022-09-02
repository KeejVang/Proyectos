# Python uses C-style string formatting to create new,
# formatted strings. The % operator is used to format a set
# of variables enclosed in a "tuple" (a fixed size list)
# together with a format string, which contains normal text
# together with "arguement specifiers", special symbols like 
# "%s" and "%d"

#This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

# To use two or more arguement specifiers, use a tuple(parenthesis)

# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

# Any object which is not a string can be formatted using
# the %s operator as well.
# The string which returns from the "repr" method of that object
# is formatted as the string. For example:

#This prints out: A list: [1, 2, 3]
mylist=[1,2,3]
print("A list: %s" % mylist)

# Basic arguement specifiers:
# %s - String or anything with string representation
# %d - integers
# %f - floating point numbers
# %.<number of digits>f - floating point numbers with a fixed
# amount of digits to the right of the dot
# %x/%X - Integers in hex representation (lowercase/uppercase)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%d"
print(format_string % data)