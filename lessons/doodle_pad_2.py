''' Lists in Python '''
#Create original list
cars = ['Mercedes', 'BMW', 'Jaguar', 'Range Rover', 'VW']

#Display the list items and show how many cars are in the original list
print(f"The are {len(cars)} cars in the list namely \n", "1.", cars[0], " \n 2.", cars[1], " \n 3.", cars[2], " \n 4.", cars[3], " \n 5.", cars[4], "\n")

#Add one more item in the original list by using list.append(x) method
cars.append('Toyota')

#Display the length of the new car
print(f"There are", len(cars), f"cars after {(cars[5])} was added to the list")


