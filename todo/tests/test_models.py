import os
import tempfile
import unittest

import config
import models

from peewee import *


class TestTodoModel(unittest.TestCase):

    # Setup and Teardown
    # ==================
    def setUp(self):

        # create a temp database file
        self.temp_db_fh, config.DATABASE_FILENAME = tempfile.mkstemp()

        # Set the DB location and point models at the test DB
        # Then initialise the DB
        models.initialize()

    def tearDown(self):
        os.close(self.temp_db_fh)  # close the temp db
        os.unlink(config.DATABASE_FILENAME)  # remove the file

    # Tests
    # =====
    def test_todo_model_can_be_created_with_name_only(self):

        # the following should not raise (peewee.IntegrityError)
        models.Todo.create(name="test item")

    def test_todo_model_requires_name(self):
        with self.assertRaises(IntegrityError):
            models.Todo.create()  # should raise

    def test_todo_model_allows_duplicate_items(self):
        """It's not uncommon for todo lists to have multiple instances
        of the same task. Need to ensure that the task name is not a
        required unique field"""
        test_name = 'test item'
        models.Todo.create(name=test_name)
        models.Todo.create(name=test_name)
        entries = models.Todo.select().where(models.Todo.name == test_name)
        self.assertEqual(entries.count(), 2)

    def test_initialize_uses_safe_mode_for_table_creation(self):
        models.initialize()  # should not raise (peewee.OperationalError)
