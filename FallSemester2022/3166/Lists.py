# Building a list
mylist = []
# Append will append the index of the list
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])

#will print out 1,2,3
for x in mylist:
    print(x)
    
# Accessing an index which does not exist generates an exception (error)
# mylist = [1,2,3]
# print(mylist[10])

#Exercise
numbers = ["1","2","3"]
strings = ["hello", "world"]
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]

# code should write out the filled arrays and the second name
# in the names in the list (Eric)

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)