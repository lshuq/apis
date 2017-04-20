from flask import *
from api_test.apis.token import token_haved
from api_test.main.app_init import app
from api_test.models.api_users.user_edit import *


@app.route('/ppsp/login', methods=['POST'])
def user_login():
    api_id = request.json.get('api_id')
    api_secret = request.json.get('api_secret')
    token = up_token(api_id, api_secret)
    if token is False:
        return make_response("你的id或者secret出错！，请检查！")
    else:
        token_text = token.token_text
        print(request.headers['token'])
        return jsonify({'token': token_text})


# 增
@app.route('/ppsp/add', methods=['POST'])
def user_add():
    api_id = request.json.get('api_id')
    api_secret = request.json.get('api_secret')
    print(api_id, api_secret)
    if api_id is None or api_secret is None:
        abort(400)
    if have_user(api_id=api_id) is False:
        abort(400)
    add_user(api_id, api_secret)
    return jsonify({'code': 1, 'msg:': 'success'})


@app.route('/', methods=['GET', 'POST'])
@token_haved
def get_resource():
    # token_text = ""
    # if request.headers['token'] != "":
    token_text = request.headers['token']
    # if request.json.get('token') is not None:
    #     token_text = request.json.get('token')
    token = token_can_use(token_text)
    if token is False:
        return jsonify({'code': 0, 'msg:': 'fault'})
    user = have_user(id_in_table=token.id)
    if user is False:
        return jsonify({'code': 0, 'msg:': 'fault'})
    return jsonify({'api_id': user.api_id, 'api_secret': user.api_secret, 'msg:': 'success'})
