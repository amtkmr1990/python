from robobrowser import RoboBrowser
br = RoboBrowser()
br.open('https://domain.com/zabbix',verify=False)
f = br.get_form()
try:
    f['name'].value = 'username'
    f['password'].value = 'password'
except Exception:
    print()
br.submit_form(f)
print(br.parsed)