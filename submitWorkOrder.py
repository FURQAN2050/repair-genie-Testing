import time

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
        print('device Type Added')


