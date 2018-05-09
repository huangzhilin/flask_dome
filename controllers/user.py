#encoding:utf-8
import flask
from models.models import *

user = flask.Blueprint('user',__name__)

@user.route('/add')
def add():
    # table_test = FlaskTable(dafef='2017-02-01')
    # # table_test = OneTable(dafef='2017-02-02')
    # #table_test = TwoTable(dafef='2017-02-03')
    # db.session.add(table_test)
    # db.session.commit()
    return flask.render_template('user/add.html')