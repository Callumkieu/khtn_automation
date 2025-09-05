import pytest
from selenium import webdriver
from time import sleep

class browerNavigation:
    @pytest.fixture(scope='class', autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        print(f'The title of web is: {self.driver.title}')

        self.driver.get('https://www.google.com/')
        print(f'The title of web is {self.driver.title}')

        self.driver.back()
        print(f'The title of web is {self.driver.title}')

        self.driver.forward()
        print(f'The title of web is {self.driver.title}')
        yield
        self.driver.quit()