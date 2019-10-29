class driver:
    
    # constructor
    def __init__(self,wd,username,password):
        self.username=username;
        self.password=password;
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
        print('login page succesfully open')

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



