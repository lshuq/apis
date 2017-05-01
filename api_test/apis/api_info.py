from flask import *
from api_test.main.app_init import app
from api_test.models.info_base.info_edit import *
from api_test.apis.token import token_haved


@app.route("/ppsp/add_info", methods=['POST'])
@token_haved
def add_info():
    info_dict = request.json
    print(info_dict['sss'])
    return jsonify(info_dict)
