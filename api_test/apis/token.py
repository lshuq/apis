from flask import *
import functools

from api_test.models.api_users.user_edit import token_can_use


def token_haved(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            token_text = request.headers['token']
            if token_can_use(token_text):
                    return func(*args, **kwargs)
            else:
                return make_response("token is wrong!")
        except:
            return make_response("request has some wrong!")

    return wrapper
