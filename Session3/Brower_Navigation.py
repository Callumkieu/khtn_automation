import pytest
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
sleep(3)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
print(f'The title of web is {driver.get}')

sleep(3)
driver.get('https://www.google.com/')
print(f'The title of web is {driver.title}')

sleep(3)
driver.back()
print(f'The title of web is {driver.title}')

sleep(3)
driver.forward()
print(f'The title of web is {driver.title}')

driver.quit()