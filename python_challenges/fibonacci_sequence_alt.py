last_number = int(input("Enter last number"))

fibonacci_sequence = [0, 1]

for i in range(2, last_number-1):
    fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
print(fibonacci_sequence)

