from selenium import webdriver;

class chromeWebDriver:
    def __init__(self):
        print('Chrome Driver open google chrome')

    def setchromeWebDriver(self):
        # Please added respective path your self
        # on linux in terminal which chromeDriver
        self.wd = webdriver.Chrome()

    def getWebDriver(self):
        return self.wd

