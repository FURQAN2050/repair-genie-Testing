import time

class lenovoClaims:
  def __init__(self,wd):
        self.driver = wd
        self.runTest()


  def runTest(self):
    self.lenovoClaimMenu()
    self.downloadCSV()
    # self.uploadCSV()

  def lenovoClaimMenu(self):
    time.sleep(1)
    self.driver.get("http://testing.repairgenie.net/lenworkorder")
    print("lenovo claim menu opened")

  def downloadCSV(self):
    # click on working 
    time.sleep(1)
    self.driver.find_element_by_tag("a[onclick^='downloadAll([['LenovoClaims-2019-11-01-1-Working.csv','downloadlenovoclaim?file=1&status=Working']]);return false;']").click()

  def uploadCSV(self):
    print("ajdkasjdkl")