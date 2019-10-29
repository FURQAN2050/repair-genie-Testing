import time

class driver:
    def __init__(self,wd,username,password):
        self.username=username ;
        self.password=password ;
        self.driver=wd; #wb=webdriver;
        self.driver.maximize_window()
        self.loginTest()

    def openLoginPage(self):
        self.driver.get("http://testing.repairgenie.net")
        print('login page succesfully open Driver Case')

    def addCredentials(self):
        time.sleep(2)
        username = self.driver.find_element_by_id("username")
        username.send_keys(self.username)
        time.sleep(2)
        password = self.driver.find_element_by_id("password")
        password.send_keys(self.password)
        print('Driver Credentials Added Successfully')

    def click_on_button(self):
        time.sleep(2)
        self.driver.find_element_by_tag_name("button").click()
        print('Button Clicked Successfully')

    def logout(self):
        time.sleep(10)
        self.driver.get("http://testing.repairgenie.net/logout")
        print('Logout Successful')

    def loginTest(self):
        self.openLoginPage()
        self.addCredentials()
        self.click_on_button()
        self.logout()




