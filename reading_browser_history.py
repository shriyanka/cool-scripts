#for ubuntu users
import sys
import subprocess
import requests
import xml.dom.minidom
from xml.dom.minidom import parse, parseString
from xml.dom import minidom
import urlfetch

username="kajal"  #your username here
default_dir_name="hkjxuece.default"  # find the name of your directory and add it here

#path="/home/%s/.mozilla/firefox/%s/"%(username,default_dir_name)
#subprocess.Popen(['sqlite3 places.sqlite "select url from moz_places order by last_visit_date desc limit 30" > ~/Desktop/history.txt'],cwd=path,shell=True)

f=open("/home/%s/Desktop/history.txt"%username)
url=f.read().split('\n')
print url
for u in url:
	resp = urlfetch.fetch(u, method='GET')
	source = resp.content
	print source
	#xml_resp = minidom.parseString(source)
	#print xml_resp
	#body  = xml_resp.getElementsByTagName('body')[0].childNodes[0].data
	#print body
	t=open("/home/%s/Desktop/%s.html"%(username,url.index(u)),'w')
	t.write(source)
	t.close()

#parsing the browsing page one by one



