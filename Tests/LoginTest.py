from asyncio import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from Pages.Login import Login
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Pages.MainPage import MainPage
import unittest

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test1_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login_button()
        main_page.check_main_page()
        sleep(1)

    def test2_invalid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        login = Login(driver=self.driver)
        login.enter_username("standard_user")
        login.enter_password("secret")
        login.click_login_button()
        sleep(1)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()




