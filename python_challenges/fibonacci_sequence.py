#Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones.
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233 ...

previous_number = 0
next_number = 1

last_number = int(input("Enter the last number \n"))
while previous_number < last_number:
    print(previous_number, end=',')
    previous_number, next_number = next_number, previous_number + next_number

