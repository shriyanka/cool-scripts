"""
Script: fire base tutorial example
Usage: Make sure you have firebase application registered
Lib : Find the firebase tar file in libs/ section
Tools: firebase python package
"""

from firebase import firebase
firebase = firebase.FirebaseApplication('https://coolscript.firebaseio.com', None)

result = firebase.get('/country', None)
print result

#have to impelement some real life solution script for it
