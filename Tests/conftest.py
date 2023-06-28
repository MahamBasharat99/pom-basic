import pytest
from selenium import webdriver

# Under project, we use folder in import section

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
#import sys
#print(sys.path)


from pom_youtube.Config.config import TestData


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def init_driver(request):
    web_driver = webdriver.Chrome(executable_path='/Users/maham-basharat/Downloads/chromedriver')
    web_driver.maximize_window();
    web_driver.close()


