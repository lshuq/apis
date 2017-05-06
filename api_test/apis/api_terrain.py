import re

from flask import *
from api_test.apis.api_user import *
from api_test.main.app_init import app
from api_test.models.api_terrains.terrain_block_edit import *
from api_test.apis.token import token_haved


@app.route("/ppsp/upload_terrain_block", methods=["POST"])
@token_haved
def upload_terrain_block():
    result = ''
    if not request.json:
        abort(400)  # 请求无效
    for datas in request.json:
        # 判断属性是否完整
        if {'order_id', 'name', 'type', 'area', 'edge'}.issubset(datas) is False:
            return make_response("Lack of some values")
        a = upload_terrain(datas)
        if a is False:
            result += (str(datas['order_id']) + '  ')
    if result is not '':
        return jsonify({'warning': "订单号为   " + result + " 的订单已存在，未被添加！"})
    return make_response("upload success")


@app.route("/ppsp/delete_terrain_block", methods=["POST"])
@token_haved
def delete_terrain_block():
    data = request.json
    if delete_terrain(order_id=data["order_id"]) is not False:
        return jsonify({"delete": "success"})
    return make_response("信息出错或数据不存在，请检查输入！")


@app.route("/ppsp/search_terrain_block", methods=["POST"])
@token_haved
def search_terrain_block():
    try:
        order_id = request.json['order_id']
    except:
        order_id = False
    if order_id:
        blocks = search_terrain(order_id=order_id)
        if blocks is False or len(blocks) is 0:
            return jsonify({"error": "查找不到！"})
        datas = []
        for block in blocks:
            data = show_terrain(block)
            datas.append(data)
        return jsonify(datas)
        # try:
        #     name = request.json['name']
        # except:
        #     name = False
        # if name:
        #     block = search_terrain(name=name)
        #     if block is not False:
        #         data = show_terrain(block)
        #         return jsonify(data)
        # return make_response("fail")
