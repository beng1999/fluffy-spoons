from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver
from selenium.webdriver import ActionChains
import utilities.custom_logger as cl
import logging
import time
from selenium import webdriver

class Operation(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(self)
        self.driver = driver
        self.sl = SeleniumDriver(driver)
        self.actions = ActionChains(driver)

    # Locators
    _search_bar = "//input[@type='text']"
    _search_select = "//a[@href='/guy.cohen_/']/div[@class='z556c']"
    _image_list = "//img[@class='FFVAD']"
    _image_comment_locator = "//textarea[@placeholder='Add a comment…']//parent::form"
    _image_comment = "//textarea[@placeholder='Add a comment…']"
    _image_button = "//form[@class='X7cDz']//button"
    _image_exit_button = "//button[@class='ckWGn']"
    imageLocator = ""

    def inputSearch(self, search = "GuyCohen"):
        self.sendKeys(search, self._search_bar, locatorType="xpath")

    def selectSearch(self):
        self.elementClick(self._search_select, locatorType="xpath")

    def likingImages(self, comment="hello"):
        images = self.getElementList(self._image_list, locatorType="xpath")
        listSize = len(images)

        print("The size of the list is: " + str(listSize))


        for row in range(1, int(listSize/3) + 1):

            for column in range(1, 4):
                # self.imageLocator = "//img[@class='FFVAD'][" + str(i) + "]//parent::div//parent::div//parent::a[1]"
                self.imageLocator = "//*[@id='react-root']/section/main/div/div[2]/article/div/div/div["+str(row)+"]/div["+str(column)+"]/a"

                # self.imageLocator = "//div[@data-ext-skip='1'][" + str(i+1) + "]"
                print(self.imageLocator);
                isElementPresent = self.elementPresenceCheck(self.imageLocator, byType="xpath")
                print(isElementPresent)
                self.elementClick(self.imageLocator, locatorType="xpath")
                time.sleep(2)
                self.elementClick(self._image_comment_locator, locatorType="xpath")
                time.sleep(1)
                self.sendKeys(comment, self._image_comment, locatorType="xpath")
                time.sleep(1)
                self.elementClick(self._image_button, locatorType="xpath")
                time.sleep(1)
                self.elementClick(self._image_exit_button, locatorType="xpath")
                time.sleep(5)
                # baseURL = "https://www.instagram.com/guy.cohen_/"
                # self.driver.get(baseURL)
                time.sleep(5)

    def automationProcess(self):
        self.inputSearch()
        time.sleep(1)
        self.selectSearch()
        time.sleep(1)
        self.likingImages()

