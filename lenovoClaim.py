import time
import os
from selenium import webdriver;

class lenovoClaims:
  def __init__(self,wd):
        self.driver = wd
        self.runTest()


  def runTest(self):
    self.lenovoClaimMenu()
    self.downloadCSV()
    self.uploadCSV()
    self.submitButton()

  def lenovoClaimMenu(self):
    time.sleep(1)
    self.driver.get("http://testing.repairgenie.net/lenworkorder")
    print("lenovo claim menu opened")

  def downloadCSV(self):
    # click on working 
    time.sleep(1)
    csvFile = self.driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[1]/a')
    csvFile.click()

    print('download csv file ')

  def uploadCSV(self):
    file_button = self.driver.find_element_by_tag_name('input')
    file_button.send_keys(os.path.dirname(os.path.realpath(__file__))+'/LenovoClaims-2019-11-01-1-Working.csv')
    print("CSV Uploaded")

  def submitButton(self):
    self.submitButton = self.driver.find_element_by_id('invoicebut')
    self.submitButton.submit() 
    print('Submit success')



# invoicebut

# chrome_options = self.driver.ChromeOptions()
# prefs = {'download.default_directory' : '/home/huzaifajalali/Desktop'}
# chrome_options.add_experimental_option('prefs', prefs)
# driver = self.driver.Chrome(chrome_options=chrome_options)