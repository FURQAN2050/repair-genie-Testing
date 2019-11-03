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
    stech = Login(self.webdriver,"stech","pass")
    swo = submitWorkOrder(self.webdriver)
    uniqueAssetId=swo.getAssetId()
    logout(self.webdriver)
    
    # #driver picks up device and logs out
    driver = Login(self.webdriver,"driver","pass")
    pickupDevice = driverPickupDevice(self.webdriver,uniqueAssetId)
    logout(self.webdriver)
    
    # admin recieves device fixes it , gives to driver and logs out
    admin = Login(self.webdriver,"admin","pass")
    workshopRecDev = workshopReceiveDevice(self.webdriver,uniqueAssetId)
    barcode= BarcodeStep(self.webdriver,uniqueAssetId)
    lenovoClaim = lenovoClaims(self.webdriver);
    adminDropDevices = adminDropDevices(self.webdriver,uniqueAssetId)
    logout(self.webdriver)
    
    #driver: 
    driver = Login(self.webdriver,"driver","pass")
    driverdropDevices = Driverdropdevices(self.webdriver,uniqueAssetId) 
    logout(self.webdriver)

  @classmethod
  def tearDownClass(self):
    self.webdriver.quit()

