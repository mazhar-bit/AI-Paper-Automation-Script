import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.common.action_chains import ActionChains
import time
from allure_commons.types import AttachmentType

from LoginPage import Login
# from readProperties import ReadConfig
# import sys
# sys.path.append('./utilities')

from config import driver


# @pytest.fixture()
# def driver():
#     driver = webdriver.Edge()
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     yield driver
#     driver.quit()


class Test_001_Login:
    # baseURL = ReadConfig.getApplicationURL()
    # username = ReadConfig.getUsername()
    # password = ReadConfig.getpassword()

  def test_login(self, driver):
        login_page = Login(driver) 
        login_page.open_page('http://aigrader.kpitb.online/')  # Fix the URL format
        login_page.setUsername('admin@admin.com')
        login_page.setpassword('admin@admin.com')
        login_page.clickLogin()
        time.sleep(15)
        driver.implicitly_wait(10)
        # assert True
        title = driver.title
        if title == 'Dashboard | QPG':
            print('Login Test Passed')
            return  # Exit the function if the condition is met
        else:
            print('Login Test Failed')
            assert False, f"Expected title: 'Dashboard | QPG', Actual title: {title}"
            # assertEqual



    # def test_login(self):

        # self.driver = webdriver.Edge()
        # self.driver.get(self.baseURL)
        # self.lp=Login(self.driver)

        # self.lp.textbox_username(self.username)

        # self.lp.text_password(self.password)
        # self.lp.clickLogin()
        # assert True 
        # print('jkk')





# username = driver.find_element(By.NAME, "UserName")
# username.send_keys("1234567890123")
# time.sleep(2)
# userpass = driver.find_element(By.NAME, "Password")
# userpass.send_keys('5SFLRC2N')
# time.sleep(2)
# driver.find_element(By.ID, 'Btn_Login').click()
# time.sleep(4)

