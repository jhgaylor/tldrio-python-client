import unittest

import json
from tldr import *


class Response(object):
    """
    A dummy response object to mimick python-requests'
    response object.
    """
    def __init__(self, data, status_code):
        self.data = data
        self.status_code = status_code
        self.text = json.dumps(data)

    def json(self):
        return self.data


class ApiTest(unittest.TestCase):

    def setUp(self):
        """
        Create a client instance
        """
        self.name = "name"
        self.key = "key"
        self.client = TLDRClient(self.name, self.key)

    def test_init(self):
        """
        Test that the client instance created correctly
        """
        self.assertIsInstance(self.client, TLDRClient)

    def test_auth_headers(self):
        """
        Test that the headers were set correctly
        """
        self.assertEqual(self.client.auth_headers()['name'], self.name)
        self.assertEqual(self.client.auth_headers()['key'], self.key)

    def test_check_200(self):
        """
        Test that _check returns json on 200
        """
        response = Response({}, 200)
        checked_response = self.client._check(response)
        self.assertEqual(checked_response, {})

    def test_check_400(self):
        """
        Test that _check returns error json on 400
        """
        resp = Response({}, 400)
        checked_response = self.client._check(resp)
        self.assertEqual(checked_response['code'], 400)
        self.assertIsInstance(checked_response['error'], str)

    def test_getLatestTldrs(self):
        """
        Test that a json response is returned
        """
        resp = self.client.getLatestTldrs(5)
        self.assertTrue(resp)
        self.assertLessEqual(len(resp), 5)

    def test_searchByUrl(self):
        """
        Test that a json response is returned
        """
        resp = self.client.searchByUrl("http://tldr.io/")
        self.assertTrue(resp)
        self.assertTrue(json.dumps(resp))

    def test_searchBatch(self):
        """
        Test that a json response is returned
        """
        resp = self.client.searchBatch(["http://tldr.io/", ])
        self.assertTrue(resp)
        self.assertTrue(json.dumps(resp))

    def test_getUser(self):
        """
        Test that a json response is returned
        """
        resp = self.client.getUser("jhgaylor")
        self.assertTrue(resp)
        self.assertTrue(json.dumps(resp))

    def test_getUserTldrs(self):
        """
        Test that a json response is returned
        """
        resp = self.client.getUserTldrs("jhgaylor")
        self.assertTrue(resp)
        self.assertTrue(json.dumps(resp))

    def test_getCategories(self):
        """
        Test that a json response is returned
        """
        resp = self.client.getCategories()
        self.assertTrue(resp)
        self.assertTrue(json.dumps(resp))

    def test_getLatestTldrsByCategory(self):
        """
        Test that a json response is returned
        """
        resp = self.client.getLatestTldrsByCategory(5, "tech-news")
        self.assertTrue(resp)
        self.assertTrue(json.dumps(resp))

if __name__ == '__main__':
    unittest.main()
