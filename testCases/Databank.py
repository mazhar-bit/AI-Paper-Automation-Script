from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Databank:
    
    def __init__(self,driver):
        self.driver = driver
        self.hover_databank = '/html/body/div/div[1]/ul/li[4]/a/span',
        self.click_question = '//*[@id="general"]/li/a',
        
    def open_url(self,url):
        self.driver.get(url) 