from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.corpus import stopwords
from nltk.stem.porter import *
import operator
from nltk.tokenize import sent_tokenize
from  nltk.probability import FreqDist

def make_summary( text):
	sent = []
	stemmed = []
	tokens = word_tokenize(text)
	sent = sent_tokenize(text)
	for token in tokens:
		if token in stopwords.words('english'):
			tokens.remove(token)
	stemmer = PorterStemmer()

	for token in tokens:
	 	stemmed.append(stemmer.stem(token))
#freq(stemmed)
	for word in stemmed:
		word.lower()
	word_freq = FreqDist(stemmed)

	most_freq_words = [pair[0] for pair in word_freq.items()[:60]]

	working_sent = [sentence.lower() for sentence in sent]

	out_sent = []

	for word in most_freq_words:
		for i in range(0,len(working_sent)):
			if (word in working_sent[i] and sent[i] not in out_sent):
				out_sent.append(sent[i])
				break
			if len(out_sent) >= 5:
			 	break
		
		if len(out_sent) >= 5:
			break

	return reorder(out_sent,text)





def reorder(out_sent,text):
	out_sent.sort(lambda s1,s2:	text.find(s1) - text.find(s2))
	return out_sent
	
def summarize( text):
	
	print " ".join(make_summary(text))
        

		
'''
def freq(words):
	freqncy = {}
	for word in words:
		if word not in freqncy.keys():
			freqncy[word] = 1
		else:
			freqncy[word] = freqncy[word] + 1

	sorted_freq = sorted(freqncy.iteritems(),key=operator.itemgetter(1),reverse = True)
	print sorted_freq

'''


