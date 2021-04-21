import requests
from bs4 import BeautifulSoup
r = requests.get('http://www.infinitskills.com')
h = r.content
print(h)
b = BeautifulSoup(h, "html.parser")
a = b.find_all('a')
print(a)
# for i in a:
#      print(i.get('href'))

