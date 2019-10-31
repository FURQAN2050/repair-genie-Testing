from login import login # and from file name get the class

from submitWorkOrder import submitWorkOrder

from dropDevices import dropDevices 

from barcode import BarcodeTest

from chromeWebDriver import chromeWebDriver

from driverPickupDevice import driverPickupDevice

from adminWorkshopRecDev import workshopReceiveDevice

from adminDropDevices import adminDropDevices

from logout import logout

import time

if __name__ == '__main__':

    cwdObj=chromeWebDriver()        #make class object
    cwdObj.setchromeWebDriver()     #set chromedriver
    webdriver=cwdObj.getWebDriver() #get chrome driver so that the same instance should be send to all files

    stech = login(webdriver,"stech","pass") #USER: Stech login
    swo = submitWorkOrder(webdriver)
    uniqueAssetId=swo.getAssetId()
    time.sleep(3)
    logout(webdriver)

    time.sleep(4)
    
    
    driver = login(webdriver,"driver","pass") #USER Driver Login
    pickupDevice = driverPickupDevice(webdriver,uniqueAssetId) #(webdriver, schoolname, assetID)
    logout(webdriver)
    admin = login(webdriver,"admin","pass") #USER Admin Login
    workshopRecDev = workshopReceiveDevice(webdriver,uniqueAssetId+"-S") #USER Admin Workshop Receive Device
    barcodeObj=BarcodeTest(webdriver,uniqueAssetId)


    # working on drop devices from admin to driver (huzaifa)
    adminDropDevices = adminDropDevices(webdriver,uniqueAssetId)
    logout(webdriver)
    
    # driver = login(webdriver,"driver","pass") #USER Driver Login
    # dropDevices = dropDevices(webdriver) #USER Driver drop device 
    # logout(webdriver)
    webdriver.quit()

