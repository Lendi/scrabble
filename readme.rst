Problem Statement:
------------------
Write a program that takes a Scrabble rack as a command-line argument and prints all valid Scrabble words that can be constructed from that rack, along with their Scrabble scores, sorted by score. 

Requirements:
-------------

(Input) - A word containing 7 alphabets where repetitions are allowed.

(Data) 
1. List containg all the alphabets and thier Scrabble values.
#. List of valid words in a file called swopods.txt 

(Conditions) 
1. Size of the smallest possible string is 2
#. The list of words are arranged in order
#. Input should be in Uppercase.

Procedure: 
----------
+ Read 7 letters using command line argument.
+ Create a dictionary containg all the alphabets and thier Scrabble values.
+ Store all the words of swopods.txt into a list.
+ Find all the possible strings of 7 letters using permutations,remove duplicates and store them into a list.
+ Compare both the lists  and store all the legal words in an another list.
+ Count the score of each word in the above list.
+ Print the highest score word.  

