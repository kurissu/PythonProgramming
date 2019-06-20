# counterStr.py
#  Created by Kris Tantinirundr on 03/31/19.
#  Copyright © 2019 Kurisu Industries. All rights reserved.

def count(word):
	for letter in set(word):
		print(letter +" "+ str(word.count(letter)))

word = input("Enter a word: ")
count(word)
