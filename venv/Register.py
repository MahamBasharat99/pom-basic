from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path='/Users/maham-basharat/Downloads/chromedriver')
driver.maximize_window();
driver.get('https://www.theboutiqueasia.com/')

close = driver.find_element(By.CLASS_NAME, 'hide-popup')
close.click();
time.sleep(2)
print("close function is running")
hamburger = driver.find_element(By.CLASS_NAME,'ion-drag')
hamburger.click();
time.sleep(3)
register = driver.find_element(By.ID,'customer_register_link')
register.click();
old_url = driver.current_url
driver.set_page_load_timeout(10)

fname = driver.find_element(By.ID, 'first_name')
fname.send_keys('Maham');
time.sleep(2)
lname = driver.find_element(By.ID, 'last_name')
lname.send_keys('Basharat');
time.sleep(2)
email = driver.find_element(By.ID, 'email')
email.send_keys("maham9@gmail.com");
time.sleep(2)
password = driver.find_element(By.ID, 'create_password')
password.send_keys("123456");
time.sleep(2)

submit = driver.find_element(By.ID, 'button-account')
submit.click()
time.sleep(5)
'''email = driver.find_element(By.ID, 'newsletter-input')
email.send_keys("newspaper@column.us");
time.sleep(2)'''
subscribe = driver.find_element(By.CLASS_NAME, 'button-subscribe')
subscribe.click()
time.sleep(5)

error = driver.find_element(By.CLASS_NAME, 'disc')
error.is_displayed()
print(error.text)
time.sleep(15);

'''recapcha= driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border')
recapcha.click()
time.sleep(2)''' #select images in recapcha


new_url =driver.current_url

