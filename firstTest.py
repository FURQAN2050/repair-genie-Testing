import unittest
from selenium import webdriver
from login import Login
from logout import logout
from chromeWebDriver import chromeWebDriver
import time
from submitWorkOrder import submitWorkOrder
from driverPickupDevice import driverPickupDevice
from adminWorkshopRecDev import workshopReceiveDevice
from barcode import BarcodeStep
from lenovoClaim import lenovoClaims
from adminDropDevices import adminDropDevices
from driverdropdevices import Driverdropdevices 
# exmaple of inhertance

class Testcases(unittest.TestCase):
  # the self keyword is required in case of class methods
  @classmethod
  def setUpClass(self):
    # Chrome Driver settings
    self.cwdObj=chromeWebDriver()       
    self.cwdObj.setchromeWebDriver() 
    self.webdriver=self.cwdObj.getWebDriver() 
    self.webdriver.maximize_window()
    

  def testSuit1(self):
    #stech registers device and logs out
    stech = Login(webdriver,"stech","pass")
    swo = submitWorkOrder(webdriver)
    uniqueAssetId=swo.getAssetId()
    logout(webdriver)
    
    # #driver picks up device and logs out
    driver = Login(webdriver,"driver","pass")
    pickupDevice = driverPickupDevice(webdriver,uniqueAssetId)
    logout(webdriver)
    
    # admin recieves device fixes it , gives to driver and logs out
    admin = Login(webdriver,"admin","pass")
    workshopRecDev = workshopReceiveDevice(webdriver,uniqueAssetId)
    barcode= BarcodeStep(webdriver,uniqueAssetId)
    lenovoClaim = lenovoClaims(webdriver);
    adminDropDevices = adminDropDevices(webdriver,uniqueAssetId)
    logout(webdriver)
    
    #driver: 
    driver = Login(webdriver,"driver","pass")
    driverdropDevices = Driverdropdevices(webdriver,uniqueAssetId) 
    logout(webdriver)

  @classmethod
  def tearDownClass(self):
    self.webdriver.quit()

