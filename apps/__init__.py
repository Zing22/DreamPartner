# -*- coding=utf-8 -*-
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
# from .views import lib
import os,sys
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))


from apps import views, models
from apps.models import User
reload(sys)
sys.setdefaultencoding('utf8')
text_factory = str

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',title="404"), 404


@app.route('/')
def index(e):
	return render_template('index.html',title="Apps Index")

from apps.views import dreamp
app.register_blueprint(dreamp.mod)
