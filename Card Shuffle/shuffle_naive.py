#!/usr/bin/python

# ---------------
# Given a deck of size N and a cut of size C every time, how many perfect 
# shuffles do you need to cut before you get back to the original deck?
#
# A perfect shuffle is defined as taking two stacks of cards and sorting them
# in such a way that you interleave the cards one from each stack.
#
# NAIVE SOLUTION: Breaks at high N and C numbers
#
# Difficulty: 3/5
# ---------------

import sys

def main():
    size = int(sys.argv[1])
    diff = int(sys.argv[2])
    count = 0
    start = [i for i in xrange(size)]
    deck = start

    while (True):
        count = count + 1
        merged = shuffle(deck, size, diff)
        if (start == merged):
            print count
            return
        else:
            deck = merged

def shuffle(deck, size, diff):
    side = deck[0:size-diff]
    main = deck[size-diff:]
    merged = [y for x in map(None,side,main) for y in x if y is not None]
    return merged

main()
