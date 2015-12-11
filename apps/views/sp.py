# -*- coding=utf-8 -*-

from flask import Blueprint, render_template, jsonify,\
                    flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from apps import db, lm
from apps.models import User

mod = Blueprint('sp', __name__, url_prefix='/apps/sp')

@mod.route('/genetree')
def index():
    return render_template('sp/genetree.html')
