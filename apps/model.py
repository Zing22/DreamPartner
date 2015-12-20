# -*- coding=utf-8 -*-

from apps import db

LOWTEXTLENGTH = 64;
MAXTEXTLENGTH = 256;

class user(db.Model):
	__tablename__ = "user"
	uid = db.Column(db.Integer, primary_key = True)
	nickname = db.Column(db.String(LOWTEXTLENGTH), unique = True)
	userDescription = db.Column(db.String(MAXTEXTLENGTH))
	email = db.Column(db.String(MAXTEXTLENGTH), unique = True)
	password = db.Column(db.String(LOWTEXTLENGTH))
	exp = db.Column(db.Integer)

class group(db.Model):
	__tablename__ = "group"
	gid = db.Column(db.Integer, primary_key = True)
	groupName =  db.Column(db.String(LOWTEXTLENGTH), unique = True)
	groupDescription = db.Column(db.String(MAXTEXTLENGTH))
	managerUid = db.Column(db.Integer)

class task(db.Model):
	__tablename__ = "task"
	tid = db.Column(db.Integer, primary_key = True)
	gid = db.Column(db.Integer)
	date = db.Column(db.DateTime)
	uidOwner = db.Column(db.Integer)
	uidExer = db.Column(db.Integer)
	point = db.Column(db.Integer)
	status = db.Column(db.String(LOWTEXTLENGTH))
	taskTitle = db.Column(db.String(LOWTEXTLENGTH))
	taskDescription = db.Column(db.String(MAXTEXTLENGTH))

class groupUser(db.Model):
	__tablename__ = "groupUser"
	fid = db.Column(db.Integer, primary_key = true)
	uid = db.Column(db.Integer)
	gid = db.Column(db.Integer)

class groupItems(db.Model):
	__tablename__ = "groupItems"
	tid = db.Column(db.Integer, primary_key = True)
	gid = db.Column(db.Integer)
	cost = db.Column(db.Integer)
	itemName = db.Column(db.String(LOWTEXTLENGTH))
	itemDescription = db.Column(db.String(MAXTEXTLENGTH))
	
class groupUserItems(db.Model):
	__tablename__ = "groupUserItems"
	fid = db.Column(db.Integer, primary_key = True)
	uid = db.Column(db.Integer)
	tid = db.Column(db.Integer)
	
class groupInforms(db.Model):
	__tablename__ = "groupInforms"
	iid = db.Column(db.Integer, primary_key = True)
	gid = db.Column(db.Integer)
	title = db.Column(db.String(LOWTEXTLENGTH))
	content = db.Column(db.String(MAXTEXTLENGTH))

class groupComments(db.Model):
	__tablename__ = "groupComments"
	cid = db.Column(db.Integer, primary_key = True)
	gid = db.Column(db.Integer)
	uid = db.Column(db.Integer)
	content = db.Column(db.String(MAXTEXTLENGTH))
	time = db.Column(db.DateTime)


'''
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
'''

