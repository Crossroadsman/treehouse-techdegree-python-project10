# tests/test_basic.py
import os
import unittest
import tempfile

from peewee import *

# the below syntax works when calling
# `python3 -m unittest` from the main project directory
# as long as the tests directory has a __init__.py file in it
import app


class BasicTests(unittest.TestCase):
    # Throughout this file:
    # `app` refers to the module `app.py`
    # `app.app` refers to the Flask app.
    # `app.config` refers to the config.py file imported by `app.py`
    # `app.app.config` refers to the config dictionary-like object in
    #   the Flask app.

    # Setup and Teardown
    # ==================
    def setUp(self):

        # Flask apps have a config attribute. This is a reference
        # to a Config object (a dictionary-like object). This does
        # not read in the values from our `config.py` file by default.

        # Set testing mode
        # (This disables error catching during request handling, so
        # we can get better error reports)
        # (It propagates any exceptions to the test client)
        # See:
        # http://flask.pocoo.org/docs/1.0/config/#TESTING
        app.app.config['TESTING'] = True

        # By default Flask-WTF includes CSRF validation as part of POST
        # validation. Since we don't generate a CSRF when we execute a POST
        # in the test, we need to disable CSRF for these tests
        # (see, for example:
        # https://flowfx.de/blog/disable-csrf-validation-when-unit-testing-a-flask-app/
        # )
        app.app.config['WTF_CSRF_ENABLED'] = False

        # Not clear exactly why we want to disable this. For relevant Flask
        # docs see:
        # http://flask.pocoo.org/docs/1.0/config/#DEBUG
        app.app.config['DEBUG'] = False

        # create a temp database file
        # (we get a file handle and a filename with full path)
        # (note, the file handle is low-level so we need to use
        # os.close() instead of <fh>.close() to close it)
        self.temp_db_fh, app.app.config["DATABASE"] = tempfile.mkstemp()

        # Initialise the DB
        temp_db = SqliteDatabase(app.app.config["DATABASE"])
        temp_db.connect()
        temp_db.create_tables([], safe=True)
        temp_db.close()

        self.app = app.app.test_client()

    def tearDown(self):
        # perform cleanup
        os.close(self.temp_db_fh)  # close the file
        os.unlink(app.app.config["DATABASE"])  # remove the file

    # Tests
    # =====
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


# -----------------

if __name__ == "__main__":
    unittest.main()


    