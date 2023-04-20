#coding = utf-8
#Coded by : Aqib Ali ID
# Dont Forget To Give me Credit 
#Fork me On Github to show your Love
#Facebook : facebook.com/dilute840

import re,requests,os,sys,time
from time import sleep as sp
import rich
from rich import print
from rich.panel import Panel as pn
def clear():
	os.system('clear')


def logo():
	print(pn(pn('''\t##     ##    ###    
\t##     ##   ## ##   
\t##     ##  ##   ##  
\t##     ## ##     ## 
\t##     ## ######### 
\t##     ## ##     ## 
\t #######  ##     ##
--------------------------------------------------
  [•] Random Working User Agent Generator Online
--------------------------------------------------
  [•] Version 1.2 [Makes Easy To Add Ua]
  [•] Tool Coded  : Aqib X Siam
  [•] Aqib Github : Dcofficial
  [•] Siam Github : SIAM-AHMED-CP
  [•] [bold cyan]Show your Love by Forking Our Repository[/bold cyan]
  [•][bold green] One Single Vulnerability All An Attacker Needs[/bold green]
--------------------------------------------------''',width=60,title=" • [bold green] [underline]Jalwa Hai Hamara Yahan [/underline][/bold green] • ",style="bold white"),title=" • [underline][bold white]Instgram ID - @CodesByAqib[/bold white] • ",style="bold cyan",width=60))


ses = requests.Session()
class iAmUserAgent:
	def __init__(self):
		os.system("xdg-open https://chat.whatsapp.com/GzUiQ51HrLpDzebhrmsgYh")
		self.url = 'https://user-agents.net/random'
		self.dalvikurl = "https://user-agents.net/applications/dalvik"
		self.total = []
		self.mylimit = 100
		self.mysave = "/sdcard/aqib_ua.txt"
	def imDilute(self):
		clear()
		logo()
		print(pn("[bold white] [01] Generate Random User Agents \n [02] Generare Dalvik User Agents",style="bold cyan",width=60))
		im_option = input(' [•] Choose : ')
		if im_option == "1":
			self.iAmRandomUserAgent()
		elif im_option == "2":
			self.iAmDalvikUserAgent()
	
	def iAmRandomUserAgent(self):
		clear()
		logo()
		try:
			limit = int(input("  [•] Put UA Limit : "))
		except(ValueError):
			limit = 100
		try:
			sav = input("  [•] Save Path :- ")
			if sav =="":
				sav = self.mysave
		except(FileNotFoundError):
			sav = self.mysave
		self.get_RandomUa(limit,sav)
		print(f"\n  [•] Proccess Has Been Completed \n  [•] Your File Saved in : {sav} ")
		print(51*'-')
		input(" [•] Press Enter To Go Main Menu")
		self.imDilute()
	def get_RandomUa(self,limit,sav):
		data = {
		'limit':f"{limit}",
		'action':'generate'
		}
		iAmWriting = open(sav,"a")
		iAmWriting.write(f'aqib_random_ua = random.choice([')
		try:
			iAmGettingData = ses.post(url=self.url,data=data).text
			for wAreRandomUserAgents in re.findall('href\=\"/string/(.*?)">(.*?)<',iAmGettingData):
				self.total.append(wAreRandomUserAgents[1])
				iAmWriting.write(f'"{wAreRandomUserAgents[1]}",')
				sys.stdout.write(f"\r  [•] Getting UA: [{len(self.total)}] ");sys.stdout.flush();sp(0.009)
		except ConnectionError:
			print(f" [•] Please Check Your Internet Connection ..")
			exit()
		iAmWriting.write("])")

	def iAmDalvikUserAgent(self):
		clear()
		logo()
		try:
			sav = input("  [•] Save Path :- ")
			if sav =="":
				sav = self.mysave
		except(FileNotFoundError):
			sav = self.mysave
		self.get_DalvikUa(sav)
		print(f"\n  [•] Proccess Has Been Completed \n  [•] Your File Saved in : {sav} ")
		print(51*'-')
		input(" [•] Press Enter To Go Main Menu")
		self.imDilute()
	def get_DalvikUa(self,sav):
		iAmWriting = open(sav,"a")
		iAmWriting.write(f'aqib_dalvik_ua = random.choice([')
		try:
			iAmGettingDalvikData = ses.get(self.dalvikurl).text
			for weAreDalvikFamily in re.findall("href\=\'/string/(.*?)'>(.*?)<",iAmGettingDalvikData):
				self.total.append(weAreDalvikFamily[1])
				iAmWriting.write(f'"{weAreDalvikFamily[1]}",')
			#print(weAreDalvikFamily[1])
				sys.stdout.write(f"\r  [•] Getting UA: [{len(self.total)}] ");sys.stdout.flush();sp(0.009)
		except ConnectionError:
			print(f" [•] Please Check Your Internet Connection ..")
			exit()
		iAmWriting.write("])")



if __name__=="__main__":
	#print(" Read The Complete Code and Remove # from line 124 to Run \n  Sirf Script use krny k liye nh hti Learn b krni hti h ")
	iAmUserAgent().imDilute()