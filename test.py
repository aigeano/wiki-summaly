import re, requests, sys
from bs4 import BeautifulSoup, NavigableString
import bleach
import summaly

t = " "

def strip_tags(data,inv):

	pattern = ['&lt','&gt','/[.*/]','html','body',';',':','/']
	soup = BeautifulSoup(data)
	for tag in soup.findAll(True):
		if tag.name in inv:
		 	s = ""
		  	for c in tag.contents:
		    		if not isinstance(c,NavigableString):
					c = strip_tags(unicode(c),inv)
				s +=unicode(c)
			tag.replaceWith(s)

	p = soup.findAll('p')
	for para in p:

		p1 = bleach.clean(para, strip = True)

	        p2 = re.sub(pattern[0],"",p1)

	        for pat in pattern :

			p2 = re.sub(pat,"",p2)

	        build_text(p2)


def build_text(txt):
	global t  
	t = t + " " + txt 


def main():
	global t
	r = requests.get("http://en.wikipedia.org/wiki/facebook")
	data= r.text
	inv = ['a','span','h2','img','sup','i','b']
        soup = BeautifulSoup(data)
	strip_tags(data,inv)
	summaly.summarize(t)
if __name__=='__main__':
        main()
