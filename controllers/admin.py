#encoding:utf-8
import flask
from models.models import *

admin = flask.Blueprint('admin',__name__)

@admin.route('/add')
def add():
    # table_test = FlaskTable(dafef='2017-02-01')
    # table_test = OneTable(dafef='2017-02-02')
    #table_test = TwoTable(dafef='2017-02-03')
    # db.session.add(table_test)
    # db.session.commit()
    return flask.render_template('admin/add.html')