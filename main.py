import login #file name
from login import login # and from file name get the class

import driverLogin
from driverLogin import driver

import submitWorkOrder
from submitWorkOrder import submitWorkOrder

import chromeWebDriver
from chromeWebDriver import chromeWebDriver


if __name__ == '__main__':

    cwdObj=chromeWebDriver()        #make class object
    cwdObj.setchromeWebDriver()     #set chromedriver
    webdriver=cwdObj.getWebDriver() #get chrome driver so that the same instance should be send to all files

    stech = login(webdriver,"stech","pass") #USER: Stech login
    swo = submitWorkOrder(webdriver)
    driver = driver(webdriver,"driver","pass") #USER Driver Login
    admin = login(webdriver,"admin","pass") #USER Admin Login
    webdriver.quit()

