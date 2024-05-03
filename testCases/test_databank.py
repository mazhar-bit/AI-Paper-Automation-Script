from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import driver
from test_login import Test_001_Login
from Databank import Databank
import time

class Test_003_databank:
    
    def test_databank(self,driver):
        
        login_test = Test_001_Login()  
        
        login_test.test_login(driver)
        
        # set the page of databank into test cases
        
        setpage = Databank(driver)
        
        setpage.sethoverdatabank()
        time.sleep(5)
        
        setpage.setclickquestion()
        
