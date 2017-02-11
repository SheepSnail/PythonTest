#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def is_prime(n):
    if n < 2:
        return False
    for x in range(2, n):
        if x ** 2 > n:
            break
        if n % x == 0:
            return False
    return True

def prime_numbers():
    primes = []
    for x in range(101):
        if is_prime(x):
            primes.append(x)
    return primes

print(prime_numbers())
