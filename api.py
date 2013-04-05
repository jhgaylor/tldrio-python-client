import requests

class TLDRClient(object):
    api_url = "https://api.tldr.io/"
    
    def __init__(self, name, key):
        self.name = name
        self.key = key

    def headers(self):
        return {
            'name': self.name,
            'key': self.key
        }

    def check(self, response):
        #this could get more sophisticated.  copy from the js library
        if response.status_code == 200:
            return response.json()
        else:
            return {
                'code':response.status_code,
                'error': response.text
            }

    def getLatestTldrs(self, number):
        url = self.api_url + "tldrs/latest/" + str(number)
        response = requests.get(url, headers=self.headers())
        return self.check(response)

    def searchByUrl(self, target_url):
        #check the requests docs
        url = self.api_url + "tldrs/search"
        response = requests.get(url, data={"url": target_url}, headers=self.headers())
        return self.check(response)

    def searchBatch(self, target_urls):
        #getting odd output via python, but the endpoint seems to be working fine from fetcher
        #{"tldrs": [], "urls": {"o": "other://o", "d": "other://d", "i": "other://i", "h": "other://h", "l": "other://l", "/": "other:///", ".": "other://.", "p": "other://p", "r": "other://r", "t": "other://t", ":": "other://:"}}
        url = self.api_url + "tldrs/searchBatch"
        response = requests.post(url, data={"batch": target_urls}, headers=self.headers())
        return self.check(response)

    def getUser(self, username, tldrs=False):
        url = self.api_url + "tldrs/latest/" + str(number)
        response = requests.get(url, headers=self.headers())
        return self.check(response)

#GET /users/:username/tldrsCreated
import json
t = TLDRClient("jakegaylor", "8P5mD26fGye43y66K5p5")
print t.api_url
#t.getLatestTldrs(3)
print json.dumps(t.searchBatch(["http://tldr.io/"]))

# r = requests.get("http://codegur.us")
# print r.text