import requests
import time
import json

ACCESS_TOKEN = "your_github_acess_token_here"

t=requests.get("https://api.github.com/notifications?access_token=%s"%(ACCESS_TOKEN))
#print json.loads(t.text[1:len(t.text)-1])['subject']['title'] prints  subject
#print json.loads(t.text[1:len(t.text)-1])['subject']['url'] prints url
#print json.loads(t.text[1:len(t.text)-1])['repository']['issues_url'] iterates repo

while True:
	t=requests.get("https://api.github.com/notifications?access_token=%s"%(ACCESS_TOKEN))
	content = json.loads(t.text[1:len(t.text)-1])
	
 	if content:
 		notify = "New Notification \n Notification Title = "+content['subject']['title']+"\n"+" Url = "+content['subject']['url']
 		import os
 		os.system('zenity --info --text="%s"'%(notify))
 		 	
 	time.sleep(1800)
