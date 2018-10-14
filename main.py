from flask import Flask, request
from apis import api
from databse import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/rest?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


def init():
    db.init_app(app)
    api.init_app(app)

    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    init()
    app.run(debug=True)