import requests
import json


class TLDRClient(object):
    api_url = "https://api.tldr.io/"
    
    def __init__(self, name, key):
        self.name = name
        self.key = key

    def headers(self):
        return {
            'name': self.name,
            'key': self.key,
            'content-type': 'application/json'
        }

    def _check(self, response):
        #this could get more sophisticated.  copy from the js library
        if response.status_code >= 200:
            #success codes should be handled here
            if response.status_code == 200:
                return response.json()
        if response.status_code >= 400:
            #default error. assumes the api returns error text as the body
            error = {
                'code': response.status_code,
                'error': response.text
            }
            if response.status_code == 404:
                error['error'] = "URL not found."

            return error
            

    def getLatestTldrs(self, number):
        url = self.api_url + "tldrs/latest/" + str(number)
        response = requests.get(url, headers=self.headers())
        return self._check(response)

    def searchByUrl(self, target_url):
        url = self.api_url + "tldrs/search"
        response = requests.get(url, params={"url": target_url}, headers=self.headers())
        return self._check(response)

    def searchBatch(self, target_urls):
        url = self.api_url + "tldrs/searchBatch"
        response = requests.post(url, data=json.dumps({'batch': target_urls}), headers=self.headers())
        return self._check(response)

    def getUser(self, username, tldrs=False):
        url = self.api_url + "users/"+username+"/"
        if tldrs:
            url += "tldrsCreated"
        response = requests.get(url, headers=self.headers())
        return self._check(response)

    def getUserData(self, username):
        return self.getUser(username, True)

if __name__ == '__main__':
    print "Why are you running this????"

