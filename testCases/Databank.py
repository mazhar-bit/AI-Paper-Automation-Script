from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class Databank:
    
    def __init__(self,driver):
        self.driver = driver
        self.hover_databank = '/html/body/div/div[1]/ul/li[4]/a/span',
        self.click_question = '//*[@id="general"]/li/a',
        
    def open_url(self,url):
        self.driver.get(url) 
        
    def sethoverdatabank(self):
       databank_hover =self.driver.find_element(By.XPATH, self.hover_databank)
       hover = ActionChains(self.driver).move_to_element(databank_hover)
       hover.perform()
       time.sleep(6)
       self.driver.find_element(By.XPATH,self.click_question).click()
       
    # def setclickquestion(self):
    #     self.driver.find_element(By.XPATH,self.click_question).click()