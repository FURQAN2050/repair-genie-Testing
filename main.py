import login #file name
from login import login # and from file name get the class

import submitWorkOrder
from submitWorkOrder import submitWorkOrder


import dropDevices
from dropDevices import dropDevices 

from barcode import BarcodeTest

import chromeWebDriver
from chromeWebDriver import chromeWebDriver

import driverPickupDevice
from driverPickupDevice import driverPickupDevice

import adminWorkshopRecDev
from adminWorkshopRecDev import workshopReceiveDevice



if __name__ == '__main__':

    cwdObj=chromeWebDriver()        #make class object
    cwdObj.setchromeWebDriver()     #set chromedriver
    webdriver=cwdObj.getWebDriver() #get chrome driver so that the same instance should be send to all files

    stech = login(webdriver,"stech","pass") #USER: Stech login
    swo = submitWorkOrder(webdriver)
    driver = login(webdriver,"driver","pass") #USER Driver Login
    pickupDevice = driverPickupDevice(webdriver) #(webdriver, schoolname, assetID)
    admin = login(webdriver,"admin","pass") #USER Admin Login
    workshopRecDev = workshopReceiveDevice(webdriver) #USER Admin Workshop Receive Device
    barcodeObj=BarcodeTest(webdriver)
    webdriver.quit()

