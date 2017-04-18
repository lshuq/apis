# 查
from api_test.models.api_users.user_model import *


def search_user(api_id, api_secret):
    try:
        tmp = User.get(User.api_id == api_id, User.api_secret == api_secret)
    except:
        return False
    return tmp


def have_user(api_id=None, api_secret=None, id_in_table=None, *args, **kwargs):
    if api_id is not None:
        try:
            user = User.get(User.api_id == api_id)
            return user
        except:
            return False
    if api_secret is not None:
        try:
            user = User.get(User.api_secret == api_secret)
            return user
        except:
            return False
    if id_in_table is not None:
        try:
            user = User.get(User.id == id_in_table)
            return user
        except:
            return False
    # 找不到user,返回False
    return False


def user_by_api_id(api_id):
    try:
        user = User.get(User.api_id == api_id)
        return user
    except:
        return False


def user_by_api_secret(api_secret):
    try:
        user = User.get(User.api_secret == api_secret)
        return user
    except:
        return False


def user_by_id(id_in_table):
    try:
        user = User.get(User.id == id_in_table)
        return user
    except:
        return False


# 添加
def add_user(api_id, api_secret):
    tmp = User()
    tmp.api_id = api_id
    tmp.api_secret = api_secret
    token = IdToken()
    token.token_text = tmp.get_user_token()
    tmp.save()
    token.save()
    return tmp


# 删除
def del_user(api_id):
    try:
        tmp = User.get(User.api_id == api_id)
        token = IdToken.get(IdToken.id == tmp.id)
        token.delete_instance()
        tmp.delete_instance()
    except:
        return False
    return tmp


# 更新
def update_user_secret(api_id, api_secret, new_secret):
    try:
        tmp = User.get(User.api_id == api_id, User.api_secret == api_secret)
        tmp.api_secret = new_secret
        tmp.save()
    except:
        return False
    return tmp


# 获取token
def get_token(api_id, api_secret):
    user = User.get(User.api_id == api_id, User.api_secret == api_secret)
    token = IdToken()
    token.token_text = user.get_user_token()
    token.token_use = True
    token.save()


# 更新token
def up_token(api_id, api_secret):
    try:
        user = User.get(User.api_id == api_id, User.api_secret == api_secret)
        token = IdToken.get(IdToken.id == user.id)
        token.token_text = user.get_user_token()
        token.token_time = datetime.now()
        token.token_use = True
        token.save()
        return token
    except:
        return False


# 判断token过期,或无效
def token_can_use(token_text):
    try:
        token = IdToken.get(IdToken.token_text == token_text)
    except:
        return False
    if token is None or token.token_use is False:
        return False
    if ((datetime.now() - token.token_time).days >= 1):
        token.token_use = False
        token.save()
        return False
    return token
