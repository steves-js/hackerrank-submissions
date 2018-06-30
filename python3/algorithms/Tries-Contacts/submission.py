#!/bin/python3

import math
import os
import random
import re
import sys

entries = dict();

# First reaction was to push all entries to a list, then go through the list of entries, however, it would not handle the large dataset
# Moved to a hash map to help with lookup but had to still get all the entries to add the possible enties
# Updated to make entries of send char combinations and number of occurances so for string 'abc' there would be {a:3 ab:2 abc:1}
def addEntry(entry):
    for index in range(len(entry)):
        entries[entry[:index+1]] = entries.get(entry[:index+1], 0) + 1

def find(key):
    print(entries.get(key, 0))

if __name__ == '__main__':
    n = int(input())

    for n_itr in range(n):
        opContact = input().split()

        op = opContact[0]

        contact = opContact[1]
        
        if op == 'add' and contact is not None:
            addEntry(contact)
        elif op == 'find' and contact is not None:
            find(contact)
