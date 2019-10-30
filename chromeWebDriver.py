from selenium import webdriver;

class chromeWebDriver:
    def __init__(self):
        print('constructor called chrome driver')

    def setchromeWebDriver(self):
        self.wd = webdriver.Chrome('/usr/local/bin/chromedriver')

    def getWebDriver(self):
        return self.wd

