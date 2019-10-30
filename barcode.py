import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from logout import logout

class BarcodeTest:
    def __init__(self,wd):
        self.driver = wd
        self.runTest()
    
    def runTest(self):
        self.openBarcodePage()
        self.enterBarcodeNumber()
        self.fillTextBoxes()
        self.logout_button()
    
    def openBarcodePage(self):
            time.sleep(2)
            self.driver.get("http://testing.repairgenie.net/barcode")
            print('Admin Dashboard succesfully open')
    

    def enterBarcodeNumber(self):
            time.sleep(2)
            self.driver.find_element(By.ID, "code").click()
            self.driver.find_element(By.ID, "code").send_keys("12345-S")
            self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
            print('Barcode Entered Successfully')
    
    def fillTextBoxes(self):
        self.fillLenovoNotes()
        self.fillSchoolNotes
        self.fillPrivateNotes()
        self.fillRepairProvided()
        self.clickStatusButton()
    
    def fillLenovoNotes(self):
        time.sleep(1)
        self.driver.find_element(By.NAME, "lennotes").click()
        self.driver.find_element(By.NAME, "lennotes").send_keys("Lenovo Notes")
        print('Lenovo Notes filled Successfully')

    def fillSchoolNotes(self):
        time.sleep(1)
        self.driver.find_element(By.ID, "notes").click()
        self.driver.find_element(By.ID, "notes").send_keys("School Notes")
        print('School Notes filled Successfully')
    
    def fillPrivateNotes(self):
        time.sleep(1)
        self.driver.find_element(By.ID, "privnotes").click()
        self.driver.find_element(By.ID, "privnotes").send_keys("Private Notes")
        print('Private Notes filled Successfully')
    
    def fillRepairProvided(self):
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".chosen-choices").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div/div/div/ul/li[7]").click()
        print('full repair info entered Successfully')
    
    def clickStatusButton(self):
        time.sleep(1)
        self.driver.find_element(By.ID, "workingbut").click()        
        print('status button clicked Successfully')


    def logout_button(self):
        logout(self.driver)
        print('logout successfull') 