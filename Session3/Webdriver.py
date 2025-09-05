import pytest
from selenium import webdriver
from time import sleep

# @pytest.fixture(scope="class")
# def setup(request):
driver = webdriver.Chrome()
    # driver.maximize_window()
    # sleep(3)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(f'The web url is: {driver.current_url}')
sleep(10)
    
request.cls.driver = driver
    # yield driver
driver.quit()