import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class BarcodeStep1:
    def __init__(self,wd,uniqueAssetId):
        self.driver = wd
        self.uniqueAssetId=uniqueAssetId;
        self.runTest()
    
    def runTest(self):
        self.openBarcodePage()
        self.enterBarcodeNumber()
        self.fillTextBoxes()
        self.selectRepairComponents()
        self.clickWorkingStatusButton()

        # barcode step2
        self.enterBarcodeNumber()
        self.fillRepairProvided()
        self.clickFixedStautsButton()
    
    def openBarcodePage(self):
            time.sleep(2)
            self.driver.get("http://testing.repairgenie.net/barcode")
            print('Admin Dashboard succesfully open')
    

    def enterBarcodeNumber(self):
            time.sleep(2)
            self.driver.find_element(By.ID, "code").click()
            self.driver.find_element(By.ID, "code").send_keys(self.uniqueAssetId)
            # this picks up the submit button
            self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
            print('Barcode Entered Successfully')
    
    def fillTextBoxes(self):
        self.fillLenovoNotes()
        self.fillSchoolNotes
        self.fillPrivateNotes()
        # self.fillRepairProvided()
        
    def fillLenovoNotes(self):
        time.sleep(1)
        self.driver.find_element(By.NAME, "lennotes").clear()
        self.driver.find_element(By.NAME, "lennotes").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "lennotes").send_keys("Lenovo Notes")
        print('Lenovo Notes filled Successfully')

    def fillSchoolNotes(self):
        time.sleep(1)
        self.driver.find_element(By.ID, "notes").clear()
        self.driver.find_element(By.ID, "notes").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "notes").send_keys("School Notes")
        print('School Notes filled Successfully')
    
    def fillPrivateNotes(self):
        time.sleep(1)
        self.driver.find_element(By.ID, "privnotes").clear()
        self.driver.find_element(By.ID, "privnotes").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "privnotes").send_keys("Private Notes")
        print('Private Notes filled Successfully')
    

    def selectRepairComponents(self):
        time.sleep(1)
        self.driver.find_element(By.ID,"38parCheck").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"25parCheck").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"27parCheck").click()
    
    def clickWorkingStatusButton(self):
        time.sleep(2)
        self.driver.find_element(By.ID, "workingbut").click()        
        print('working status button clicked')

    # USE THIS CODE AGAIN in the right order this should not be here right now
    def fillRepairProvided(self):
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".chosen-choices").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div/div/div/ul/li[7]").click()
        print('full repair info entered Successfully')

    def clickFixedStautsButton(self):
        time.sleep(1)
        self.driver.find_element(By.ID,"fixbut").click()
        print('fixed status button clicked')