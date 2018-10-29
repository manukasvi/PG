from selenium import webdriver
from selenium.webdriver.common.by import By
from base.pg_selenium_driver import SeleniumDriver
import os
from selenium.webdriver.support.select import Select
import time

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _login_link = "Login"
    _user_name_field = "tfUserName"
    _password_field = "tfPassword"
    _login_button = "//b[contains(text(),'Log In')]"

    #def getLoginLink(self):
    #    return self.driver.find_element(By.LINK_TEXT, self._login_link)

    #def getEmailField(self):
     #   return self.driver.find_element(By.ID,self._email_field)

    #def getPasswordField(self):
     #   return self.driver.find_element(By.ID,self._password_field)

    #def getLoginButton(self):
     #   return self.driver.find_element(By.ID,self._login_button)

    #def clickLoginLink(self):
    #    self.elementClick(self._login_link, locatorType='link')

    def enterEmail(self, email):
        self.sendKeys(email, self._user_name_field, locatorType="name")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="name")

    def dropDownSelect(self):
        timeZoneElement = self.driver.find_element(By.XPATH, "//select[@name='timezone']")
        sel = Select(timeZoneElement)
        sel.select_by_visible_text("(GMT+05:30) Chennai, Kolkata, Mumbai, New Delhi")
        time.sleep(5)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email, password):
        #self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.dropDownSelect()
        self.clickLoginButton()








