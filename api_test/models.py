from datetime import date
from peewee import *

db1 = SqliteDatabase('person.db')
db2 = MySQLDatabase('firstapi', user='shu', passwd='password')


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db1  # This model uses the "people.db" database.


class BaseModel(Model):
    class Meta:
        database = db2


class Book(BaseModel):
    author = CharField(default="me")
    title = TextField(default="1")

    class Meta:
        database = db2


class Tasks(BaseModel):
    task_id = IntegerField()
    title = CharField()
    description = TextField()
    done = BooleanField()


db2.create_table(Tasks, safe=True)
db2.create_table(Book, safe=True)

Book(author="tt", title="ll").save()
