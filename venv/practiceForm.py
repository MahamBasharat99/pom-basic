from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path='/Users/maham-basharat/Downloads/chromedriver')
driver.maximize_window();

firstName= driver.find_element(By.id,"firstName")
firstName.send_keys("Maham")
secondName= driver.find_element(By.id,"lastName")
secondName.send_keys("Basharat")
email= driver.find_element(By.id,"userEmail")
email.send_keys("maham.basharat@invozone.com")
male= driver.find_element(By.id,"gender-radio-1")
male.click()
female= driver.find_element(By.id,"gender-radio-2")
female.click()
other= driver.find_element(By.id,"gender-radio-3")
other.click()
userNum= driver.find_element(By.id,"userNumber")
userNum.send_keys("0308-1584397")
DOB= driver.find_element(By.id,"dateOfBirthInput")
DOB.click()
DOB_Month=driver.find_element(By.CLASS_NAME,"react-datepicker__month-select")
DOB_Month.click()

subjects= driver.find_element(By.id,"dateOfBirthInput")
subjects.send_keys("C")






