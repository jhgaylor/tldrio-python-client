# Python client for tldr.io's public API

Python client for <a href="http://tldr.io">tldr.io</a>'s
public API (whose doc you can find <a href="http://tldr.io/api-documentation">here</a>).


## Installation

Via pip

    pip install git+https://github.com/jhgaylor/tldrio-python-client.git

### OR

Clone the repo

    git clone https://github.com/jhgaylor/tldrio-python-client.git


## Creating a client
```python
from tldr import TLDRClient

client = TLDRClient("name", "key")
```

## Getting the latest tldrs
The syntax is `client.getLatestTldrs(number, params)`, where `number` is the number of tldrs you want to get (maximum 50) and params (optional) is a dictionary representing a query string. For example:

Returns a list of tldrs or error object

```python
#latest 5 tldrs
tldrs = client.getLatestTldrs(5)
```

```python
#latest 5 tldrs for category "tech-news"
tldrs = client.getLatestTldrs(5, parms={'category':"tech-news"})
```

## Searching tldrs by url
The syntax is `client.searchByUrl(url)` where `url` is the url (figures ...) For example:

Returns a tldr or error object

```python
tldr = client.searchByUrl('http://tldr.io')
```

## Searching the tldrs for a batch of urls
The syntax is `client.searchBatch(urls)` where `urls` is an array of urls.  You can't search for more than 50 tldrs at once. For example:

Returns a list of tldrs or error object

```python
tldrs = client.searchBatch(['http://tldr.io', 'http://news.ycombinator.com/'])
```

## Getting user data
The syntax is `client.getUser(username)` where `username` is the username of the target user.  For example:

Returns a user or error object

```python
user_data = client.getUser('jhgaylor')
```



## Searching tldrs by user
The syntax is `client.getUserTldrs(username)` where `username` is the username of the author of the tldrs For example:

Returns a list of tldrs or error object

```python
tldrs = client.getUserTldrs('jhgaylor')
```

## Getting tldr categories

The syntax is `client.getCategories()`  For example:

Returns a list of tldrs or error object

```python
categories = client.getCategories()
```

The data format is:

```javascript
[
    {
        "_id": "5150639a43aac5ab0b000001",
        "type": "category",
        "name": "Tech News",
        "slug": "tech-news"
    },
    ...
]
```

## Getting tldr categories

The syntax is `client.getLatestTldrsByCategory(number, category_slug)`  where `number` is the number of tldrs you want to get (maximum 50) and category_slug is the slug returned from /categories/ For example:

Returns a list of tldrs or error object

```python
#alias for client.getLatestTldrs(5, params={'category':"tech-news"})
tldrs = client.getLatestTldrsByCategory(5, "tech-news")
```
