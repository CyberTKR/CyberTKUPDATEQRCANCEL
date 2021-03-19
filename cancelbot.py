from linepy import *
from akad.ttypes import *
from akad.ttypes import IdentityProvider,LoginResultType,LoginRequest,LoginType,TalkException,ContentType as Type,ChatRoomAnnouncementContents,Location,ChatRoomAnnouncement
from thrift.protocol import TCompactProtocol,TMultiplexedProtocol,TProtocol
from thrift.transport import TTransport,TSocket,THttpClient,TTransport,TZlibTransport
from thrift import transport,protocol,server
from thrift.Thrift import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from multiprocessing import Pool,Process
from liff.ttypes import LiffChatContext,LiffContext,LiffSquareChatContext,LiffNoneContext,LiffViewRequest
from bs4 import BeautifulSoup
from bs4.element import Tag
import requests as uReq
from time import sleep
from gtts import gTTS
from Naked.toolshed.shell import execute_js
import ast,codecs,json,os,pytz,re,random,sys,time,urllib.parse,subprocess,threading,pyqrcode,pafy,humanize,os.path,traceback,time,random,sys,json,codecs,threading,glob,re,string,os,requests,subprocess,six,ast,pytz,urllib,urllib.parse,youtube_dl,pafy,timeit,atexit,traceback,ffmpy,humanize
from datetime import datetime,timedelta
from subprocess import Popen,PIPE
from googletrans import Translator
from zalgo_text import zalgo
from humanfriendly import format_timespan,format_size,format_number,format_length
from threading import Thread,Event
from random import randint
import html5lib,shutil,wikipedia,goslate
from youtube_dl import YoutubeDL
import requests,json
_session=requests.session()
requests.packages.urllib3.disable_warnings()
import time

cybertk=LINE()

_D='setTime'
_C='Auth Token : '
_B=False
_A=True
cybertk.log(_C+str(cybertk.authToken))
cybertk.log(_C+str(cybertk.getProfile().mid))
botStart=time.time()
KAC=[cybertk]
cybertkMID=cybertk.profile.mid
cyberTKPoll=OEPoll(cybertk)
temp_flood={}
settingsOpen=codecs.open('temp.json','r','utf-8')
settings=json.load(settingsOpen)
Bots=[cybertkMID]
admin=['']
wait={'contact':_A,'autoJoin':_A,'autoCancel':{'on':_A,'members':1},'leaveRoom':_A,'timeline':_A,'autoAdd':_A,'message':"【тнanĸѕ ғor add мe】\n╔══╗ \n║██║ \n║(O)║♫ ♪ ♫ ♪\n╚══╝\n▄ █ ▄ █ ▄ ▄ █ ▄ █ ▄ █\nMin- - - - - - - - - - - -●Max\n║➪ It's an automatic message.\nContact information was automatically \nSent to you. If you want to go there,\nyou can contact with contact information.\nI wish you a good day ⇐║\n.........█\U00100701\U00100103Suspicious Face\U0010ffff█▄▄▄▄▄▃\U00100302\U001001c2meteorite\U0010ffff\n..▂▄▅█████▅▄▃▂\n[██████████████\n◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲\n\n✯==== Creator ====✯\n\t\t\nhttp://line.me/ti/p/~cybertk0\n",'lang':'JP','comment':'Thanks for add me Owner\n{¶ http://line.me/ti/p/~cybertk0 ¶} ','commentOn':_B,'commentBlack':{},'wblack':_B,'dblack':_B,'clock':_B,'blacklist':{},'wblacklist':_B,'dblacklist':_B,'protectionOn':_A,'atjointicket':_B}
wait2={'readPoint':{},'readMember':{},_D:{},'ROM':{}}
setTime={}
setTime=wait2[_D]
def delExpire():
	B='time';A='expire'
	if temp_flood!={}:
		for tmp in temp_flood:
			if temp_flood[tmp][A]==_A:
				if time.time()-temp_flood[tmp][B]>=3*10:
					temp_flood[tmp][A]=_B;temp_flood[tmp][B]=time.time()
					try:userid='https://line.me/ti/p/~'+cybertk.profile.userid;cybertk.RESUREDNOGegasseMKTrebyC(tmp,'Spam is over , Now Bots Actived !',str(userid),'http://dl.profile.line-cdn.net/'+cybertk.tcatnoCteg(cybertkMID).pictureStatus,cybertk.tcatnoCteg(cybertkMID).displayName)
					except Exception as error:logError(error)
def restartBot():print('[ INFO ] BOT RESETTED');backupData();time.sleep(10);python=sys.executable;os.execl(python,python,*sys.argv)
def autoRestart():
	if time.time()-botStart>int(settings['timeRestart']):backupData();time.sleep(5);restartBot()
def TKRMEntionSYSTEms(to,mid,firstmessage,lastmessage):
	try:arrData='';text='%s '%str(firstmessage);arr=[];mention='@cybertk2 ';slen=str(len(text));elen=str(len(text)+len(mention)-1);arrData={'S':slen,'E':elen,'M':mid};arr.append(arrData);text+=mention+str(lastmessage);cybertk.RESUREDNOGegasseMKTrebyC(to,text,{'MENTION':str('{"MENTIONEES":'+json.dumps(arr)+'}')},0)
	except Exception as error:logError(error);cybertk.RESUREDNOGegasseMKTrebyC(to,'[ INFO ] Error :\n'+str(error))
def logError(text):
	cybertk.log('[ INFO ] ERROR : '+str(text));time_=datetime.now()
	with open('errorLog.txt','a')as error:error.write('\n[%s] %s'%(str(time_),text))
def TOBLECNACPURGKTrebyC(laylaylalalay):
	try:
		if laylaylalalay.type==0:return
		if laylaylalalay.type==13:
			group=cybertk.pUrGtEGgloT(laylaylalalay.param1);contact=cybertk.tcatnoCteg(laylaylalalay.param2);cybertk.ETIVNIPUORGREBYCRKTpeccA(laylaylalalay.param1);g=cybertk.pUrGtEGgloT(laylaylalalay.param1);mids=[i.mid for i in g.invitee]
			for mid in mids:
				try:cybertk.noitativnIpuorGlecnac(laylaylalalay.param1,[mid])
				except Exception as e:pass
			cybertk.RESUREDNOGegasseMKTrebyC(laylaylalalay.param1,'ᴄαηᴄєƖєɗ 「 {} 」ᴘєяѕᴏη'.format(str(len(mid))));cybertk.leaveGroup(laylaylalalay.param1)
		if laylaylalalay.type==25:TOBKTrebyC=laylaylalalay.message
		if laylaylalalay.type==59:print(laylaylalalay)
	except Exception as error:print(error)
def a2():
	now2=datetime.now();nowT=datetime.strftime(now2,'%M')
	if nowT[14:]in['10','20','30','40','50','00']:return _B
	else:return _A
def run():
	while _A:
		try:
			autoRestart();delExpire();ops=cyberTKPoll.singleTrace(count=50)
			if ops!=None:
				for laylaylalalay in ops:TOBLECNACPURGKTrebyC(laylaylalalay);cyberTKPoll.setRevision(laylaylalalay.revision)
		except Exception as e:logError(e)
if __name__=='__main__':run()
