import time
from selenium.webdriver.support.ui import Select
class submitWorkOrder:
    def __init__(self,wd):
        self.driver = wd;
        self.runTest()

    def openSubmitWorkOrderPage(self):
        time.sleep(2);
        self.driver.get("http://testing.repairgenie.net/addsingledevice")
        print('submit Work Order Page succesfully open')

    def fillTextBoxes(self):
        self.assetId()
        self.incidentId()
        self.deviceType()
        self.periferal()
        self.serial()
        self.logout_button()


    def runTest(self):
        self.openSubmitWorkOrderPage();
        self.fillTextBoxes()

    def assetId(self):
        time.sleep(2)
        assetIdTextBox=self.driver.find_element_by_name("msb")
        assetIdTextBox.send_keys("1000")
        print('asset Id added')

    def incidentId(self):
        time.sleep(2)
        incidentIdTextBox = self.driver.find_element_by_name("incid")
        incidentIdTextBox.send_keys("1000")
        print('incident Id added')

    def deviceType(self):
        time.sleep(2)
        # select = Select(self.driver.find_element_by_xpath("//*[@id='adddevform']/div[3]/select"))
        select = Select(self.driver.find_element_by_name('devtype'))
        # select.select_by_value("11e")
        select.select_by_index(2)
        print('deviceType Added')

    def periferal(self):
        time.sleep(2)
        select = Select(self.driver.find_element_by_xpath("//*[@id='adddevform']/div[4]/select"))
        select.select_by_index(2)
        print('peripheral Added')

    def serial(self):
        time.sleep(2)
        serialIdTextBox = self.driver.find_element_by_name("serial")
        serialIdTextBox.send_keys("500")
        print('serial No added')

    def logout_button(self):
        logoutButton = self.driver.find_element_by_class_name('fa-sign-out')
        logoutButton.click()
