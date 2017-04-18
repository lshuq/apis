from flask import *
from api_test.apis.api_user import *
from api_test.main.app_init import app
from api_test.apis.api_user import token_haved
from api_test.models.api_terrains.terrain_block_edit import *


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
    if result is not None:
        return jsonify({'warning': "订单号为   "+result + " 的订单已存在，未被添加！"})
    return make_response("upload success")


@app.route("/ppsp/delete_terrain_block", methods=["POST"])
@token_haved
def delete_terrain_block():
    pass


@app.route("/ppsp/search_terrain_block", methods=["POST"])
@token_haved
def search_terrain_block():
    pass
