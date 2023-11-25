'''Insert an item at a given position. The first argument is the index of the element before which to insert,
so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).'''

#Create list of countries you want to go
countries_i_love = ['New Zealand', 'Canada', 'USA', 'Australia']

countries_i_love.insert(3, 'Canada')
print(f"The countries I love to go are: ")

#Display the names of the countries
for country_names in countries_i_love:
    print(country_names, end=', ')

#insert a new line character
print("\n")
#list.remove(x). Remove the first item from the list whose value is equal to x.
#It raises a ValueError if there is no such item.

end_of_list = len(countries_i_love)
name_to_keep = input("Enter name of country you wish to go: \n")

while i < end_of_list-1:
    if name_to_keep not in countries_i_love:

countries_i_love.remove('Canada')

