def add_two_numbers(a, b):
  """
  This function adds two numbers and returns the sum.

  Args:
    a: The first number.
    b: The second number.

  Returns:
    The sum of the two numbers.
  """

  return a + b

#Getting two numbers from user to add
first_number, second_number = input("Enter two numbers to add: \n").split()

# Calling the function
sum = add_two_numbers(int(first_number), int(second_number))

# Printing the result
print(f"The sum of {first_number} and {second_number} is: {sum}")
