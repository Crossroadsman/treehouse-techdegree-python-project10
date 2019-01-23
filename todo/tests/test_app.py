import os
import unittest
import tempfile

from peewee import *

import app


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
        response = self.app.get('/')

        self.assertEqual(response.status_code, 200)

    def test_my_todos_renders_correct_template(self):
        response = self.app.get('/')

        expected_text = b'<title>Todo API with Flask</title>'
        self.assertIn(expected_text, response.data)

    def test_favicon_can_load_file(self):
        with self.app.get('/favicon.ico') as response:
            self.assertEqual(response.status_code, 200)


# ------------------------

if __name__ == '__main__':
    unittest.main()
