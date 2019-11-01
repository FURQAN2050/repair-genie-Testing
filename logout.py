class logout:
    def __init__(self,wd):
        self.driver=wd; #wb=webdriver;
        self.logoutButton()
    
    def logoutButton(self):
        logoutButton = self.driver.get('http://testing.repairgenie.net/logout')
        print('Logged out')