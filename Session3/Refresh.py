from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
print(f'Url of web is {driver.current_url}')

sleep(5)
driver.refresh()
print(f'Url of web is {driver.current_url}')

sleep(5)
driver.quit()