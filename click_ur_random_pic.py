import subprocess
import random
import time
import sys


md=subprocess.Popen(['mkdir pics'],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

while True:
	command='vlc -I dummy v4l2:///dev/video0 --video-filter scene --no-audio --scene-path pics --scene-prefix %s --scene-format png vlc://quit --run-time=1'%(random.randint(1,10000))
	cmd=subprocess.Popen([command],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,bufsize=0)
	try:
		time.sleep(900)
	except:
		sys.exit("Existing")

