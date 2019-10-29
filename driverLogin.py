class driver:
    def __init__(self,wd,username,password):
        self.username=username;
        self.password=password;
        self.driver=wd; #wb=webdriver;
        self.driver.maximize_window()
        self.loginTest()

    def openLoginPage(self):
        self.driver.get("http://testing.repairgenie.net")
        print('login page succesfully open')

    def loginTest(self):
        self.openLoginPage()



