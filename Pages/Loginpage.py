import pytest
from selenium.webdriver.common.by import By
from pom_youtube.Pages.BasePage import BasePage
from pom_youtube.Config.config import TestData


###import Pages.BasePage import BasePage


class LoginPage(BasePage):
    # """"Locators"""
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign Up")
    LOGIN_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div/div[5]/form/button")
    REMEMBER_ME = (By.CLASS_NAME, 'PrivateSwitchBase-input')

    # """Constructor"""
    def __init(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    # """Page Actions for login"""
    # Page title
    def get_login_page_title(self, title):
        return self.get_title(title)

    # Sign up link verification
    #def is_signup_link_exist(self):
        #return self.is_visible(self.SIGNUP_LINK)

    # Login app
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
