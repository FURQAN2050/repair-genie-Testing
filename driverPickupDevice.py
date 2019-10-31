# This will Login into the Driver Account,
# Click on Pick-Up Device menu,
# Select a given School from the list,
# Enter Asset ID into the field,
# Click Submit


from login import login


class driverPickupDevice:
    def __init__(self,wd,uniqueAssetId): #,school_name,assetID
        # self.school_name = school_name
        # self.assetID = assetID
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
        print('Pick-Up Device Menu Hit')

    def selectSchool(self):
        self.driver.get("http://testing.repairgenie.net/pickupschoolsdev?sch=Admin+2nd+Floor")
        # selectSchoolName.click()
        print('School Name Hit')

    def inputAsset(self):
        self.inputAssetID = self.driver.find_element_by_id('assetid')
        self.inputAssetID.send_keys(self.uniqueAssetId)
        print('AssetID input successful')

    def submitButton(self):
        self.submitButton = self.driver.find_element_by_xpath('//*[@id="pickupdevs"]/div/div[1]/input[2]')
        self.submitButton.submit() 
        print('Submit success')


