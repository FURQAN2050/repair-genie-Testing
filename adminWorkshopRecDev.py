# This will log in to the Admin user,
# Open Workshop Receive Device from side Menu,
# Enter values in the AssetID field,
# Submit the values

import login #file name
from login import login


class workshopReceiveDevice:
    def __init__(self,wd):
        self.driver = wd
        self.driver.maximize_window()
        self.driverPickupDeviceTest()

# This controls all the Steps to take place
    def driverPickupDeviceTest(self):
        login(self.driver,"admin","pass")
        self.workshop_ReceiveMenu()
        self.inputAsset()
        self.submitButton()

    def workshop_ReceiveMenu(self):
        pickupMenu = self.driver.get("http://testing.repairgenie.net/workshoprecvdev")
        print('Receive Menu Hit')

    def inputAsset(self):
        self.inputAssetID = self.driver.find_element_by_id('assetid')
        self.inputAssetID.send_keys('12345')
        print('AssetID input successful')

    def submitButton(self):
        self.submitButton = self.driver.find_element_by_xpath('//*[@id="workshoprecv"]/div/div[1]/input[2]')
        self.submitButton.submit() 
        print('Submit success')