from login import login # and from file name get the class

from submitWorkOrder import submitWorkOrder

from dropDevices import dropDevices 

from barcode import BarcodeTest

from chromeWebDriver import chromeWebDriver

from driverPickupDevice import driverPickupDevice

from adminWorkshopRecDev import workshopReceiveDevice

from adminDropDevices import adminDropDevices

from logout import logout

if __name__ == '__main__':

    cwdObj=chromeWebDriver()        #make class object
    cwdObj.setchromeWebDriver()     #set chromedriver
    webdriver=cwdObj.getWebDriver() #get chrome driver so that the same instance should be send to all files

    stech = login(webdriver,"stech","pass") #USER: Stech login
    swo = submitWorkOrder(webdriver)
    logout(webdriver)
    driver = login(webdriver,"driver","pass") #USER Driver Login
    pickupDevice = driverPickupDevice(webdriver) #(webdriver, schoolname, assetID)
    logout(webdriver)
    admin = login(webdriver,"admin","pass") #USER Admin Login
    workshopRecDev = workshopReceiveDevice(webdriver) #USER Admin Workshop Receive Device
    barcodeObj=BarcodeTest(webdriver)


    # working on drop devices from admin to driver (huzaifa)
    adminDropDevices = adminDropDevices(webdriver)
    logout(webdriver)
    
    driver = login(webdriver,"driver","pass") #USER Driver Login
    dropDevices = dropDevices(webdriver) #USER Driver drop device 
    logout(webdriver)
    webdriver.quit()

