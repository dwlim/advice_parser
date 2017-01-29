#!/bin/usr/python

import json
import difflib
import operator
import random

def tokenize(str):
	str = str.lower()
	words = str.split()
	return words

def determineCategory(arr, categories):
	count = {"Social Life": 0, "Family": 0, "School": 0, "Relationship": 0, "Political": 0, "Health": 0, "Environment": 0, "Technology": 0, "Self": 0}
	keywords = categoriesToKeywordsList(categories)
	
	for input in arr: 
		for cat in categories: 
			#keys = difflib.get_close_matches(input, keywords[cat], 1)
			for word in keywords[cat]:
				if (word ==input):
					# add boolean for noMatches
					count[cat] += categories[cat][word]
					
			#if (len(keys) > 0):
				#count[cat] += categories[cat][keys[0]]

	return max(count.items(), key=operator.itemgetter(1))[0]

def categoriesToKeywordsList(categories):
	keywords = {"Social Life": [], "Family": [], "School": [], "Relationship": [], "Political": [], "Health": [], "Environment": [], "Technology": [], "Self": []}

	for cat in categories: 
		for key in categories[cat]:
			keywords[cat].append(str(key))
	
	return keywords

def getJoke(arr, jokes, category):
	dict = jokes[category]

	for word in arr:
		for key in dict:
			if (key == word):
				jokes = dict[key].split("~")
				return random.choice(jokes)
	
	#To be modified to general category. Need to change return of determineCategory
	randomSubCat = dict[random.choice(list(dict.keys()))]
	return random.choice(dict[randomSubCat].split("~"))

def main():
	with open("categories.json") as data_file: 
		categories = json.load(data_file)

	with open("category_terms.json") as jokes_file:
		jokes = json.load(jokes_file)

	words = tokenize("fat")
	category = determineCategory(words, categories)
	print(getJoke(words, jokes, category))

if __name__ == '__main__':
	main()