from selenium import webdriver

from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path='/Users/maham-basharat/Downloads/chromedriver')
driver.maximize_window();


driver.get('https://www.theboutiqueasia.com/')
fname = driver.find_element(By.ID, 'customer_email')
fname.send_keys("newspaper@column.us");

'''driver.find_element(By.ID, "customer_email").send_keys(xyz)'''
email= driver.find_element(By.ID, 'customer_email')
email.send_keys(mahambasharat8@gmail.com)
password = driver.find_element(By.ID, 'customer_password')
password.send_keys("123456");
login = driver.find_element(By.CLASS_NAME, 'submit')
login.click()
time.sleep(2)
'''old_url = driver.current_url
driver.set_page_load_timeout(10)
fname = driver.find_element(By.ID, 'email')
fname.send_keys("newspaper@column.us");
lname = driver.find_element(By.ID, 'password')
lname.send_keys("1111111");
email = driver.find_element(By.ID, 'submit')
email.click()
time.sleep(2)
error = driver.find_element(By.ID, 'error')
error.is_displayed()
print(error.text)
time.sleep(15);

new_url =driver.current_url'''



driver.close()







