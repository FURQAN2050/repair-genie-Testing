
import time


class login:
    def __init__(self,wd,username,password):
        self.username=username
        self.password=password
        self.driver=wd #wb=webdriver;
        self.driver.maximize_window()
        self.loginTest()

# This controls all the Steps to take place
    def loginTest(self):
        self.openLoginPage()
        self.addCredentials()
        self.login_button_submit()

    def openLoginPage(self):
        self.driver.get("http://testing.repairgenie.net")
        print('login page succesfully open')
    
    def addCredentials(self):
        time.sleep(1)
        username = self.driver.find_element_by_id("username")
        username.send_keys(self.username)
        time.sleep(1)
        password = self.driver.find_element_by_id("password")
        password.send_keys(self.password)
        print('credentials added successfully')

    def login_button_submit(self):
        time.sleep(2)
        self.driver.find_element_by_tag_name("button").click();
        print('Login Button Clicked Successfully')