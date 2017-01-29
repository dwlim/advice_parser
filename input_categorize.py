#!/bin/usr/python

import json
import difflib

def tokenize(str):
	str = str.lower()
	words = str.split()
	return words

def determineCategory(arr, category):
	count = {"Social Life": 0, "Family": 0, "School": 0, "Relationship": 0, "Political": 0, "Health": 0, "Environment": 0, "Technology": 0, "Self": 0}
	keywords = {"Social Life": [], "Family": [], "School": [], "Relationship": [], "Political": [], "Health": [], "Environment": [], "Technology": [], "Self": []}

	for cat in category: 
		for key in category[cat]:
			keywords[cat].append(str(key))
	
	for input in arr: 
		for cat in category: 
			keys = difflib.get_close_matches(input, keywords[cat], 1)
			if (len(keys) > 0):
				




	
	# maxWeight = 0
	# match = ""
	# for cat in count:
	# 	if count[cat] > maxWeight: 
	# 		maxWeight = count[cat]
	# 		match = cat

	#return match


def main():
	with open("categories.json") as data_file: 
		category = json.load(data_file)

	words = tokenize("My family is so bad because I hate my brother")
	determineCategory(words, category)

if __name__ == '__main__':
	main()



