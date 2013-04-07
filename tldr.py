import requests
import json


class TLDRClient(object):
    """
    An api wrapper for http://tldr.io/ 
    """
    api_url = "https://api.tldr.io/"
    
    def __init__(self, name, key):
        self.name = name
        self.key = key

    def headers(self):
        """
        Helper to return request headers
        """
        return {
            'name': self.name,
            'key': self.key,
            'content-type': 'application/json'
        }

    def _check(self, response):
        """
        Returns the state of the response.  Data on success, error on failure
        """
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
        """
        Retrieve the latest tldrs :: GET /tldrs/latest/:number
        """
        url = self.api_url + "tldrs/latest/" + str(number)
        response = requests.get(url, headers=self.headers())
        return self._check(response)

    #I'd almost like to call this getUrlOr404
    def searchByUrl(self, target_url):
        """
        Retrieve tldr for url or 404 :: GET /tldrs/search/?url=:url
        """
        url = self.api_url + "tldrs/search"
        response = requests.get(url, params={"url": target_url}, headers=self.headers())
        return self._check(response)

    def searchBatch(self, target_urls):
        """
        Retrieve the tldrs for a set of urls :: POST /tldrs/searchBatch
        """
        url = self.api_url + "tldrs/searchBatch"
        response = requests.post(url, data=json.dumps({'batch': target_urls}), headers=self.headers())
        return self._check(response)

    def getUser(self, username):
        """
        Retrieve user data :: GET /users/:username
        """
        url = self.api_url + "users/"+username+"/"
        if tldrs:
            url += "tldrsCreated"
        response = requests.get(url, headers=self.headers())
        return self._check(response)

    def getUserData(self, username):
        """
        Retrieve tldrs by user :: GET /users/:username/tldrsCreated/
        """
        url = self.api_url + "users/"+username+"/tldrsCreated"
        response = requests.get(url, headers=self.headers())
        return self._check(response)

if __name__ == '__main__':
    print "Why are you running this? import it!"

