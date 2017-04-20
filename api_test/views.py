#!/flask/bin/python3.5
from flask import jsonify, Flask
from models import Tasks

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': "aaa"})


if __name__ == "__main__":
    app.run(debug=True)
