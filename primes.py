"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

def primes(number_of_primes):
    prime_list = []
    num = 2  # Initialize num to 2, the first prime number
    while len(prime_list) < number_of_primes:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    return prime_list

print(primes(100))