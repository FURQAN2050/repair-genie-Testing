

class adminDropDevices:
  def __init__(self,wd,uniqueAssetId):
        self.driver = wd
        self.uniqueAssetId=uniqueAssetId
        self.runTest()

  def runTest(self):
    self.opendropDevicesPage()
    #self.openSchool()
    self.assetID()
    self.submitButton()


  def opendropDevicesPage(self):
      self.driver.get('http://testing.repairgenie.net/createdrop')
      print('Navigated to Admin Drop Devices menu')

  def openSchool(self):
      self.driver.get('schooldevs?loc=Academies+of+Loudoun')
      print('Selected Academies of Loudoun')

  def assetID(self):
        assetIdTextBox=self.driver.find_element_by_name('assetid')
        assetIdTextBox.send_keys(self.uniqueAssetId)
        print('AssetId Input Successful')

  def submitButton(self):
        self.submitButton = self.driver.find_element_by_xpath('//*[@id="dropmedev"]/div/div[1]/input[2]')
        self.submitButton.submit() 
        print('Sucessfully dropped device to driver for school delivery')

