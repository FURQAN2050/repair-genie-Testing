from selenium import webdriver;
import os

class chromeWebDriver:
    def __init__(self):
        print('Chrome Driver open google chrome')

    def setchromeWebDriver(self):
        print(os.path.dirname(os.path.realpath(__file__)))
        chrome_options = webdriver.ChromeOptions()
        prefs = {'download.default_directory' : os.path.dirname(os.path.realpath(__file__))}
        chrome_options.add_experimental_option('prefs', prefs)
        self.wd = webdriver.Chrome(chrome_options=chrome_options)
        # self.wd = webdriver.Chrome('/usr/bin/chromedriver')

    def getWebDriver(self):
        return self.wd

