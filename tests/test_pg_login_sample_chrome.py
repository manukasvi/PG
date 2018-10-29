from selenium import webdriver
import os
from selenium.webdriver.common.by import By

from base.pg_selenium_driver import SeleniumDriver
from pages.pg_login import LoginPage
import time
import unittest

class TestLogin(unittest.TestCase):

    def test(self):
        driverLocation = "C:\\Users\\mkasvi\\Selenium_tutorial\\Libs\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseURL = "https://trackwiseqa.pg.com/TrackWiseVAL/"
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)

        #overrideLink = driver.find_element(By.ID,"overridelink")
        #overrideLink.click()

        # parent_Handle = driver.current_window_handle
        # print(parent_Handle)
        # handles = driver.window_handles
        # for handle in handles:
        #     print(handle)

        sd = SeleniumDriver(driver)

        sd.switchWindows()
        time.sleep(5)


        #if handle not in parent_Handle:
        #    driver.switch_to.window(handle)

        #userNameField = driver.find_element(By.NAME,"tfUserName")
        #userNameField.send_keys("eqms_fp3")

        #passwordField = driver.find_element(By.NAME,"tfPassword")
        #passwordField.send_keys("admin")

        #loginButton = driver.find_element(By.XPATH,"//b[contains(text(),'Log In')]")
        #loginButton.click()

        LPP = LoginPage(driver)
        LPP.login("eqmsk_fp1", "admin")

PG = TestLogin()
PG.test()