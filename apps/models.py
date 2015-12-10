# -*- coding=utf-8 -*-
from apps import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    password = db.Column(db.String(64))
    nickname = db.Column(db.String(64))
    email = db.Column(db.String(120), unique = True)

    #### Not allow to change begin ####
    is_authenticated = True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3
    #### Not allow to change end ####

    def __repr__(self):
        return '<User %r, %r, %r, %r, %r>' % (self.username, self.password,\
            self.nickname, self.email, self.authorization)