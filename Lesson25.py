def break_words(stuff):
	"""This function breaks words apart"""
	words = stuff.split(' ')
	return words
	
def sort_words(words):
	"""Sorts the words"""
	return sorted(words)
	
def print_first_word(words):
	"""prints the first word"""
	word = words.pop(0)
	print word
	
def print_last_word(words):
	"""prints the last word"""
	word = words.pop(-1)
	print word
	
def sort_sentence(sentence):
	"""takes in a sentence and returns sorted words"""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""takes the first and last word from a sentence"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Prints out some shit"""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	
	
	
