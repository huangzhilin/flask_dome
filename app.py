#encoding:utf-8

import flask
from common import config
from models import db

app = flask.Flask(__name__)
app.config.from_object(config)
db.init_app(app)

#使用蓝图来模块化
from controllers.user import user
from controllers.admin import admin
app.register_blueprint(user,url_prefix='/user')
app.register_blueprint(admin,url_prefix='/admin')

@app.route('/')
def hello_world():
    return 'index'

if __name__ == '__main__':
    app.run(port=8888)
