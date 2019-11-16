from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver
from selenium.webdriver.common.keys import Keys
import time

class AutoFollower(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self)
        self.sl = SeleniumDriver(driver)

    #Locators
    _user_icon = "//div[@role='button'][1]"
    _follow_button = "//button[contains(text(), 'Follow')]"

    def clickFollowButton(self):
        self.elementClick(self._follow_button, locatorType="xpath")

    def FollowUser(self):
        self.clickFollowButton()