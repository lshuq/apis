import random
from datetime import datetime

from api_test.models.basemodels import *


class IdToken(MySQLModel):
    token_text = CharField(max_length=64)
    token_time = DateTimeField(default=datetime.now())
    token_use = BooleanField(default=False)


class User(MySQLModel):
    api_id = IntegerField()
    api_secret = CharField()

    # 获取token,随机生成字符串
    def get_user_token(self):
        token = ''.join(list(map(lambda str_int: chr(str_int),
                                 [random.randrange(35, 91, 1) for _ in range(64)])))
        return token


try:
    mysql_db.create_tables(models=[User, IdToken])
except InternalError:
    pass
