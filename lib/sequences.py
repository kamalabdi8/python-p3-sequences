#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])  # Print an empty list for length = 0
        return
    elif length == 1:
        print([0])  # Print a list with one element for length = 1
        return
    
    # Generate Fibonacci sequence for length >= 2
    fibonacci = [0, 1]
    for f_ in range(2, length):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    print(fibonacci)
