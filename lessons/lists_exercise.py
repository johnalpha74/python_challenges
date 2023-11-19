#Python knows a number of compound data types, used to group together other values.
# The most versatile is the list, which can be written as a list of comma-separated values (items)
# between square brackets. Lists might contain items of different types, but usually the items all
# have the same type.

fruits = ['apples', 'oranges', 'banana', 'pear', 'grapes', 'mango']
squares = [1, 4, 9, 16, 25]

# Like strings (and all other built-in sequence types), lists can be indexed and sliced
print(fruits[3] + " " + fruits[0])

#Slicing indices creates a new list
my_fruits = fruits[0:2]
print(my_fruits[0] + " " + my_fruits[1])

# Lists also support operations like concatenation
added_fruits = my_fruits + ['peaches', 'appricot']
print(added_fruits)
