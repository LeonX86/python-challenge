#http://www.pythonchallenge.com/pc/def/linkedlist.php
from urllib import request
from urllib import parse
from urllib.request import urlopen

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = "12345"

for i in range(400):
    print(" %s%s " % (url, nothing))
    sentence = request.urlopen("%s%s" % (url, nothing)).read().decode('utf-8')
    sentence = sentence.split(' ')
    nothing = sentence[len(sentence)-1]