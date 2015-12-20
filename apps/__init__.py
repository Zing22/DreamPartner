# -*- coding=utf-8 -*-
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
# from .views import lib
import os,sys
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

app = Flask(__name__)
print(__name__)
app.config.from_object('config')
app.config["APPLICATION_ROOT"] = 'apps'
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))


from apps import views, models, baseview
from apps.models import *
reload(sys)
sys.setdefaultencoding('utf8')
text_factory = str

@lm.user_loader
def load_user(id):
    return user.query.get(int(id))

from apps.views import dreamp
from apps.views import sp
app.register_blueprint(dreamp.mod)
app.register_blueprint(sp.mod)
