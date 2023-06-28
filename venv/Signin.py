from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path='/Users/maham-basharat/Downloads/chromedriver')
driver.maximize_window();

url='https://www.theboutiqueasia.com/'
driver.get(url)

close = driver.find_element(By.CLASS_NAME, 'hide-popup')
close.click();
time.sleep(2)
hamburger = driver.find_element(By.CLASS_NAME,'ion-drag')
hamburger.click();
time.sleep(3)
signin = driver.find_element(By.ID,'customer_login_link')
signin.click();
old_url = driver.current_url
driver.set_page_load_timeout(10)

email = driver.find_element(By.ID, 'customer_email')
email.send_keys("newspaper@column.us");
time.sleep(2)

password = driver.find_element(By.ID, 'customer_password')
password.send_keys(" uiop ");
time.sleep(2)

submit = driver.find_element(By.XPATH,'//input[@type="submit"]')
submit.click()
time.sleep(5)

error = driver.find_element(By.CLASS_NAME, 'disc')
error.is_displayed()
print(error.text)
time.sleep(15);

new_url =driver.current_url


# email.send_keys("moeed.fayyaz@invozone.com");
#
# gender1 = driver.find_element(By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[1]/label')
# gender1.click()
# mobile = driver.find_element(By.ID, 'userNumber')
# mobile.send_keys("3434687700")
# dob = driver.find_element(By.ID, 'dateOfBirthInput')
# dob.click()
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, '[class$="month-select"]').click()
# driver.find_element(By.CSS_SELECTOR, 'option[value="10"]').click()
# driver.find_element(By.CSS_SELECTOR, '[class$="year-select"]').click()
# driver.find_element(By.CSS_SELECTOR, 'option[value="1992"]').click()
# driver.find_element(By.CSS_SELECTOR, '[class$="026"]').click()
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
# s = driver.find_element(By.CSS_SELECTOR, '[id="subjectsInput"]')
# s.send_keys("English")
# s.send_keys(Keys.RETURN)
# time.sleep(1)


# driver.find_element(By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[1]/label').click()
#
# # upload = driver.find_element(By.ID, 'uploadPicture')
# # upload.send_keys('/Users/moeed-invozone/Downloads/test.png')
#
# address = driver.find_element(By.ID, 'currentAddress')
# address.send_keys("V-123")
# time.sleep(1)
#
# state = driver.find_element(By.CSS_SELECTOR, '[class$="css-2b097c-container"][id="state"]')
# state.click()
# menu = driver.find_element(By.XPATH, '//*[@id="state"]/div[2]')
# menu.find_element(By.ID, 'react-select-3-option-0').click()
#
# city = driver.find_element(By.CSS_SELECTOR, '[class$="css-2b097c-container"][id="city"]')
# city.click()
# menu = driver.find_element(By.XPATH, '//*[@id="city"]/div[2]')
# menu.find_element(By.CSS_SELECTOR, '[class$="css-1n7v3ny-option"]').click()
#
# time.sleep(1)
#
# submit = driver.find_element(By.ID, 'submit')
# submit.click()
#
# time.sleep(2)
# #close = driver.find_element(By.ID, 'closeLargeModal') //Click to close
# #close.click()

driver.close()










