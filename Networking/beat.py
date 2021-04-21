import requests

payload = {
    'username' : 'user',
    'password' : 'password',
    #'redirect_uri': 'https://beatext.domain.com/nagiosxi/views/index.php'

}
login_url = 'https://beatext.domain.com/nagiosxi/login.php'
#req_url = 'https://beatext.domain.com/nagiosxi/views/'
# with requests.Session() as session:
#     session.verify = False
#     post = session.post(login_url, data=payload)
#     print(post)
#     r = session.get(req_url,verify=False)
#     #print(r.text)   #or whatever else you want to do with the request data!
# # r = requests.get('https://beatext.domain.com/nagiosxi/views/',data, verify=False )
r = requests.post('https://beatext.domain.com/nagiosxi/views/index.php', data=payload, verify=False)
with open('REQ2.HTML', 'wb') as f:
      f.write(r.content)

