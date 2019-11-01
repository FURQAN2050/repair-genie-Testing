from chromeWebDriver import chromeWebDriver
import time
from login import login # and from file name get the class
from submitWorkOrder import submitWorkOrder
from driverPickupDevice import driverPickupDevice
from adminWorkshopRecDev import workshopReceiveDevice
from barcode import BarcodeStep
from lenovoClaim import lenovoClaims
from adminDropDevices import adminDropDevices
from driverdropdevices import Driverdropdevices 
from logout import logout

if __name__ == '__main__':

    # Chrome Driver settings
    cwdObj=chromeWebDriver()        
    cwdObj.setchromeWebDriver()
    webdriver=cwdObj.getWebDriver() 

    #stech registers device and logs out
    stech = login(webdriver,"stech","pass")
    swo = submitWorkOrder(webdriver)
    uniqueAssetId=swo.getAssetId()
    logout(webdriver)
    
    # #driver picks up device and logs out
    driver = login(webdriver,"driver","pass")
    pickupDevice = driverPickupDevice(webdriver,uniqueAssetId)
    logout(webdriver)
    
    # admin recieves device fixes it , gives to driver and logs out
    admin = login(webdriver,"admin","pass")
    workshopRecDev = workshopReceiveDevice(webdriver,uniqueAssetId)
    barcode= BarcodeStep(webdriver,uniqueAssetId)
    lenovoClaim = lenovoClaims(webdriver);
    adminDropDevices = adminDropDevices(webdriver,uniqueAssetId)
    logout(webdriver)
    
    #driver: 
    driver = login(webdriver,"driver","pass")
    driverdropDevices = Driverdropdevices(webdriver,uniqueAssetId) 
    logout(webdriver)
    webdriver.quit()

