

class adminDropDevices:
  def __init__(self,wd):
        self.driver = wd
        self.driver.maximize_window()
        self.runTest()

  def runTest(self):
    self.opendropDevicesPage()
    # self.openSchool()
    self.assetID()
    self.submitButton()


  def opendropDevicesPage(self):
      self.driver.get('http://testing.repairgenie.net/createdrop')
      print('Admin Drop Devices Menu Hit')

  # def openSchool(self):
  #     self.driver.get('http://testing.repairgenie.net/schooldevs?loc=Admin+2nd+Floor')
  #     print('Drop Devices page open succesfully')

  def assetID(self):
        assetIdTextBox=self.driver.find_element_by_name('assetid')
        assetIdTextBox.send_keys('12345')
        print('Asset Id Input Successful')

  def submitButton(self):
        self.submitButton = self.driver.find_element_by_xpath('//*[@id="dropmedev"]/div/div[1]/input[2]')
        self.submitButton.submit() 
        print('Submit success')

