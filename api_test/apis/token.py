from flask import *
import functools

from api_test.models.api_users.user_edit import token_can_use


def token_haved(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            token_text = request.headers['token']
            if token_can_use(token_text):
                try:
                    return func(*args, **kwargs)
                except:
                    return make_response("Some wrong happened in request.json!")
            else:
                return make_response("token is wrong!")
        except:
            return make_response("request.headers has not token")

    return wrapper


# def token_haved(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             if request.headers['token'] != "":
#                 token_text = request.headers['token']
#                 if token_can_use(token_text):
#                     return func(*args, **kwargs)
#                 else:
#                     return make_response("token is wrong!")
#         except:
#             return make_response("request is empty")
#             # if request.json.get('token') is not None:
#             #     token_text = request.json.get('token')
#             #     if token_can_use(token_text):
#             #         return func(*args, **kwargs)
#             #     else:
#             #         pass
#
#     return wrapper