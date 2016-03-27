from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh.index import open_dir


ix = open_dir("index")

with ix.searcher() as searcher:
	query = QueryParser("content", ix.schema).parse("passport")
	results = searcher.search(query)
	for i in results:
		print i['path']


