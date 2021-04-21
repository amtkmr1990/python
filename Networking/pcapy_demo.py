# import requests
# import pprint
# r = requests.get('https://msn.com')
# pprint.pprint(r.headers)

import urllib.request
header = urllib.request.urlopen('http://msn.com').info()
print(str(header))