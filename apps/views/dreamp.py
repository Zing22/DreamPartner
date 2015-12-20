# -*- coding=utf-8 -*-

from flask import Blueprint, render_template, jsonify,\
                    flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from apps import db, lm
from apps.models import *
from apps.libs.dreamp.dreamp_logic import *

# mod = Blueprint('dreamp', __name__, url_prefix='/dreamp')
mod = Blueprint('dreamp', __name__, url_prefix='/apps/dreamp')

@mod.route('/')
@mod.route('/index')
def index():
    user = g.user
    return render_template('dreamp/index.html',
        title = 'Index',
        user=user,)


@mod.before_request
def before_request():
    g.user = current_user


@mod.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('.index'))
    if request.method == 'POST':
        if request.form.get('remember-me') is not None:
            remember = True
        else:
            remember = False
        if checkLogin(request.form['username'],request.form['password']):
            user = Player.query.filter_by(username=request.form['username']).first()
            login_user(user, remember=remember)
            return redirect(url_for('.index'))
        else:
            flash("Check your input and try again.")
    return render_template('dreamp/login.html', title='Sign In')


@mod.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('.index'))


@mod.route('/register')
def register():
    return redirect(url_for('.index'))
