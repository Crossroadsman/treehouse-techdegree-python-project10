import os
import unittest
import tempfile
import json

from flask import request

from peewee import *

# the below syntax works when calling
# `python3 -m unittest` from the main project directory
# as long as the tests directory has a __init__.py file in it
# (even though __init__.py is optional since Python 3.3)
import app
import config
import models


# Throughout this file:
# `app` refers to the module `app.py`
# `app.app` refers to the Flask app.
# `app.config` refers to the config.py file imported by `app.py`
# `app.app.config` refers to the config dictionary-like object in
#   the Flask app.


class TestToDoList(unittest.TestCase):

    # Setup and Teardown
    # ==================
    def setUp(self):

        # Flask apps have a config attribute. This is a reference
        # to a Config object (a dictionary-like object). This does
        # not read in the values from our `config.py` file by default.
        #
        # create a temp database file
        # (we get a file handle and a filename with full path)
        # (note, the file handle is low-level so we need to use
        # os.close() instead of <fh>.close() to close it)
        self.temp_db_fh, config.DATABASE_FILENAME = tempfile.mkstemp()

        # Set testing mode
        # (This disables error catching during request handling, so
        # we can get better error reports)
        app.app.config["TESTING"] = True

        # Create a test client
        self.app = app.app.test_client()

        # Set the db location then point models at the test DB
        # Initialise the DB
        models.initialize()

    def tearDown(self):
        # perform cleanup
        os.close(self.temp_db_fh)  # close the file
        os.unlink(config.DATABASE_FILENAME)  # remove the file

    # Tests
    # =====
    def test_todolist_get_returns_correct_response(self):

        test_todo_item_data = [
            {'name': 'first test item', 'completed': True},
            {'name': 'second test item', 'completed': False},
            {'name': 'a third test item', 'completed': False},
        ]
        for todo_item in test_todo_item_data:
            models.Todo.create(**todo_item)

        # response is a flask.wrappers.Response object
        response = self.app.get('/api/v1/todos')

        json_data = response.get_json()

        for i, item in enumerate(json_data):
            expected_data = test_todo_item_data[i]
            self.assertEqual(item['name'], expected_data['name'])
            self.assertEqual(item['completed'], expected_data['completed'])

    def test_todolist_post_with_valid_data_returns_correct_response(self):

        uri = '/api/v1/todos'
        data = {
            'name': 'a valid test item',
            'completed': False,
            'edited': True
        }

        response = self.app.post(
            uri,
            data=json.dumps(data),
            content_type='application/json'
        )

        response_text = response.get_json()

        expected_status = 201
        expected_body = {
            'name': 'a valid test item',
            'completed': False,
        }

        self.assertEqual(response.status_code, expected_status)
        for key, value in expected_body.items():
            self.assertEqual(response_text[key], value)


