from selenium import webdriver
from pages.home.practiceoperation import Operation
from pages.home.login import Login
from pages.home.hashtagcommenting import Hashtag
import time

class Instagram():
    baseURL = "https://www.instagram.com"

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(baseURL)
    ht = Hashtag(driver)
    lg = Login(driver)
    op = Operation(driver)

    def automation(self):
        self.lg.initialLogin()
        self.ht.hashtagSelector()
        #self.op.automationProcess()
        #time.sleep(2)
        #self.driver.quit()


ff = Instagram()
ff.automation()