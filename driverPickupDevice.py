# This will Login into the Driver Account,
# Click on Pick-Up Device menu,
# Select a given School from the list,
# Enter Asset ID into the field,
# Click Submit


from login import login
import time

class driverPickupDevice:
    def __init__(self,wd,uniqueAssetId):
        self.driver = wd
        self.uniqueAssetId=uniqueAssetId
        self.driver.maximize_window()
        self.driverPickupDeviceTest()

# This controls all the Steps to take place
    def driverPickupDeviceTest(self):
        self.pickupDeviceMenu()
        self.selectSchool()
        self.inputAsset()
        self.submitButton()

    def pickupDeviceMenu(self):
        pickupMenu = self.driver.get("http://testing.repairgenie.net/pickup")
        # pickupMenu.click()
        print('Navigating to pick up device menu')

    def selectSchool(self):
        self.driver.get("http://testing.repairgenie.net/pickupschoolsdev?sch=Academies+of+Loudoun")
        # selectSchoolName.click()
        print('School selected')

    def inputAsset(self):
        self.inputAssetID = self.driver.find_element_by_id('assetid')
        time.sleep(2)
        self.inputAssetID.send_keys(self.uniqueAssetId)
        print('AssetID input successful')

    def submitButton(self):
        self.submitButton = self.driver.find_element_by_xpath('//*[@id="pickupdevs"]/div/div[1]/input[2]')
        self.submitButton.submit() 
        print('AssetID submit successfull')
        print('driver picked up device')


