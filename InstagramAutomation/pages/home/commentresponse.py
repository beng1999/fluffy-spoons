from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver
import time

class CommentResponse(BasePage):

    def __init__(self, driver):
        super().__init__(self)
        self.driver = driver
        self.sl = SeleniumDriver(driver)

    #Locators
    _comment_input = "//button[contains(text(), 'Reply')]"
    _page_comments = "//span[@aria-label='Like']"
    _comment_message_box = "//textarea[@placeholder='Add a comment…']"
    _user_notification = "//div[@aria-hidden='true']"
    _image_notification = "//*[@id='react-root']/section/main/div/div[1]/div/div[2]/div[3]/a[1]/div/div[1]/img"

    def clickReplyComment(self):
        self.elementClick(self._comment_input, locatorType="xpath")

    def inputComment(self, comment="Thanks!"):
        self.sendKeys(comment, self._comment_message_box, locatorType="xpath")

    def checkForNotification(self):
        notification = self.elementPresenceCheck(self._user_notification, byType="xpath")
        return notification

    def isItPictureNotification(self):
        imageNotification = self.elementPresenceCheck(self._image_notification, byType="xpath")
        return imageNotification

    def commentResponse(self):
        if self.checkForNotification():
                if self.isItPictureNotification():
                    comments = self.getElementList(self._page_comments, locatorType="xpath")
                    listSize = len(comments)

                    print(listSize)

                    for i in range(2, listSize):
                        _comment_like_button = "//span[@aria-label='Like'][" + str(i) + "]//parent::button"

                        self.elementClick(_comment_like_button, locatorType="xpath")
                        self.clickReplyComment()
                        self.inputComment()
