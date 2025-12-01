from selenium.webdriver.common.by import By
from Locators import *


class Login:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, password_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, login_button_id).click()
