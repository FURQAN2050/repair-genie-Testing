import login #file name
from login import login # and from file name get the class

import submitWorkOrder
from submitWorkOrder import submitWorkOrder

import chromeWebDriver
from chromeWebDriver import chromeWebDriver


if __name__ == '__main__':

    cwdObj=chromeWebDriver()        #make class object
    cwdObj.setchromeWebDriver()     #set chromedriver
    webdriver=cwdObj.getWebDriver() #get chrome driver so that the same instance should be send to all files

    loginObj=login(webdriver,"stech","pass")
    swo=submitWorkOrder(webdriver)

