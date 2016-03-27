# Intranet-Search

Basic search for IITG Intranet. To test, follow below the steps:

```
scrapy crawl IITG
```

Links will be saved in log.txt. Remove first line of log.txt and rename the file to links.txt.
Run the following for indexing.
```
python indexor.py
```

Edit the search query in search.py, and run search.py

```
python search.py
```


> **Todo:**


> - Implement threading for the crawler indexing and link scraping.
> - Allow search.py to take CLI arguments as search queries.
> - Implement pagination of search results, echo total number of links.
> - Think of features and implement them for the search.
