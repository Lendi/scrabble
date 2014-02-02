#!usr/bin/python

import sys
import itertools

inputIs = sys.argv[1]
all_possible = []
posword = []

from itertools import permutations
for r in range(2,8):#range is taken assuming that string passed is of length 7
        possible = [''.join(p) for p in permutations(inputIs.upper(),r)]#strings of length r 
        all_possible.extend(possible)#strings of all lengths in a list
        used_words = set(all_possible)#duplicates removed

words = [line.strip() for line in open("/home/charvitha/ts/scrabble/sowpods.txt",'r')]
#score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
 #        "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
  #       "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
   #      "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
    #     "x": 8, "z": 10}

for x in used_words:
        if x in words:
                print x #prints legal words
