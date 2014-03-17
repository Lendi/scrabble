#!usr/bin/python

import sys
import itertools

inputIs = sys.argv[1]
all_possible = []
used_words = []

from itertools import permutations
for r in range(2,8):#range is taken assuming that string passed is of length 7
        possible = [''.join(p) for p in permutations(inputIs.upper(),r)]#strings of length r 
        all_possible.extend(possible)#strings of all lengths in a list
        unique_words = set(all_possible)#duplicates removed

words = [line.strip() for line in open("/home/charvitha/ts/scrabble/sowpods.txt",'r')]

valid_words = []
for each in unique_words:
        if each in words:
                valid_words.append(each.lower())#all legal words
                
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
score_of_words=[]
for word in valid_words:
	score=0
	for letter in word:
		score+=scores[letter]#value of each letter is being added to produce the score 
	a=(score,word)
	score_of_words.append(a)

required_set = sorted(score_of_words,reverse=True)#soretd in descending order

for score_wise in required_set:
	print score_wise

