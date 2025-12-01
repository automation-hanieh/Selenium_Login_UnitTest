from selenium.webdriver.common.by import By
from Locators import *


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def check_main_page(self):
         self.driver.find_element(By.XPATH, product_xpath)


