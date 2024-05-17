from selenium.webdriver.common.by import By
from selenium import webdriver
class Login:
    # textbox_username = '/html/body/div/div/div[2]/form/div[1]/div[1]/div/input',
    # text_password = '/html/body/div/div/div[2]/form/div[1]/div[2]/div/input',
    # btn_login = '/html/body/div/div/div[2]/form/button',

    def __init__(self, driver):
       
        self.driver = driver 
        self.textbox_username = '/html/body/div/div/div[2]/form/div[1]/div[1]/div/input',
        self.text_password = '/html/body/div/div/div[2]/form/div[1]/div[2]/div/input',
        self.btn_login = '/html/body/div/div/div[2]/form/button',

    def open_page(self,url):    
        self.driver.get(url)
        

    def setUsername(self,username):
        self.driver.find_element(By.XPATH,*self.textbox_username).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.XPATH,*self.text_password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,*self.btn_login).click()
