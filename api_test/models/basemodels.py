from peewee import *

mysql_db = MySQLDatabase(database='web', host='localhost', port=3306,
                         user='shu', passwd='password', charset='utf8')


class MySQLModel(Model):
    class Meta:
        database = mysql_db
