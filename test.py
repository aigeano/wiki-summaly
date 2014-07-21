import re, requests, sys
from bs4 import BeautifulSoup, NavigableString
import bleach
def strip_tags(data,inv):
	soup = BeautifulSoup(data)
	for tag in soup.findAll(True):
		if tag.name in inv:
		 	s = ""
		  	for c in tag.contents:
		    		if not isinstance(c,NavigableString):
					c = strip_tags(unicode(c),inv)
				s +=unicode(c)
			tag.replaceWith(s)
	return soup


def main():
	r = requests.get("http://en.wikipedia.org/wiki/google")
	data= r.text
	inv = ['p','a','span','h2','img','sup']
	pattern = ['&lt','&gt','/[.*/]','html','body',';',':','/']
        soup = BeautifulSoup(data)
	p = strip_tags(data,inv)
	p1 = bleach.clean(p, strip = True)
	p2 = re.sub(pattern[0],"",p1)
	for pat in pattern :
		p2 = re.sub(pat,"",p2)
	print p2
if __name__=='__main__':
        main()
