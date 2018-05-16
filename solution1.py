#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
"""
Re-ID
=====

There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been lording it over the poor minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has tasked you with reassigning everyone new, random IDs based on her Completely Foolproof Scheme.

She's concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion must draw a number from a hat. That number is the starting index in that string of primes, and the minion's new ID number will be the next five digits in the string. So if a minion draws "3", their ID number will be "71113".

Help the Commander assign these IDs by writing a function answer(n) which takes in the starting index n of Lambda's string of all primes, and returns the next five digits in the string. Commander Lambda has a lot of minions, so the value of n will always be between 0 and 10000.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) n = 0
Output:
    (string) "23571"

Inputs:
    (int) n = 3
Output:
    (string) "71113"

"""

import math

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x == 3:
        return True
    else:
        for n in range(2,x-1):
            if x % n == 0:
                return False
        return True

def find_next_prime_number(n):
    n = n + 1
    while 1:
        if is_prime(n):
            return n
        n = n + 1

max_index = 100000
size = 5
length = max_index + size

cache = ""
last_x = 1

def prepare(n):
    real_length = min(n, length)
    global cache
    global last_x
    while len(cache) < real_length:
        last_x = find_next_prime_number(last_x)
        cache = cache + str(last_x)
    return cache

def answer(n):
    # your code here
    result = prepare(n+size)
    return result[n:n+size]

print(answer(0))
print(answer(3))
