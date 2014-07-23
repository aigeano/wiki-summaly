from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.corpus import stopwords
from nltk.stem.porter import *
import operator
def word(text):
	stemmed = []
	tokens = word_tokenize(text)

	for token in tokens:
		if token in stopwords.words('english'):
			tokens.remove(token)
	stemmer = PorterStemmer()

	for token in tokens:
	 	stemmed.append(stemmer.stem(token))
	freq(stemmed)

	
		

def freq(words):
	freqncy = {}
	for word in words:
		if word not in freqncy.keys():
			freqncy[word] = 1
		else:
			freqncy[word] = freqncy[word] + 1

	sorted_freq = sorted(freqncy.iteritems(),key=operator.itemgetter(1),reverse = True)
	print sorted_freq
