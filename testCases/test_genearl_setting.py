import pytest 
from selenium import webdriver
import sys
sys.path.append('./utilities')
from SettingPage import setting
from test_login import Test_001_Login

from config import driver


# @pytest.fixture()
# def driver():
#     driver = webdriver.Edge()
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     yield driver
#     driver.quit()
    
class Test_002_Setting:
    
   def test_login(self, driver):
        # Instantiate Test_001_Login class
        test_login_instance = Test_001_Login()

        # Call test_login method of Test_001_Login class
        test_login_instance.test_login(driver)
        setpage = setting(driver) 
        # setpage.open_page('http://aigrader.kpitb.online/')  # Fix the URL format
        setpage.sethover_setting()
        
        # setpage.clickLogin()
        
        # time.sleep(15)
        # title = driver.title
        # if title == 'Dashboard | QPG':
        #     print('Login Test Passed')
        #     return  # Exit the function if the condition is met
        # else:
        #     print('Login Test Failed')
        #     assert False, f"Expected title: 'Dashboard | QPG', Actual title: {title}"
        
    