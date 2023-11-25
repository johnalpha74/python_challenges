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

countries_i_love.remove('Canada')
for country_names in countries_i_love:
    print(country_names, end=', ')

#insert a new line character
print("\n")

#sort countries alphabetically
countries_i_love.sort()
for sortedout in countries_i_love:
    print(sortedout, end=', ')

#insert a new line character
print("\n")

#reverse the list
countries_i_love.reverse()
for reversed in countries_i_love:
    print(reversed, end=", ")

#insert a new line character
print("\n")

#remove an item
countries_i_love.pop(0)
for reversed in countries_i_love:
    print(reversed, end=", ")

