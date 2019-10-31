
import time


class logout:
    def __init__(self,wd):
        self.driver=wd; #wb=webdriver;
        self.logoutTest()
    
    def logoutButton(self):
        logoutButton = self.driver.find_element_by_class_name('fa-sign-out')
        logoutButton.click()
        print('Logged out') 


    def logoutTest(self):
        self.logoutButton() 

