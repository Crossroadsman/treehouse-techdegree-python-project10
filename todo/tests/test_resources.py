import os
import unittest
import tempfile

from peewee import *

import app


VERBOSE = False


class TestToDoList(unittest.TestCase):

    # Setup and Teardown
    # ------------------
    def setUp(self):

        # Flask apps have a config attribute. This is a reference
        # to a Config object (a dictionary-like object). This does
        # not read in the values from our `config.py` file by default.
        #
        # create a temp database file
        # (we get a file handle and a filename with full path)
        # (note, the file handle is low-level so we need to use
        # os.close() instead of <fh>.close() to close it)
        self.temp_db_fh, app.app.config["DATABASE"] = tempfile.mkstemp()

        # Set testing mode
        # (This disables error catching during request handling, so
        # we can get better error reports)
        app.app.config["TESTING"] = True

        # Create a test client
        self.app = app.app.test_client()

        # Initialise the DB
        temp_db = SqliteDatabase(app.app.config["DATABASE"])
        temp_db.connect()
        temp_db.create_tables([], safe=True)
        temp_db.close()

    def tearDown(self):
        # perform cleanup
        os.close(self.temp_db_fh)  # close the file
        os.unlink(app.app.config["DATABASE"])  # remove the file

    # Tests
    # -----
    def test_todolist_get_returns_correct_response(self):

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

        self.fail()




# ------------------------

if __name__ == '__main__':
    unittest.main()
