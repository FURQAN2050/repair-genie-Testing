from selenium import webdriver;

class chromeWebDriver:
    def __init__(self):
        print('')

    def setchromeWebDriver(self):
        # Please added respective path your self
        # on linux in terminal which chromeDriver
        self.wd = webdriver.Chrome()
        print('Chrome Driver install location found')

    def getWebDriver(self):
        print('Chrome Driver opened Google chrome')
        return self.wd

