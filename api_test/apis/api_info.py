import base64

from flask import *
from api_test.main.app_init import app
from api_test.models.info_base.info_edit import *
from api_test.apis.token import token_haved


@app.route("/ppsp/add_info", methods=['POST'])
@token_haved
def add_info():
    info_dict = request.json
    info = info_add(info_dict)
    if info:
        return jsonify({"code": 0, "msg": "处理成功", "id": info.cmpany_id})
    return jsonify({"code": 0, "msg": "error"})


@app.route("/ppsp/modify_info", methods=['POST'])
@token_haved
def modify_info():
    info_dict = request.json
    info = info_modify(info_dict)
    if info:
        return jsonify({"code": 0, "msg": "处理成功", "id": info.cmpany_id})
    return jsonify({"code": 0, "msg": "error"})
