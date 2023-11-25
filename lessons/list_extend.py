#Extend the list by appending all the items from the iterable using list.extend(iterable)
#Create two lists with baby names for girls and boys respectively
girls_baby_names = ['Kayleigh', 'Kayla', 'Natasha', 'Nicole']
boys_baby_names = ['Kayden', 'Kunaka', 'Junior', 'Munashe']

#Print names in the two lists separately
for names in girls_baby_names:
    print(names, end=' ')

#Put new line after the list
print("\n")

for names in boys_baby_names:
    print(names, end=" ")

#Put new line after the list
print("\n")
#Extend the gils list with the boys list
girls_baby_names.extend(boys_baby_names)


#Display the names that were added
#print(f"The girls names are")
for names in girls_baby_names:
    print( names, end=' ')
