import utilities.custom_logger as cl
from pages.home.practiceoperation import Operation
import logging
from base.basepage import BasePage
import time

class Login(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    _log_in_button = "//a[contains(text(),'Log in')]"
    _username = "//input[@name='username']"
    _password = "//input[@name='password']"
    _login_button = "//div[contains(text(), 'Log In')]//parent::button"
    _popup = "//button[contains(text(), 'Not Now')]"

    def clickLogin(self):
        self.elementClick(self._log_in_button, locatorType="xpath")

    def inputUsername(self, username="ben_g99@hotmail.com"):
        first = self.elementPresenceCheck(self._username, byType="xpath")
        if first:
            self.sendKeys(username, self._username, locatorType="xpath")
        else:
            print("Element not found")

    def inputPassword(self, password="yruadreaded12"):
        self.sendKeys(password, self._password, locatorType="xpath")

    def clickLogButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def turnOffPopUp(self):
        self.elementClick(self._popup, locatorType="xpath")

    def initialLogin(self):
        self.clickLogin()
        time.sleep(2)
        self.inputUsername()
        time.sleep(2)
        self.inputPassword()
        time.sleep(2)
        self.clickLogButton()
        time.sleep(2)
        self.turnOffPopUp()
        time.sleep(2)
