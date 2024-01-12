#Below syntax will create empty set
b = set()
print(type(b))

#adding values to empty set
b.add(4)
b.add(5)
b.add(5)
b.add((4,5,6)) #we can add tuples to sets
print(b)


# #adding values to empty set
# b.add(4)
# b.add(5)
# b.add(5)
# b.add([4,5,6]) #we cannot add list to sets since its unhashable and its contents can be changed by changing values.
# print(b)


# #adding values to empty set
# b.add(4)
# b.add(5)
# b.add(5)
# b.add({4:5}) #we cannot add dictionary to sets since its unhashable and its contents can be changed by changing values.
# print(b)

print(len(b))
b.remove(5) #removes 5 from set.
# b.remove(15) #throws error while trying to remove 15(which is not present in set)
print(b)

b.pop()
print(b) #removes random values from the set.



