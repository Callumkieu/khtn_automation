import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


def test_login():
        driver = webdriver.Chrome()
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        sleep(2)
        username = driver.find_element(By.XPATH, "//input[@name = 'username']")
        password = driver.find_element(By.XPATH, "//input[@name = 'password']")
        username.send_keys('Admin')
        password.send_keys('admin123')
        sleep(5)
        driver.quit()