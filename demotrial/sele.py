from selenium import webdriver

from time import sleep

web = webdriver.Chrome(r'C:\Users\username\Downloads\chromedriver_win32\chromedriver.exe')
web.get('https://ci.domain.com:8080/')
web_username = web.find_element_by_id('j_username')
web_username.send_keys('user')
web_password = web.find_element_by_name('j_password')
web_password.send_keys('password')
web_submit = web.find_element_by_id('yui-gen1-button')
web_submit.click()
print(web.page_source)

web.close()