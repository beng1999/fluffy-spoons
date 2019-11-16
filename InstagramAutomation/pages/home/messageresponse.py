from base.basepage import BasePage
import time

class MessageResponse(BasePage):

    def __init__(self, driver):
        super().__init__(self)
        self.driver = driver


    #Locators
    _blue_circle_locator = "//*[@id='react-root']/section/div[2]/div/div/div[2]/div/div[2]/a/div/div[3]"
    _notification_alert = "//*[@id='react-root']/section/nav[1]/div/div/header/div/div[2]/a/div"
    #This locator is for the number that pops up on your messages tab to show you that you got a message
    _message_inbox = "//a[@href='/direct/inbox/']"
    #clicks the inbox element on the top right of the screen
    _conversation_list_num = "//*[@id='react-root']/section/div[2]/div/div/div[2]/div/div"
    messageScript = {
        "1": "Hey! Thanks for the DM, this is Rachel. How are you today?!",
        "2": "Awesome :) We reached out to you because we love your feed and would love to collaborate with you! Have you heard of us before?",
        "3": "I will tell you a little about us! We are a brand that started out earlier last year. Our mission is to provide a pristine, protected habitat-sanctuary- for honeybees and other pollinators in order to remove stressors that challenge their ability to heal from disease states that are killing hives worldwide; through our Save The Bee items. A portion of every sale goes to the Save the Honeybee Foundation!",
        "4": "Take a look at our website and let us know what your favorite piece is! www.savethebee.co",
        "5": "Mine is our HoneyComb Bee Pendant Necklace! I would love to create a discount for you. Once you receive the item, we would love to post any picture you send us of you sporting it!",
        "6": "I just made the code 'Savebees' for you! It's good for 25% off your entire order for 24 hours, The following link will automatically apply your custom code! www.savethebee.co/discount/savebees",
        "7": "Together we can help save the bees!"
    }

    def isNotificationThere(self):
        didWeGetMessage = False
        didWeGetMessage = self.elementPresenceCheck(self._notification_alert, byType="xpath")
        print(didWeGetMessage)
        return didWeGetMessage

    def didUserMessage(self):
        if self.isNotificationThere():
            self.elementClick(self._message_inbox, locatorType="xpath")
        else:
            print("No messages have been received")

    def userMessageResponse(self):
        conversations = self.getElementList(self._conversation_list_num, locatorType="xpath")
        listSize = len(conversations) - 1


        print("The size of the list is: " + str(listSize))

        for i in range(2, (listSize + 1)):
            messageIdentifier = "//*[@id='react-root']/section/div[2]/div/div/div[2]/div/div[" + str(i) + "]/a/div/div[3]"
            _dm_conversation = "//span[@id='react-root']/section/div[2]/div/div/div[2]/div/div[" + str(i) + "]"

            doesMessageExist = self.elementPresenceCheck(messageIdentifier, byType="xpath")

            if doesMessageExist:
                self.elementClick(_dm_conversation, locatorType="xpath")


    def instagramResponse(self):
        self.isNotificationThere()