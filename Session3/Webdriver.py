import pytest
from selenium import webdriver
from time import sleep

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    sleep(30)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print(f'The web url is: {driver.current_url}')
    
    request.cls.driver = driver
    yield driver
    driver.quit()