from selenium import webdriver
import os
import time

#class with all the functionality bot has#
class InstagramBot:
    #function is called when class is created#
    def __init__(self, username, password):
        """
        Username:str : The Instagram username
        Password:str : The Instagram password

        Stuff to remember:
        Driver: Selenium.webdriver.Chrome : The chromedriver used to control browser actions

        """
        self.username = username
        self.password = password
        self.base_url= 'https://www.instagram.com'
        #in order to log into instagram we're going to need an internet browser#
        #boot up the browser, download chrome driver , chromedriver.exe as initial parameter#
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.login()

    
 #next step is to pass username and password#  #this whole process is through selenium# 
    def login(self):
        #extension method to get from insta-- will open instagram, paste login URL HERE#
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        #finds where username should be put and enters our username#
        
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_name('username').send_keys(self.username)
        
        self.driver.find_element_by_name('password').send_keys(self.password)

        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()
    def nav_user(self, user):
        #each bracket is gonna represent each parameter used
        self.driver.get('{}/{}/'.format(self.base_url, user))

        # self.driver.get('https://instagram.com/user'
    # def follow_user( self,user):
    #     #goes to user page, follow user
    #     self.nav_user(user)

    #     follow_button = self.driver.find_element_by_xpath('//')
    #     follow_button.click()


if __name__ == '__main__':
    #where actual username will go#
    ig_bot = InstagramBot('temp_username', 'temp_password')
    
    ig_bot.nav_user('Instagram')



