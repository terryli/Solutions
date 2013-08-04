#!/usr/bin/python

# ---------------
# Given a deck of size N and a cut of size C every time, how many perfect 
# shuffles do you need to cut before you get back to the original deck?
#
# A perfect shuffle is defined as taking two stacks of cards and sorting them
# in such a way that you interleave the cards one from each stack.
#
# SMART SOLUTION: Works for any N and C efficiently
#
# Difficulty: 5/5
# ---------------

import sys

def main():
    size = int(sys.argv[1])
    diff = int(sys.argv[2])
    table = {}
    completed = 0
    count = 0
    start = [i for i in xrange(size)]
    deck = start

    while (True):
        count = count + 1
        merged = shuffle(deck, size, diff)

        for i in range(size):
            if (table.has_key(i) == False):
                if (start[i] == merged[i]):
                    table[i] = count
                    completed = completed + 1
        
        if (completed == size):
            print lcmm(table.values())
            return
        else: 
            deck = merged

def shuffle(deck, size, diff):
    side = deck[0:size-diff]
    main = deck[size-diff:]
    merged = [y for x in map(None,side,main) for y in x if y is not None]
    return merged

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(counts):
    return reduce(lcm, counts)

main()
