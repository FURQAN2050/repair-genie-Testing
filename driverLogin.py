import time

class driver:
    
    # constructor
    def __init__(self,wd,username,password):
        self.username=username ;
        self.password=password ;
        self.driver=wd; #wb=webdriver;
        self.driver.maximize_window()
        self.loginTest()

    # controls all the tests to be run
    def loginTest(self):
        self.openLoginPage()
        self.addCredentials()
        self.login_button()
        self.logout_button()
    
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

<<<<<<< HEAD
    def loginTest(self):
        self.openLoginPage()
        self.addCredentials()
        self.click_on_button()
        self.logout()

=======
    def addCredentials(self):
        # time.sleep(2)
        username = self.driver.find_element_by_id("username")
        username.send_keys(self.username)
        # time.sleep(2)
        password = self.driver.find_element_by_id("password")
        password.send_keys(self.password)
        print('credentials added successfully')

    def login_button(self):
        # time.sleep(2)
        self.driver.find_element_by_tag_name("button").click();
        print('button clicked successfully')


    def logout_button(self):
        logoutButton = self.driver.find_element_by_class_name('fa-sign-out')
        logoutButton.click()
>>>>>>> origin/arsalanwahidasghar



