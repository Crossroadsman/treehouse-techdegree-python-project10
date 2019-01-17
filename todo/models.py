import datetime

from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer,
                          BadSignature, SignatureExpired)
from peewee import *

import config


DATABASE = SqliteDatabase('todo.sqlite')

# Models
# ------
class Todo(Model):
    name = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


# Helper Functions
# ----------------
def initialize():
    DATABASE.connect(reuse_if_open=True)
    DATABASE.create_tables([Todo], safe=True)
    DATABASE.close()
