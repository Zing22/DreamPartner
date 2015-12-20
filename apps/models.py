# -*- coding=utf-8 -*-

from apps import db

LOWTEXTLENGTH = 64;
MAXTEXTLENGTH = 256;

# chart1
class user(db.Model):
	__tablename__ = "user"
	uid = db.Column(db.Integer, primary_key = True)
	nickname = db.Column(db.String(LOWTEXTLENGTH), unique = True)
	userDescription = db.Column(db.String(MAXTEXTLENGTH))
	email = db.Column(db.String(MAXTEXTLENGTH), unique = True)
	password = db.Column(db.String(LOWTEXTLENGTH))
	exp = db.Column(db.Integer)
	def __init__(self, nickname, userDescription, email, password):
		self.nickname = nickname
		self.userDescription = userDescription
		self.email = email
		self.password = password
		self.exp = 0

# chart2
class group(db.Model):
	__tablename__ = "group"
	gid = db.Column(db.Integer, primary_key = True)
	groupName =  db.Column(db.String(LOWTEXTLENGTH), unique = True)
	groupDescription = db.Column(db.String(MAXTEXTLENGTH))
	managerUid = db.Column(db.Integer)
	def __init__(self, groupName, groupDescription, managerUid):
		self.groupName = groupName
		self.groupDescription = groupDescription
		self.managerUid = managerUid

# char3
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
	def __init__(self, gid, date, uidOwner, point, taskTitle, taskDescription):
		self.gid = gid
		self.date = date
		self.uidOwner = uidOwner
		self.uidExer = -1
		self.point = point
		self.status = "NOT ACCEPTED YET"
		self.taskTitle = taskTitle
		self.taskDescription = taskDescription

# char4
class groupUser(db.Model):
	__tablename__ = "groupUser"
	fid = db.Column(db.Integer, primary_key = True)
	uid = db.Column(db.Integer)
	gid = db.Column(db.Integer)
	def __init__(self, uid, gid):
		self.uid = uid
		self.gid = gid

# char5
class groupItems(db.Model):
	__tablename__ = "groupItems"
	tid = db.Column(db.Integer, primary_key = True)
	gid = db.Column(db.Integer)
	cost = db.Column(db.Integer)
	itemName = db.Column(db.String(LOWTEXTLENGTH))
	itemDescription = db.Column(db.String(MAXTEXTLENGTH))
	def __init__(self, gid, cost, itemName, itemDescription):
		self.gid = gid
		self.cost = cost
		self.itemName = itemName
		self.itemDescription = itemDescription

# chart5
class groupUserItems(db.Model):
	__tablename__ = "groupUserItems"
	fid = db.Column(db.Integer, primary_key = True)
	uid = db.Column(db.Integer)
	tid = db.Column(db.Integer)
	def __init__(self, uid, tid):
		self.uid = uid
		self.tid = tid

# chart6
class groupInforms(db.Model):
	__tablename__ = "groupInforms"
	iid = db.Column(db.Integer, primary_key = True)
	gid = db.Column(db.Integer)
	title = db.Column(db.String(LOWTEXTLENGTH))
	content = db.Column(db.String(MAXTEXTLENGTH))
	def __init__(self, gid, title, content):
		self.gid = gid
		self.title = title
		self.content = content

# chart7
class groupComments(db.Model):
	__tablename__ = "groupComments"
	cid = db.Column(db.Integer, primary_key = True)
	gid = db.Column(db.Integer)
	uid = db.Column(db.Integer)
	content = db.Column(db.String(MAXTEXTLENGTH))
	time = db.Column(db.DateTime)
	def __init__(self, gid, uid, content, time):
		self.gid = gid
		self.uid = uid
		self.content = content
		self.time = time


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

