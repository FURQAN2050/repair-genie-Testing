import time

from selenium.webdriver.support.ui import Select

import random


class submitWorkOrder:   
    def __init__(self,wd):
        self.driver = wd;
        self.runTest()
        #self.driver.implicitly_wait(3)
    

    def openSubmitWorkOrderPage(self):
        time.sleep(2);
        self.driver.get("http://testing.repairgenie.net/addsingledevice")
        print('submit Work Order Page succesfully open')

    def fillTextBoxes(self):
        self.assetId()
        self.incidentId()
        self.deviceType()
        #self.periferal()
        self.serial()
        self.nameLabel()
        self.pickUp()
        self.schoolRefID()
        self.Issue()
        #self.reset()
        self.submit()
        

    def runTest(self):
        self.openSubmitWorkOrderPage();
        self.fillTextBoxes()

    def assetId(self):
        time.sleep(2)
        assetIdTextBox=self.driver.find_element_by_name("msb")
        self.uniqueAssetId=random.randint(10000, 15000)
        self.uniqueAssetId=str(self.uniqueAssetId)
        assetIdTextBox.send_keys(self.uniqueAssetId)
        print('asset Id added')

    def incidentId(self):
        time.sleep(2)
        incidentIdTextBox = self.driver.find_element_by_name("incid")
        incidentIdTextBox.send_keys("10000")
        print('incident Id added')

    def deviceType(self):
        time.sleep(2)
        #select = Select(self.driver.find_element_by_xpath("//*[@id='adddevform']/div[3]/select"))
        select = Select(self.driver.find_element_by_name('devtype'))
        select.select_by_index(2)
        print('deviceType Added')

    def periferal(self):
        time.sleep(2)
        #select = Select(self.driver.find_element_by_xpath("//*[@id='adddevform']/div[4]/select"))
        select = Select(self.driver.find_element_by_name('peripheral'))
        select.select_by_index(2)
        print('peripheral Added')

    def serial(self):
        time.sleep(2)
        serialIdTextBox = self.driver.find_element_by_name("serial")
        serialIdTextBox.send_keys("10000")
        print('serial No added')

    def nameLabel(self):
        time.sleep(2)
        name_LabelIdTextBox = self.driver.find_element_by_name("namelabel")
        name_LabelIdTextBox.send_keys("Test Submission")
        print('name Label added')

    def pickUp(self):
        time.sleep(2)
        select = Select(self.driver.find_element_by_xpath("//*[@id='adddevform']/div[7]/select"))
        select.select_by_index(1)
        print('pickUP and Drop Location Added')  

    def schoolRefID(self):
        time.sleep(2)
        schoolRefIDIdTextBox = self.driver.find_element_by_name("schoolrefid")
        schoolRefIDIdTextBox.send_keys("10000")
        print('School Ref ID added')


    def Issue(self):
        time.sleep(2)
        IssueIdTextBox = self.driver.find_element_by_name("issue")
        IssueIdTextBox.send_keys("A test submission by Abid to go through the workflow.")
        print('Issue added')


    def reset(self):
        time.sleep(3)
        restButton = self.driver.find_element_by_class_name('btn-default')
        restButton.click()
        print('reset button clicked successfully')

    def submit(self):
        time.sleep(3)
        submitButton = self.driver.find_element_by_class_name('btn-success')
        submitButton.click()
        print('submit button clicked successfully') 

    def getAssetId(self):
        return self.uniqueAssetId;   

