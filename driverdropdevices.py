# This will Login into the admin Account,
# Click on Drop Devices menu,
# Select a given Device from the list,
# Enter Asset ID into the field,
# Click Submit
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class Driverdropdevices:
    def __init__(self,wd,uniqueAssetId):
        self.driver = wd;
        self.uniqueAssetId = uniqueAssetId
        self.runTest()

    def runTest(self):
        self.opendropDevicesPage()
        self.selectSchool()
        self.fillTextBoxes()  
        self.signatureConfirmation() 

    def opendropDevicesPage(self):
        self.driver.get('http://testing.repairgenie.net/')
        time.sleep(1)
        self.driver.get("http://testing.repairgenie.net/drop")
        time.sleep(1)
        print('Navigating to Drop Devices on driver page')


    def fillTextBoxes(self):
        self.assetId()
        self.submitButton()

    def selectSchool(self):
        self.driver.get("http://testing.repairgenie.net/dropmeschoolsdev?sch=Academies+of+Loudoun")
        print("driver selected school for device dropoff")
        time.sleep(1)

    def assetId(self):
        assetIdTextBox=self.driver.find_element_by_id('assetid')
        time.sleep(1)
        assetIdTextBox.send_keys(self.uniqueAssetId)
        print('successfully added AssetID')

    def submitButton(self):
        self.submitButton = self.driver.find_element_by_xpath('//*[@id="dropdevs"]/input[2]')
        time.sleep(1)
        self.submitButton.submit() 
        print('Successfully dropped device at school')
        

    # problem
    def signatureConfirmation(self):
        # signature field is now gone and now giving errors
        signature = self.driver.find_element_by_xpath("//*[contains(text(), ' Signature Confirmation ')]")
        signature.click()
        print('Navigated to signature confirmation page')
        reciever = self.driver.find_element_by_name('receiver')
        time.sleep(1)
        reciever.send_keys('School representative')
        time.sleep(1)
        canvas = self.driver.find_element_by_class_name('signature-pad')
        actions = ActionChains(self.driver)
        actions.move_to_element(canvas).perform()
        actions.click_and_hold(canvas).perform()
        actions.move_by_offset(150, 50).perform()
        actions.move_to_element(canvas).perform()
        actions.click_and_hold(canvas).perform()
        actions.move_by_offset(100, 50).perform()
        actions.move_to_element(canvas).perform()
        time.sleep(1)
        submitButton = self.driver.find_element_by_id('Submit')
        submitButton.click()
        print('Successfully confrimed devices were recieved by School representative')

        
