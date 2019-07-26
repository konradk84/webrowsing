import time

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.set_headless()
assert opts.headless

browser = webdriver.Firefox(options=opts)
browser.get("") 

username = browser.find_element_by_name("loginform[login]") 

password = browser.find_element_by_name("loginform[pwd]")
username.send_keys("") 
password.send_keys("") 
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()
time.sleep(5)
#browser.get("")
print(browser.page_source)
browser.quit()
