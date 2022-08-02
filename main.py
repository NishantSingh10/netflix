from ast import Pass
from lib2to3.pgen2 import driver
from requests import options
from selenium import webdriver
import time
from Credential import LoginId, Password

driver = webdriver.Chrome()
driver.get("https://netflix.com")
time.sleep(5)
SignIn= driver.find_element("xpath",'/html/body/div[1]/div/div/div/div/div/div[1]/div/a').click()
time.sleep(5)

email=driver.find_element("xpath",'/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div/div/label/input')
email.send_keys(LoginId)

passw=driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div[1]/div/label/input')
passw.send_keys(Password)

signin=driver.find_element("xpath",'/html/body/div[1]/div/div[3]/div/div/div[1]/form/button').click()
time.sleep(5)


driver.get("https://www.netflix.com/in/title/81597698")
time.sleep(5)
play=driver.find_element("xpath", '/html/body/div[1]/div/div[2]/section[3]/div[2]/ul/li/div/button/span[2]').click()
time.sleep(5)

des=driver.find_element("xpath", '/html/body/div[1]/div/div[2]/section[1]/div[1]/div[1]/div[2]/div/div[2]/div[1]').screenshot()
time.sleep(5)

