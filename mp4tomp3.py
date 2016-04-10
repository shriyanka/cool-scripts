from pydub import AudioSegment
from pydub.playback import play
import time

_STOP = True

song = AudioSegment.from_mp3("song.mp4")
song.export("song2.mp3", format="mp3")

sixty_seconds = 60 * 1000
first_60_seconds = song[:sixty_seconds]		
play(first_60_seconds)