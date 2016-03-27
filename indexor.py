from whoosh.index import create_in
from whoosh.fields import *
import string
import sys,urllib2,urllib,socket
from whoosh.qparser import QueryParser

from bs4 import BeautifulSoup

timeout = 3
socket.setdefaulttimeout(timeout)


schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
ix = create_in("index", schema)
writer = ix.writer()

with open('links.txt') as fp:
    for line in fp:
	url = line
	if ".pdf" not in url:
		print line
		try:
			f = urllib.urlopen(url)
			content1 = f.read()
			soup = BeautifulSoup(content1)
			title = soup.get_text() 
			
			writer.add_document(title=unicode(url,"utf-8"), path=unicode("/"+url,"utf-8"),content=unicode(title))
			#writer.add_document(title=u"Second document", path=u"/b",content=u"The second one is even more interesting!")

		except Exception as e:
			print "Caught exception e"
	
writer.commit()




