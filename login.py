import time

class Login:
    def __init__(self, wd, username, password):
        self.username = username
        self.password = password
        self.driver = wd  # wb=webdriver;
        self.loginTest()

# This controls all the Steps to take place
    def loginTest(self):
        self.openLoginPage()
        self.addCredentials()
        self.login_button_submit()

    def openLoginPage(self):
        self.driver.get("http://testing.repairgenie.net")
        print('Navigated to login page')

    def addCredentials(self):
        time.sleep(2)
        username = self.driver.find_element_by_id("username")
        time.sleep(2)
        username.send_keys(self.username)
        password = self.driver.find_element_by_id("password")
        time.sleep(2)
        password.send_keys(self.password)
        print('credentials added successfully')

    def login_button_submit(self):
        time.sleep(2)
        self.driver.find_element_by_tag_name("button").click()
        print('login button clicked successfully')
        print(self.username, 'logged in successfully')
