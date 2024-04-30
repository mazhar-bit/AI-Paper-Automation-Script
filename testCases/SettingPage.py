from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class setting:

    def __init__(self,driver):
        # webbrowser = webdriver.Edge()
        self.driver = driver
        self.hover_setting = '/html/body/div/div[1]/ul/li[3]/a',
        self.hover_discipline = '//*[@id="general"]/li[1]/a',
        self.hover_term='//*[@id="general"]/li[2]/a',
        self.hover_class='//*[@id="general"]/li[3]/a',
        self.hover_subject='//*[@id="general"]/li[4]/a',
        self.hover_chapter='//*[@id="general"]/li[5]/a',

    def open_page(self,url):
        self.driver.get(url)

    def sethover_setting(self):
        element_to_hover_over = self.driver.find_element(By.XPATH, *self.hover_setting)
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()
        time.sleep(5)
        # disciplainehover = self.driver.find_element(By.XPATH,*self.hover_discipline)
        # hover = ActionChains(self.driver).move_to_element(disciplainehover)
        # hover.perform()
        
        
    def sethover_discipline(self):
        disciplainehover = self.driver.find_element(By.XPATH,*self.hover_discipline)
        hover = ActionChains(self.driver).move_to_element(disciplainehover)
        hover.perform()
        time.sleep(2)
        self.driver.find_element(By.XPATH,*self.hover_discipline).click()
        # hoverclick.click()   
       
        
    def sethover_term(self):
        termhiver = self.driver.find_element(By.XPATH,self.hover_term)
        hover = ActionChains(self.driver).move_to_element(termhiver)
        hover.perform()
        self.driver.find_element(By.XPATH,self.hover_term).click()
            



