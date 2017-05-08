import base64
import re

from flask import *
from api_test.main.app_init import app
from api_test.models.info_base.info_edit import *
from api_test.apis.token import token_haved


def info_check(info, way=0):
    msg = []
    if 'pwd' not in info:
        msg.append('pwd')
    if 'name' not in info:
        msg.append('name')
    if 'company_type' not in info:
        msg.append('company_type')
    if 'address' not in info:
        msg.append('address')
    if 'comment' not in info:
        msg.append('comment')
    if 'principal_name' not in info:
        msg.append('principal_name')
    if 'principal_phone' not in info:
        msg.append('principal_phone')
    if 'contacts_name' not in info:
        msg.append('contacts_name')
    if 'contacts_phone' not in info:
        msg.append('contacts_phone')
    if 'hotline' not in info:
        msg.append('hotline')
    if way is 0:
        if 'company_id' not in info:
            msg.append('company_id')
    if way == 1:
        if 'code' not in info:
            msg.append('code')
        if 'authentication' not in info:
            msg.append('authentication')
        if 'logo' not in info:
            msg.append('logo')
        if 'business_licence' not in info:
            msg.append('business_licence')
        if 'qualification' not in info:
            msg.append('qualification')
    if msg == []:
        return False
    return msg


def info_check_value(info, way=0):
    msg = []
    x = info['company_type']
    if x < 1 or x > 3:
        msg.append('company_type')
    for i in info['principal_phone']:
        if i < '0' or i > '9':
            msg.append('principal_phone')
            break
    for i in info['contacts_phone']:
        if i < '0' or i > '9':
            msg.append('contacts_phone')
            break
    for i in info['hotline']:
        if i < '0' or i > '9':
            msg.append('hotline')
            break
    if 'email' in info:
        type = r"^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$"
        if not re.match(type, info['email']):
            msg.append('email')
    if way is 0:
        x = info['company_id']
        i = str(x)
        if i < '0' or i > '9':
            msg.append('company_id')
    if way == 1:
        i = info['authentication']
        if i < 0 or i > 1:
            msg.append('authentication')
    if msg == []:
        return False
    return msg


@app.route("/ppsp/add_info", methods=['POST'])
@token_haved
def add_info():
    info_dict = request.json
    lack = info_check(info_dict, way=1)
    if lack:
        return jsonify({"code": 0, "msg": "缺少参数", "缺少参数列表": lack})
    info = info_add(info_dict)
    if info:
        return jsonify({"code": 1, "msg": "处理成功", "id": info.company_id})
    return jsonify({"code": 0, "msg": "error"})


@app.route("/ppsp/modify_info", methods=['POST'])
def modify_info():
    info_dict = request.json
    lack = info_check(info_dict)
    if lack:
        return jsonify({"code": 0, "msg": "缺少参数", "缺少参数列表": lack})
    wrong = info_check_value(info_dict)
    if wrong:
        return jsonify({"code": 0, "msg": "参数出错", "出错参数列表": wrong})
    info = info_modify(info_dict)
    if info:
        return jsonify({"code": 1, "msg": "处理成功", "id": info.company_id})
    return jsonify({"code": 0, "msg": "error"})
