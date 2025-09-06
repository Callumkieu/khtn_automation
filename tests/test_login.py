import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(2)

    # nhập username & password
    username = driver.find_element(By.XPATH, "//input[@name='username']")
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    username.send_keys("Admin")
    password.send_keys("admin123")

    # bấm nút login
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    sleep(5)

    # kiểm tra user dropdown tab xuất hiện sau khi login
    user_dropdown = driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
    assert user_dropdown.is_displayed(), "Login failed! User dropdown not visible."

    driver.quit()