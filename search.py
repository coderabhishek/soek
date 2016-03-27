from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh.index import open_dir
import sys 

ix = open_dir("index")
print sys.argv[1]+"-------------------\n\n\n"
with ix.searcher() as searcher:
	query = QueryParser("content", ix.schema).parse(sys.argv[1])
	results = searcher.search(query)
	for i in results:
		print i['path']


