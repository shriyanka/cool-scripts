"""
Script: To create a time notifier
Usage: Before begining install pydub and keep a song renamed as ring.mp3 in your root folder containing this script
Tools: Pydub for audio playbacks
"""

from pydub import AudioSegment
from pydub.playback import play
import time

_STOP = True

print "Enter Hour (24-Hour Format)"
hr = input()
print "Enter Minute"
mn = input()

while _STOP:
	now = time.localtime()
	
	if now.tm_hour == hr and now.tm_min == mn:
		song = AudioSegment.from_mp3("ring.mp3")
		song.export("final.wav", format="wav")
		
		#play one minute long only
		sixty_seconds = 60 * 1000
		first_60_seconds = song[:sixty_seconds]		
		play(first_60_seconds)
		_STOP = False
		break
