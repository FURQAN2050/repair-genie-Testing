import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logout
from logout import logout


class dropDevices:
    def __init__(self,wd):
        self.driver = wd;
        self.runTest()
        #self.driver.implicitly_wait(3)


    def opendropDevicesPage(self):
        time.sleep(2);
        self.driver.find_element_by_link_text('Drop Devices').click()
        #self.driver.get("http://testing.repairgenie.net/createdrop")
        print('Drop Devices Page succesfully open')

    def fillTextBoxes(self):
        self.assetId()
        self.sumbit()

    def runTest(self):
        self.opendropDevicesPage();
        self.fillTextBoxes()

    def assetId(self):
        time.sleep(2)
        assetIdTextBox=self.driver.find_element_by_name("assetid")
        assetIdTextBox.send_keys("10000")
        print('asset Id added')

    def submit(self):
        time.sleep(3)
        submitButton = self.driver.find_element_by_name("").click()
        submitButton.click()
        print('sumbit button clicked successfully') 


