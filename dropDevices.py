# This will Login into the admin Account,
# Click on Drop Devices menu,
# Select a given Device from the list,
# Enter Asset ID into the field,
# Click Submit
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



class dropDevices:
    def __init__(self,wd):
        self.driver = wd;
        self.runTest()

    def opendropDevicesPage(self):
        time.sleep(2);
        self.driver.get("http://testing.repairgenie.net/createdrop")
        print('Drop Devices page open succesfully')


    def fillTextBoxes(self):
        self.assetId()
        self.submitButton()



    def runTest(self):
        self.opendropDevicesPage();
        self.fillTextBoxes()   


    def assetId(self):
        time.sleep(2)
        assetIdTextBox=self.driver.find_element_by_name("assetid")
        assetIdTextBox.send_keys("10000")
        print('asset Id added')


    def submitButton(self):
        self.submitButton = self.driver.find_element_by_xpath('//*[@id="dropmedev"]/div/div[1]/input[2]')
        self.submitButton.submit() 
        print('Submit success')

