#!/usr/bin/env python3

def print_fibonacci(length):
    result = [0, 1, 1]
    while len(result) < length:
        result.append(result[-2] + result[-1])
    print([] if length == 0 else result[0:length] if length < 3 else result)
    