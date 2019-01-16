import os
import unittest
import tempfile

from peewee import *

import app


VERBOSE = False


class TestApp(unittest.TestCase):
    
    # Setup and Teardown
    # ------------------
    def setUp(self):

        # Set testing mode
        # (This disables error catching during request handling, so
        # we can get better error reports)
        app.app.config["TESTING"] = True

        # Create a test client
        self.app = app.app.test_client()

    # Tests
    # -----
    def test_my_todos_can_load_page(self):
        # response is a flask.wrappers.Response object
        response = self.app.get('/')
        
        if VERBOSE:
            print("==== DEBUG response object ====")
            print("response object")
            print(type(response))
            print(dir(response))
            print("Interesting attributes:")
            print(f"content_encoding: {response.content_encoding}")
            print(f"data (byte string): {response.data}")
            print(f"data type: {type(response.data)}")
            print(f"get_data: {response.get_data()}")
            print(f"status_code: {response.status_code}")
            print(f"status_code type: {type(response.status_code)}")
            print(f"json: {response.json}")
            print(f"get_json: {response.get_json()}")
            print(f"headers: {response.headers}")
            print(f"headers type: {type(response.headers)}")
            print(f"headers attributes: {dir(response.headers)}")
            print(f"location: {response.location}")
            print("==== END DEBUG response object ====")

        self.assertEqual(response.status_code, 200)


    def test_my_todos_renders_correct_template(self):
        response = self.app.get('/')

        expected_text = b'<title>Todo API with Flask</title>'
        self.assertIn(expected_text, response.data)


# ------------------------

if __name__ == '__main__':
    unittest.main()
