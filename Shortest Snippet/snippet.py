#!/usr/bin/python

# ---------------
# Given a paragraph of any number of words, and a list of N search terms,
# write an algorithm that will return the shortest snippet within the list
# that contains all N terms in any order, case-insensitive.
#
# Difficulty: 5/5
# ---------------

import sys

def main():
    body_str = "The George Washington Bridge in New York City is one of the oldest bridges ever constructed. It is now being remodeled because the bridge is a landmark. City officials say that the landmark bridge effort will create a lot of new jobs in the city"
    args_str = "is a Landmark City Bridge"

    body = body_str.split(" ")
    args = args_str.split(" ")

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
            if (n.lower() == i.lower()):
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
