# http://www.pythonchallenge.com/pc/def/equality.html
from urllib.request import urlopen
import re

url = 'http://www.pythonchallenge.com/pc/def/equality.html'

response = urlopen(url)
html = response.read()
text = str(html)
pattern = re.compile(r'<!--(.+)-->')
result = pattern.findall(text)
result = result[0]

letter = re.compile(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
letters = letter.findall(result)
msg = ''.join(letters)
print(msg)