#!/usr/bin/python

# ---------------
# Given a list of any number of integers, and a search list of N integers,
# write an algorithm that will return the shortest snippet within the list
# that contains all N integers in any order.
#
# Difficulty: 5/5
# ---------------

import sys

def main():
    body = [1, 2, 4, 5, 7, 10, 2, 2, 5, 3, 10, 4, 6, 8, 8, 9, 2, 3, 1, 1, 5, 9]
    args = [2, 3, 5]

    pos = 0
    table = {}
    global_mins = {}
    current_mins = {}
    dist = len(body)

    for i in args:
        table[i] = []
        current_mins[i] = []

    for n in body:
        for i in args:
            if (n == i):
                table[i].append(pos)
                continue
        pos = pos + 1

    for i in args:
        current_mins[i] = table[i].pop(0)

    idx = min(current_mins, key=current_mins.get)

    while (True):
        x = max(current_mins.values())
        y = min(current_mins.values())
        diff = x - y

        if (diff < dist):
            dist = diff
            global_mins = current_mins.copy()

            if (len(table[idx]) > 0):
                current_mins[idx] = table[idx].pop(0)
                idx = min(current_mins, key=current_mins.get)
            else:
                break
        else:
            print global_mins
            return


main()
