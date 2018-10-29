from selenium import webdriver
import os
from selenium.webdriver.common.by import By

class TestLogin():

    def test(self):
        driverLocation = "C:\\Users\\mkasvi\\Selenium_tutorial\\Libs\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = driverLocation
        driver = webdriver.Ie(driverLocation)
        baseURL = "https://trackwiseqa.pg.com/TrackWiseVAL/"
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)

        overrideLink = driver.find_element(By.ID,"overridelink")
        overrideLink.click()

        handles = driver.window_handles
        for handle in handles:
            print(handle)

        currentHandle = driver.current_window_handle
        print(currentHandle)

PG = TestLogin()
PG.test()


