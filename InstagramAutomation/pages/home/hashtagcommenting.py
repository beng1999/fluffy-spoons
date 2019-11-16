from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver
from pages.home.autofollower import AutoFollower
import time

class Hashtag(BasePage):

    def __init__(self, driver):
        super().__init__(self)
        self.driver = driver
        self.sd = SeleniumDriver(driver)
        self.af = AutoFollower(driver)

    #Locators
    _hashtag_search = ""
    _search_bar = "//input[@type='text']"
    _image_like_button = "/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button"
    _image_comment_locator = "/html/body/div[3]/div[2]/div/article/div[2]/section[3]/div/form/textarea"
    _image_button = "//form[@method='POST']//button"
    _image_exit_button = "//button[@class='ckWGn']"

    def inputSearch(self, search="savethebees"):
        self.sendKeys(search, self._search_bar, locatorType="xpath")

    def clickHashtag(self):
        self._hashtag_search = "savethebees" #All lowercase
        self._search_select = "//a[@href='/explore/tags/" + self._hashtag_search + "/']"
        self.elementClick(self._search_select, locatorType="xpath")

    def likeImage(self):
        self.elementClick(self._image_like_button, locatorType="xpath")

    def exitImageButton(self):
        self.elementClick(self._image_exit_button, locatorType="xpath")

    def commentingOnImages(self, comment="Awesome post!"):
        for i in range(1, 26):
            imageLocator = "//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div["+ str(i) +"]/a"

            isElementPresent = self.elementPresenceCheck(imageLocator, byType="xpath")
            print(isElementPresent)

            self.elementClick(imageLocator, locatorType="xpath")
            time.sleep(2)
            self.elementClick(self._image_comment_locator, locatorType="xpath")
            time.sleep(1)
            self.sendKeys(comment, self._image_comment_locator, locatorType="xpath")
            time.sleep(1)
            self.elementClick(self._image_button, locatorType="xpath")
            time.sleep(1)
            self.likeImage()
            time.sleep(1)
            #self.af.FollowUser()   #Need to download chrome extension
            time.sleep(1)
            self.exitImageButton()
            time.sleep(3)

    def hashtagSelector(self):
        time.sleep(1)
        self.inputSearch()
        time.sleep(4)
        self.clickHashtag()
        time.sleep(2)
        self.commentingOnImages()
        time.sleep(2)
