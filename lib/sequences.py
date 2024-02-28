#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = [0, 1]

    if length <= 0:
        print([])
    elif length == 1:
        print(fibonacci_sequence[:1])
    elif length == 2:
        print(fibonacci_sequence)
    else:
        while len(fibonacci_sequence) < length:
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_number)
        print(fibonacci_sequence)
   