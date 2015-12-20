# try git

# chart1
def createUser(nickname, username, password):
	return uid

def deleteUser(uid):
	return true | false;

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
def createItem(gid) :
	return tid; -> # Need or not ?

def deleteItem(tid) :
	return true | false; -> # Need or not ?

def getCost(gid, tid) :
	return Cost;

def setCost(gid, tid, newCost) :
	return true | false;

def getItemname(gid, tid) :
	return Itemname;

def setItemname(gid, tid, newItemname) :
	return true | false;

def getItemdescription(gid, tid) :
	return Itemdescription;

def setItemdescription(gid, tid, newItemdescription) :
	return true | false;

#chart 7
def createItem(uid, tid) :
	return fid; -> # Need or not ?

def deleteItem(uid, tid) :
	return true | false; -> # Need or not ?

def getCost(gid, tid) :
	return Cost;

def setCost(gid, tid, newCost) :
	return true | false;

def getItemname(gid, tid) :
	return Itemname;

def setItemname(gid, tid, newItemname) :
	return true | false;

def getItemdescription(gid, tid) :
	return Itemdescription;

def setItemdescription(gid, tid, newItemdescription) :
	return true | false;

def getTimes(gid) :
	return items;

#chart 8
def createUserItems(gid, uid, tid) :
	return fid;

def deleteUserItems(gid, uid, tid) :
	return true | false;

def getUserItens(gid, uid) :
	return (items);

#def getUserItems(gid, uid, tid) :
#	return fid; -> first appear -> need or not ?

# chart 9
def createGroupInforms(gid) :
	return iid;

def deleteGroupInforms(iid) :
	return true | false;

def setTitle(iid, newTitle) :
	return true | false;

def getTitle(iid, newTitle) :
	return true | false;

def setTime(iid, newTime) :
	return true | false;

def getTime(iid) :
	return time;

def getInforms(gid) :
	return (Iid);

def getFirstInforms(gid) :
	return Iid;

#chart 10
def createGroupComments(gid, uid) :
	return cid;  # initialization time

def deleteGroupComments(cid) :
	return true | false;

def setContent(gid, uid, content) :
	return true | false;

def getContent(cid) :
	return content;

	

