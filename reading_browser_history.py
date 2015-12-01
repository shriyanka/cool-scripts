#for ubuntu users
import sys
import subprocess
import requests

username="kajal"  #your username here
default_dir_name="hkjxuece.default"  # find the name of your directory and add it here

path="/home/%s/.mozilla/firefox/%s/"%(username,default_dir_name)
subprocess.Popen(['sqlite3 places.sqlite "select url from moz_places order by last_visit_date desc limit 30" > ~/Desktop/history.txt'],cwd=path,shell=True)


f=open("/home/%s/Desktop/history.txt"%username)
url=f.read().split('\n')
print url
for u in url:
	source=requests.get(u)
	#print source.content
	t=open("/home/%s/Desktop/%s.html"%(username,url.index(u)),'w')
	t.write(source.content)
	t.close()




