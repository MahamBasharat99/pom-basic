import pytest


from pom_youtube.Tests.test_base import BaseTest
from pom_youtube.Pages.Loginpage import LoginPage
#issues in this line
from pom_youtube.Config.config import TestData
#import sys
#sys.path.append("/Users/maham-basharat/PycharmProjects/Assignments/pom_youtube")


class TestLogin(BaseTest):
    def test_signup_link_exist(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signup_link_exist()
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
