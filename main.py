from chromeWebDriver import chromeWebDriver
import time
from login import login # and from file name get the class
from submitWorkOrder import submitWorkOrder
from driverPickupDevice import driverPickupDevice
from adminWorkshopRecDev import workshopReceiveDevice
from barcodeStep1 import BarcodeStep1
from lenovoClaim import lenovoClaims
from barcodeStep2 import BarcodeStep2
from adminDropDevices import adminDropDevices
from driverdropdevices import Driverdropdevices 
from logout import logout

if __name__ == '__main__':

    # Chrome Driver settings
    cwdObj=chromeWebDriver()        
    cwdObj.setchromeWebDriver()
    webdriver=cwdObj.getWebDriver() 

    # #stech registers device and logs out
    stech = login(webdriver,"stech","pass") 
    swo = submitWorkOrder(webdriver)
    uniqueAssetId=swo.getAssetId()
    logout(webdriver)
    
    # #driver picks up device and logs out
    driver = login(webdriver,"driver","pass")
    pickupDevice = driverPickupDevice(webdriver,uniqueAssetId)
    logout(webdriver)
    
    # admin recieves device fixes it , gives to driver and logs out
    admin = login(webdriver,"admin","pass") #USER Admin Login
    workshopRecDev = workshopReceiveDevice(webdriver,uniqueAssetId) #USER Admin Workshop Receive Device
    barcodeStep1= BarcodeStep1(webdriver,uniqueAssetId)
    lenovoClaim = lenovoClaims(webdriver) 
    barcodeStep2 = BarcodeStep2(webdriver,uniqueAssetId)
    adminDropDevices = adminDropDevices(webdriver,uniqueAssetId)
    logout(webdriver)
    
    # #driver: 
    driver = login(webdriver,"driver","pass") #USER Driver Login
    driverdropDevices = Driverdropdevices(webdriver,'13134') #USER Driver drop device 
    logout(webdriver)
    webdriver.quit()

