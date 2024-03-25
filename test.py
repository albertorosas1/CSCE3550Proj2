import unittest
from unittest.mock import patch #unit testing
from http.server import HTTPServer #import http server
from main import MyServer #import server class from main.py

class TestMyServer(unittest.TestCase):
    def setUp(self):
        self.server = HTTPServer(('localhost', 8080), MyServer)
        self.server.allow_reuse_address = False  # checking to make sure its not already in use

    def tearDown(self):
        self.server.server_close() #testing for tearDown

    def test_do_POST_auth(self):
        with patch('http.server.BaseHTTPRequestHandler.send_response') as mock_send_response:
            # create a mock request
            self.server.path = '/auth?valid=1'
            self.server.do_POST()
            # making sure the 200 is sent
            mock_send_response.assert_called_once_with(200) #testing for valid end point

    def test_do_POST_invalid_endpoint(self):
        with patch('http.server.BaseHTTPRequestHandler.send_response') as mock_send_response:
            # create mock request path
            self.server.path = '/invalid_endpoint'
            self.server.do_POST()
            # make sure the response is set
            mock_send_response.assert_called_once_with(405) #test for posting to invalid endpoint

if __name__ == '__main__':
    unittest.main() #our unit testing main