import requests
import time
import json

ACCESS_TOKEN = "your access_token here"

while True:
	t=requests.get("https://api.github.com/notifications?access_token=%s"%(ACCESS_TOKEN))
	content = json.loads(t.content)
 	if content:
 		import os
 		os.system('zenity --info --text="%s"'%(content))
 	
 	time.sleep(1800)
