#Python knows a number of compound data types, used to group together other values.
# The most versatile is the list, which can be written as a list of comma-separated values (items)
# between square brackets. Lists might contain items of different types, but usually the items all
# have the same type.

fruits = ['apples', 'oranges', 'banana', 'tomatoes', 'pear', 'grapes', 'mango']
squares = [1, 4, 9, 16, 25]

# Like strings (and all other built-in sequence types), lists can be indexed and sliced
print(fruits[3] + " " + fruits[0])

#Slicing indices creates a new list
my_fruits = fruits[0:2]
print(my_fruits[0] + " " + my_fruits[1] + "\n")

# Lists also support operations like concatenation
added_fruits = my_fruits + ['peaches', 'appricot']
print(f"added_fruits + \n")

#Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their conten
print(f"Original list is {fruits} + \n")
fruits[3] = 'Strawberry'
print(f"New modified list is{ fruits} + \n")

#New items can be added at the end of the list, by using the list.append() method
fruits.append('avocado')
print(f"Appended fruit list is {fruits} \n")

#Assignment to slices is also possible, and this can even change the size of the list or clear it entirely
cities = ['Quebec', 'Ottawa', 'Toronto', 'Victoria BC', 'Edmonton']
print(f"The listed cities are: {cities} \n")


