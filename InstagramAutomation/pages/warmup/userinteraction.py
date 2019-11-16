from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver
import time
import random

class UserActivity(BasePage):

    def __init__(self, driver):
        super().__init__(self)
        self.driver = driver
        self.sd = SeleniumDriver(driver)

    #Locators
    _like_button = "//span[@aria-label='Like']" #Selects all the like buttons on the page with [1] being the top one
    #To be able to click the button: //span[@aria-label='Like'][1]//parent::button
    _comment_button = "//span[@aria-label='Comment']" #Selects all the comment buttons on the page with [1] being the top one
    #To be able to click the button: //span[@aria-label='Comment'][1]//parent::button
    _stories_icon = "//*[@id='react-root']/section/main/section/div[1]/div[1]/div[3]/div/div[1]" #Shows all the stories at the top of the page
    #This above one is what I found for desktop
    _stories_icon_mobile = "//span[@role='link']//parent::div//parent::button" #Selects all the stories seen on the page
    totalLikableElements = 0
    totalCommentElements = 0
    totalStories = 0
    _comment_input_box = "//textarea[@placeholder='Add a comment…']"
    _post_comment_button = "//button[contains(text(), 'Post')]"
    _back_button = "//svg[@aria-label='Back']//parent::span//parent::a"
    _home_button = "//span[@aria-label='Home']"

    #  5 images are found on the page when you first open Instagram on mobile #
    #  5 image likes, 5 image comments, and 11 stories are found #

    def scrollDown(self):
        self.webScroll("down")

    def scrollUp(self):
        self.webScroll()

    def setUp(self):
        self.totalLikableElements = self.getElementList(self._like_button, locatorType="xpath")
        self.totalCommentElements = self.getElementList(self._comment_button, locatorType="xpath")
        self.totalStories = self.getElementList(self._stories_icon_mobile, locatorType="xpath")

        #This means I don't need to scroll anywhere for the first 5 images and 11 stories
        #Not confirmed: Not sure how the stories work - If i finish the 11 do more pop up?
        #If you scroll down to the 5th image, then more images popup with the correct index
        #So if I click on the 5th image like, and refresh the search for new images then it
        #will appear correctly and I could continue liking and commenting on images

    def UserImageLikes(self):
        for i in range(1, self.totalLikeableElements + 1):
            _click_like_button = "//span[@aria-label='Like'][" + str(i) + "]//parent::button"
            self.elementClick(_click_like_button, locatorType="xpath")

    def UserCommenting(self):
        comments = {"0": "Awesome post!", "1": "Love your feed! You got great posts", "2": "Awesome post :)"}
        for i in range(1, self.totalCommentElements + 1):
            _click_comment_button = "//span[@aria-label='Comment'][" + str(i) + "]//parent::button"
            self.elementClick(_click_comment_button, locatorType="xpath")
            self.elementClick(self._comment_input_box, locatorType="xpath")
            self.sendKeys(comments[random.randint(0,4)], self._comment_input_box, locatorType="xpath")
            self.elementClick(self._post_comment_button, locatorType="xpath")
            self.elementClick(self._back_button, locatorType="xpath")

    def UserViewStories(self):
        doneWithStories = False
        _click_first_story = "//span[@role='link'][2]//parent::div//parent::button"
        self.elementClick(_click_first_story, locatorType="xpath")
        while doneWithStories == False:
            time.sleep(6)
            doneWithStories = self.elementPresenceCheck(self._home_button, byType="xpath")








