import requests
import csv
from simple-salesforce import Salesforce
import pandas as pd


sf = Salesforce(username=email.com, password=your_password, security_token = your_token)


login_data = {'username': your_username, 'password': your_password_plus_your_token}


with requests.session() as s:
    d = s.get("https://your_instance.salesforce.com/{}?export=1&enc=UTF-8&xf=csv".format(reportid), headers=sf.headers, cookies={'sid': sf.session_id})