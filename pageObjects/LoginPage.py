import time
from locators import *
from wrappers.wrappers import enter_using_xpath, click_using_xpath


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self, url):
        self.driver.get(url)
        time.sleep(5)

    def enter_username(self, username):
        enter_using_xpath(self.driver, username_textbox, username, "Entered username")

    def enter_password(self, password):
        enter_using_xpath(self.driver, password_textbox, password, "Entered password")

    def click_login(self):
        click_using_xpath(self.driver, login_button, "Clicked on login button")
