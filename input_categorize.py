#!/bin/usr/python

import json
import difflib
import operator

def tokenize(str):
	str = str.lower()
	words = str.split()
	return words

def determineCategory(arr, categories):
	count = {"Social Life": 0, "Family": 0, "School": 0, "Relationship": 0, "Political": 0, "Health": 0, "Environment": 0, "Technology": 0, "Self": 0}
	keywords = {"Social Life": [], "Family": [], "School": [], "Relationship": [], "Political": [], "Health": [], "Environment": [], "Technology": [], "Self": []}

	for cat in categories: 
		for key in categories[cat]:
			keywords[cat].append(str(key))
	
	for input in arr: 
		for cat in categories: 
			keys = difflib.get_close_matches(input, keywords[cat], 1)
			if (len(keys) > 0):
				count[cat] += categories[cat][keys[0]]

	return max(count.items(), key=operator.itemgetter(1))[0]

def determineSubCategory(arr, categories, category):
	keywords = {"Social Life": [], "Family": [], "School": [], "Relationship": [], "Political": [], "Health": [], "Environment": [], "Technology": [], "Self": []}

	for cat in category: 
		for key in category[cat]:
			keywords[cat].append(str(key))




	
	# maxWeight = 0
	# match = ""
	# for cat in count:
	# 	if count[cat] > maxWeight: 
	# 		maxWeight = count[cat]
	# 		match = cat

	#return match


def main():
	with open("categories.json") as data_file: 
		categories = json.load(data_file)

	words = tokenize("My family is so bad because I hate my brother")
	category = determineCategory(words, categories)
	print(category)

if __name__ == '__main__':
	main()



