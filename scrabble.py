#!usr/bin/python
import sys
import itertools

all_possible = []
valid_words = []

def possible_words( rack ):
	from itertools import permutations
	for r in range(2,8):#range is taken assuming that string passed is of length 7 
		possible = [''.join(p) for p in permutations(rack.upper(),r)]#strings of length r 
		all_possible.extend(possible)#strings of all lengths in a list
		unique_words = set(all_possible)#duplicates removed
	return unique_words

def valid_scrabble_words(rack_words):
	words = [line.strip() for line in open("/home/charvitha/ts/scrabble/sowpods.txt",'r')]
	for each in rack_words:
		if each in words:
			valid_words.append(each.lower())#all legal words
	return valid_words
	
def count_score( scrabble_words):
	scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
	score_of_words = []
	for word in scrabble_words:
		score = 0
		for letter in word:
			score += scores[letter]#value of each letter is being added to produce the score 
		word_and_score = (score,word)
		score_of_words.append(word_and_score)
	return score_of_words
	
rack = sys.argv[1]
if len(rack) > 7 or len(rack) < 7:
	print "Enter a 7 letter word"
else:
	all_words = possible_words( rack )
	scrabble_words = valid_scrabble_words( all_words)
	word_scores = count_score(scrabble_words)
	required_set = sorted(word_scores,reverse = True)#soretd in descending order
	for score_wise in required_set:
		print score_wise
