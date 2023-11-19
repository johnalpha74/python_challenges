#The built-in function len() also applies to lists:

letters = ['a', 'b', 'c', 'd', 'e']
letters_length = len(letters)
print(letters_length)

letters.append('f')
letters_length = len(letters)
print(f"New letters length is: {letters_length} \n")

