#fire base tutorial example

from firebase import firebase
firebase = firebase.FirebaseApplication('https://coolscript.firebaseio.com', None)

result = firebase.get('/country', None)
print result

#have to impelement some real life solution script for it
