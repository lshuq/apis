#!/flask/bin/python3.5
from flask import url_for, jsonify, abort, request, Flask
from passlib.apps import custom_app_context as pwd_context
from peewee import *

db = MySQLDatabase('firstapi', user='shu', passwd='password')

app = Flask(__name__)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(max_length=32, index=True)
    password_hash = CharField(max_length=128)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


db.create_table(User, safe=True)

a = db.execute_sql("select * from user")

for i in a:
    print(i[0])


@app.route('/test/user', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)  # missing arguments
    if User.filter(username=username).first() is not None:
        abort(400)  # existing user
    user = User(username=username)
    user.hash_password(password)
    user.save()
    return jsonify({'username': user.username}), 201, {
        'Location': url_for('user', name="me", _external=True)
    }


if __name__ == '__main__':
    app.run()
