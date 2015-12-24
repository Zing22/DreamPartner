from apps import db
from models import *

# chart1
def createUser(nickname, email, password):
	newUser = user(nickname, "他还没有填写个人简介", email, password)
	db.session.add(newUser)
	db.commit()
	return uid

def deleteUser(uid):
	try:
		db.session.delete(user.query.get(uid))
		db.commit()
		return true
	except Exception:
		return false

def getNickname(uid):
	return nickname

def setNickname(uid, newNickname):
	return true | false  #success or not
	
def checkPassword(username, inputedPassword):
	return true | false  #correct or not

def setPassword(uid, newPassword):
	return true | false  #success or not

def getExp(uid):
	return exp;

def increaseExp(uid, addedExp):
	return true | false  #success or not

# chart2
def createGroup(groupname, managerid):
	return gid

def deleteGroup(gid):
	return true | false;

def setGroupName(gid, name):
	return true | false;

def getGroupName(gid):
	return name;

def setGroupDescription(gid, contentText):
	return true | false;

def getGroupDescription(gid):
	return Groupdescription;
	
def setManager(gid, newUid):
	return true | false;

def getManager(gid):
	return managerid ;

#chart 3
def createTask(taskName, gid, uidOwner):
	return tid;

def deleteTask(tid):
	return true | false;

def setExer(uidExer):
	return true | false;

def getExer(tid):
	return uid;

def getGroup(tid) :
	return gid;

def setPoint(tid, newPoint) :
	return true | false;

def getPoint(tid) :
	return point;

def setStatus(tid, newStatus):
	return true | false;
	
def getStatus(tid):
	return Status;

def setTasktitle(tid, newTasktitle):
	return true | false;
	
def getTasktitle(tid):
	return Tasktitle;

def setTaskdescription (tid, newTaskdescription ):
	return true | false;
	
def getTaskdescription (tid):
	return Taskdescription ;

def getTaskExeBy(uid) :
	return (tid)

def getTaskOf(gid) :
	return (tid)

def getAllTask() :
	return (tid)

#chart4
def joinGroup(gid, uid):
	return true | false

def exitGroup(gid, uid):
	return true | false

def checkExist(gid, uid):
	return true | false;

def getGroups(uid) :
	return groups;

def getMember(gid) :
	return members;

#chart5
def createUserPoint(gid, uid) :
	return fid; -> # Need or not ?

def deleteUserPoint(gid, uid) :
	return true | false; -> # Need or not ?

def deleteUserPoint(fid) :
	return true | false; -> # Need or not ?

def getmagicpoint(gid, uid) :
	return magicpoint;

def setmagicpoint(gid, uid, newmagicpoint) :
	return true | false;

def getearnpoint(gid, uid) :
	return earnpoint;

def setearnpoint(gid, uid, newearnpoint) :
	return true | false;

#chart 6
def createItem(gid, cost, itemName, itemDescription) :
	try:
		u = groupItems(gid, cost, itemName, itemDescription)
		db.session.add(u)
		db.commit()
		return u.tid
	except Exception:
		return -1

def deleteItem(tid) :
	try:
		u = groupItems.query.get(tid).first()
		db.session.delete(u)
		db.commit()
		return True
	except Exception:
		return False

def getCost(tid) :
	try:
		u = groupItems.query.get(tid).first()
		return u.cost
	except Excepption:
		return -1;

def setCost(tid, newCost) :
	try:
		u = groupItems.query.get(tid).first()
		u.cost = newCost
		db.session.commmit()
		return True
	except Excepption:
		return False

def getItemname(tid) :
	try:
		u = groupItems.query.get(tid).first()
		return u.itemName
	except Excepption:
		return "I don't know!"

def setItemName(tid, newItemName) :
	try:
		u = groupItems.query.get(tid).first()
		u.itemName = newItemName
		db.session.commmit()
		return True
	except Excepption:
		return False

def getItemDescription(tid) :
	try:
		u = groupItems.query.get(tid).first()
		return u.itemDescription
	except Excepption:
		return "I don't know!"

def setItemdescription(tid, newItemdescription) :
	try:
		u = groupItems.query.get(tid).first()
		u.itemDescription = itemDescription
		db.session.commmit()
		return True
	except Excepption:
		return False

def getItems(tgid) :
	try:
		u = groupItems.query.filter(gid = tgid)
		ret = []
		for x in u :
			ret.append(u.tid)
		return tuple(ret)
	except Exception:
		return "I don't know!"
# return tid

def getTid(tgid, titemName) :
	try :
		u = groupItems.query.filter_by(gid = tgid, itemName = titemName).first()
		return u.tid
	except Exception :
		return -1
