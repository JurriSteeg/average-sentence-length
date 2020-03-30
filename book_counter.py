import re


def open_book(book):
	"""turn all the books into text"""
	with open(book, encoding='utf-8') as infile:
		return infile.read()


def split_sentences(book):
	"""split the texts into sentences and put them in a list"""
	to_find = "[^ ].*?[^A-Z]+[!?.]"
	return [item for item in re.findall(to_find, open_book(book)) if item != '']


def split_words(book):
	"""split the sentences into words"""
	return [sentences.split() for sentences in split_sentences(book)]
	
	
def word_count(book):
	"""count the lenght of the senteces"""
	return [len(words) for words in split_words(book)]


def length_calculus(words):
	"""count the amount of words and the amount of sentences"""
	total = 0
	for i in words:
		total += words[i]
	return total, len(words)
	

def main():
	
	maxE_wordli = word_count('Max_Havelaar_English.txt')
	maxE_words, maxE_sen = length_calculus(maxE_wordli)
	lucE_wordli = word_count('Lucifer_English.txt')
	lucE_words, lucE_sen = length_calculus(lucE_wordli)
	chrE_wordli = word_count('Christmas_Carol_English.txt')
	chrE_words, chrE_sen = length_calculus(chrE_wordli)
	
	english_total = maxE_wordli + lucE_wordli + chrE_wordli
	english_words, english_sen = length_calculus(english_total)
	english_average = int(english_words/english_sen)
	
	
	maxD_wordli = word_count('Max_Havelaar_Dutch.txt')
	maxD_words, maxD_sen = length_calculus(maxD_wordli)
	lucD_wordli = word_count('Lucifer_Dutch.txt')
	lucD_words, lucD_sen = length_calculus(lucD_wordli)
	chrD_wordli = word_count('Christmas_Carol_Dutch.txt')
	chrD_words, chrD_sen = length_calculus(chrD_wordli)
	
	dutch_total = maxD_wordli + lucD_wordli + chrD_wordli
	dutch_words, dutch_sen = length_calculus(dutch_total)
	dutch_average = int(dutch_words/dutch_sen)
	
	
	higherD = 0 
	higherE = 0 
	lowerD = 0 
	lowerE = 0
	
	for i in dutch_total:
		if i >= english_average:
			higherD += 1
		else:
			lowerD += 1
			
	for i in english_total:
		if i >= english_average:
			higherE += 1
		else:
			lowerE += 1
	
	
	print("The average sentence length in the English Max Havelaar is: ", int(maxE_words/maxE_sen))
	print("The average sentence length in the English Lucifer is: ", int(lucE_words/lucE_sen))
	print("The average sentence length in the English Christmas Carol is: ", int(chrE_words/chrE_sen), "\n")
	print("The average sentence length in the English translations is: ", english_average, "\n")
	
	print("The average sentence length in the Dutch Max Havelaar is: ", int(maxD_words/maxD_sen))
	print("The average sentence length in the Dutch Lucifer is: ", int(lucD_words/lucD_sen))
	print("The average sentence length in the Dutch Christmas Carol is: ", int(chrD_words/chrD_sen), "\n")
	print("The average sentence length in the Dutch translations is: ", dutch_average, "\n")
	
	print("Dutch sentences higher than the English average:", higherD)
	print("Dutch sentences lower than the English average:", lowerD)
	print("English sentences higher than the English average:", higherE)
	print("English sentences lower than the English average:", lowerE)
	
		
if __name__ == '__main__':
	main()
