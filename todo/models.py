import datetime

from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer,
                          BadSignature, SignatureExpired)
from peewee import *

import config


DATABASE = SqliteDatabase(None)

# Models
# ------
class Todo(Model):
    """This model replicates all the data fields on the Angular app's
    Todo items, except `edited` which at the back end is always False
    """
    name = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)
    completed = BooleanField(default=False)

    class Meta:
        database = DATABASE


# Helper Functions
# ----------------
def initialize():

    # We can use Run-time database configuration to set the DB to load
    # at runtime (this allows us to change the DB filename from our test
    # suite before creating the database)
    # see:
    # http://docs.peewee-orm.com/en/latest/peewee/database.html#run-time-database-configuration
    DATABASE.init(config.DATABASE_FILENAME)
    DATABASE.connect(reuse_if_open=True)
    DATABASE.create_tables([Todo], safe=True)
    DATABASE.close()
