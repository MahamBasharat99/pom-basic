# command and forward slash is used for comment multiple lines

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path='/Users/maham-basharat/Downloads/chromedriver')
driver.maximize_window();

url='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
driver.get(url)

email = driver.find_element(By.CLASS_NAME, 'oxd-label')
email.send_keys("Admin");
time.sleep(2)

password = driver.find_element(By.ID, 'customer_password')
password.send_keys("admin123");
time.sleep(2)

submit = driver.find_element(By.XPATH,'//input[@type="submit"]')
submit.click()
time.sleep(5)

error = driver.find_element(By.CLASS_NAME, 'disc')
error.is_displayed()
print(error.text)
time.sleep(15);

new_url =driver.current_url
