from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""Parent class of all pages """
'''''contain methods and utilities'''


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.ID, by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.ID, by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.ID, by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.ID, by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
