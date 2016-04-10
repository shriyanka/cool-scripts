"""
Project: Sentiment Analysis using Background History data
Module 1: Reading the User History table and storing the links in History.txt
Module 2: Opening each urls and fetching the raw text seperatly in each file as __url__name.txt
Tools: Python, Urlfetch, Subprocess-for making comand line request
Date: 4th Dec, 2015 
"""

import sys
import subprocess
import requests
import urlfetch

username="kajal"
default_dir_name="hkjxuece.default"

path="/home/%s/.mozilla/firefox/%s/"%(username,default_dir_name)
subprocess.Popen(['sqlite3 places.sqlite "select url from moz_places order by last_visit_date desc limit 30" > ~/Desktop/history.txt'],cwd=path,shell=True)

f=open("/home/%s/Desktop/history.txt"%username)
url=f.read().split('\n')
print url
for u in url:
	resp = urlfetch.fetch(u, method='GET')
	source = resp.content
	print source
	t=open("/home/%s/Desktop/%s.html"%(username,url.index(u)),'w')
	t.write(source)
	t.close()