class TestToDo(unittest.TestCase):

    # Setup and Teardown
    # ==================
    def setUp(self):

        self.temp_db_fh, config.DATABASE_FILENAME = tempfile.mkstemp()
        app.app.config["TESTING"] = True
        self.app = app.app.test_client()
        models.initialize()

    def tearDown(self):
        # perform cleanup
        os.close(self.temp_db_fh)  # close the file
        os.unlink(config.DATABASE_FILENAME)  # remove the file

    # Tests
    # =====
    def test_todo_put_with_name_change_returns_correct_response(self):

        test_todo_item_data = [
            {'name': 'first test item', 'completed': True},
            {'name': 'second test item', 'completed': False},
            {'name': 'a third test item', 'completed': False},
        ]
        for todo_item in test_todo_item_data:
            models.Todo.create(**todo_item)

        uri = '/api/v1/todos/2'
        data = {
            'name': 'modified second test item',
            'completed': False,
            'edited': True
        }
        response = self.app.put(
            uri,
            data=json.dumps(data),
            content_type='application/json'
        )

        json_data = response.get_json()

        expected_data = {
            'name': data['name'],
            'completed': False
        }
        expected_status_code = 200

        self.assertEqual(response.status_code, expected_status_code)
        for key in ['name', 'completed']:
            self.assertEqual(json_data[key], expected_data[key])

    def test_todo_put_with_completed_change_returns_correct_response(self):

        test_todo_item_data = [
            {'name': 'first test item', 'completed': True},
            {'name': 'second test item', 'completed': False},
            {'name': 'a third test item', 'completed': False},
        ]
        for todo_item in test_todo_item_data:
            models.Todo.create(**todo_item)

        uri = '/api/v1/todos/2'
        data = {
            'name': 'second test item',
            'completed': True,
            'edited': True,
        }
        response = self.app.put(
            uri,
            data=json.dumps(data),
            content_type='application/json'
        )

        json_data = response.get_json()

        expected_data = {
            'name': data['name'],
            'completed': True
        }
        expected_status_code = 200

        self.assertEqual(response.status_code, expected_status_code)
        for key in ['name', 'completed']:
            self.assertEqual(json_data[key], expected_data[key])

    def test_todo_put_with_changes_modifies_correctly(self):
        """The PUT request not should modify any other items"""

        test_todo_item_data = [
            {'name': 'first test item', 'completed': True},
            {'name': 'second test item', 'completed': False},
            {'name': 'a third test item', 'completed': False},
        ]
        for todo_item in test_todo_item_data:
            models.Todo.create(**todo_item)

        uri = '/api/v1/todos/2'
        data = {
            'name': 'modified second test item',
            'completed': True,
            'edited': True,
        }
        response = self.app.put(
            uri,
            data=json.dumps(data),
            content_type='application/json'
        )

        json_data = response.get_json()

        expected_data = [
            {'name': 'first test item', 'completed': True},
            {'name': 'modified second test item', 'completed': True},
            {'name': 'a third test item', 'completed': False},
        ]

        all_items = models.Todo.select()

        for i, item in enumerate(all_items):
            self.assertEqual(expected_data[i]['name'], item.name)
            self.assertEqual(expected_data[i]['completed'], item.completed)

    def test_todo_delete_with_valid_data_returns_correct_response(self):

        test_todo_item_data = [
            {'name': 'first test item', 'completed': True},
            {'name': 'second test item', 'completed': False},
            {'name': 'a third test item', 'completed': False},
        ]
        for todo_item in test_todo_item_data:
            models.Todo.create(**todo_item)

        uri = '/api/v1/todos/2'
        data = None

        response = self.app.delete(uri, data=data)
        response_text = response.get_data(as_text=True)

        expected_status = 204
        with app.app.test_request_context():
            self.app.get(uri)
            base_url = request.url_root

        expected_location = base_url + 'api/v1/todos'
        expected_response_body = ""

        self.assertEqual(response.status_code, expected_status)
        self.assertEqual(response.headers['Location'], expected_location)
        self.assertEqual(response_text, expected_response_body)

    def test_todo_delete_with_valid_data_only_modifies_specified_item(self):

        test_todo_item_data = [
            {'name': 'do not delete', 'completed': True},
            {'name': 'DELETE ME', 'completed': False},
            {'name': 'also do not erase', 'completed': False},
        ]
        for todo_item in test_todo_item_data:
            models.Todo.create(**todo_item)

        uri = '/api/v1/todos/2'
        data = None

        self.app.delete(uri, data=data)

        do_not_delete = models.Todo.select().where(
            models.Todo.name == 'do not delete'
        )
        delete_me = models.Todo.select().where(
            models.Todo.name == 'DELETE ME'
        )
        also_do_not_erase = models.Todo.select().where(
            models.Todo.name == 'also do not erase'
        )

        self.assertEqual(do_not_delete.count(), 1)
        self.assertTrue(do_not_delete.get().completed)
        self.assertEqual(delete_me.count(), 0)
        self.assertEqual(also_do_not_erase.count(), 1)
        self.assertFalse(also_do_not_erase.get().completed)

# ------------------------

if __name__ == '__main__':
    unittest.main()