"""
if there is more than one item have a same name in one groups, this method will only return one of them.
"""

def getItemsGid(tid) :
	try:
		u = GroupItems.query.get(tid).first()
		return u.gid
	except Exception :
		return -1
	

#chart 7
def createUserItems(uid, tid) :
	try:
		u = groupUserItems(uid, tid)
		db.session.add(u)
		db.commit()
		return u.tid
	except Exception:
		return -1

def deleteUserItems(fid) :
	try :
		u = groupUserItems.query.get(fid).first()
		db.session.delete(u)
		db.commit()
		return True
	except Exception :
		return False

def getUserItems(tuid) :
	try :
		u = groupUserItems.query.filter_by(uid = tuid)
		ret = []
		for x in u :
			ret.append(u.tid)
		return tuple(ret)
	except Exception :
		return ()
# return tid

def getUserItemsOfGroup(tuid, tgid) :
	try :
		u = getUserItems(tid)
		ret = []
		for x in u :
			if getItemsGid(x.gid) == tgid :
				ret.append(x.tid)
		return tuple(ret)
	except Exception :
		return ()
	
def getUserItemFid(tuid, ttid) :
	try :
		u = groupUserItems.query.filter_by(uid = tuid, tid = ttid).first()
		return u.fid;
	except Exception :
		return -1;
#	return fid; -> first appear

# chart 8
def createGroupInforms(gid, title, content) :
	try :
		u = groupInforms(gid, title, content)
		db.session.add(u)
		db.commit()
		return u.iid
	except Exception :
		return -1;

def deleteGroupInforms(iid) :
	try :
		u = groupInforms.query.get(iid).first()
		db.session.delete(u)
		db.commit()
		return True
	except Exception :
		return False

def setGid(iid, tgid) :
	try :
		u = groupInforms.query.get(iid).first()
		u.gid = tgid
		db.commit()
		return True
	except Exception :
		return False

def getGid(iid) :
	try :
		u = groupInforms.query.get(iid).first()
		return u.gid
	except Exception :
		return "NULL"
		
def setTitle(iid, newTitle) :
	try :
		u = groupInforms.query.get(iid).first()
		u.title = newTitle
		db.commit()
		return True
	except Exception :
		return False

def getTitle(iid) :
	try :
		u = groupInforms.query.get(iid).first()
		return u.title
	except Exception :
		return "NULL"

def setContent(iid, newContent) :
	try :
		u = groupInforms.query.get(iid).first()
		u.content = newContent
		db.commit()
		return True
	except Exception :
		return False

def getContent(iid) :
	try :
		u = groupInforms.query.get(iid).first()
		return u.content
	except Exception :
		return "NULL"

"""
def setTime(iid, newTime) :
	try :
		u = groupInforms.query.get(iid).first()
		u.releasetime = newTime
		db.commit()
		return True
	except Exception :
		return False
"""

def getInformsReleasetime(iid) :
	try :
		u = groupInforms.query.get(iid).first()
		return u.releasetime
	except Exception :
		return -1

def getInformsOfGroup(tgid) :
	try :
		u = groupInforms.query.filter_by(gid = tgid)
		ret = []
		for x in u :
			ret.append(x.iid)
		return tuple(ret)
	except Exception :
		return ()
# unsorted

def getFirstInforms(tgid) :
	try :
		u = groupInforms.query.filter_by(gid = tgid)
		mylist = list(u)
		mylist.sort(lambda x, y : cmp(x.releasetime, y.releasetime), reverse = True)
		return mylist[0].iid
	except Exception :
		return -1
# if unsucceed, return -1
# otherwise, return iid
# compare by releasetime

#chart 9
def createGroupComments(gid, uid, content) :
	try :
		u = GroupComments(gid, uid, content)
		db.session.add(u)
		db.commit()
		return u.cid
	except :
		return -1
	return cid;  # initialization time

def deleteGroupComments(cid) :
	try :
		u = GroupComments.get(cid).first()
		db.session.delete(u)
		db.commit()
		return True
	except Exception :
		return False

def setContent(cid, newContent) :
	try :
		u = GroupComments.get(cid).first()
		u.content = newContent
		db.commit()
		return True
	except Exception :
		return False

def getContent(cid) :
	try :
		u = GroupComments.get(cid).first()
		db.session.delete(u)
		db.commit()
		return True
	except Exception :
		return False

def getCommentsReleasetime(cid) :
	try :
		u = GroupComments.get(cid).first()
		return u.releasetime
	except Exception :
		return -1
	

