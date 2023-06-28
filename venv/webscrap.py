import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='/Users/maham-basharat/Downloads/chromedriver')
driver.maximize_window();
driver.get('https://admin-sell-it-marketplace.invo.zone')
# driver.set_page_load_timeout(15)
time.sleep(5)

new_url = driver.current_url
print(new_url)
# Admin login in test cases
if new_url == "https://admin-sell-it-marketplace.invo.zone/sign-in":
    email = driver.find_element(By.XPATH, '//*[@name="email"]')
    email.send_keys("emi@basar.io")
    password = driver.find_element(By.XPATH, '//*[@type="password"]')
    password.send_keys("vGgsPdjJyE4PjeY")
    sign_in = driver.find_element(By.XPATH, '//*[@class="button SignIn_button__1SRQa"]')
    sign_in.click()
    # message = driver.find_element(By.XPATH,"//*[@class='Toastify']")
    # how to read toastify error message?
    time.sleep(8)
    # print(message)
    # message.is_displayed()
    # print(message.text) #ask???
    new_url2 = driver.current_url
    print("new url " + new_url2)
    if new_url2 == "https://admin-sell-it-marketplace.invo.zone/":
        # driver.execute_script("alert('Welcome via Selenium')")
        print("Sign in successfully")

        # Relative path Case
        # if we use element it just return only one element but if we use elements then it would return all childs in array[]
        # getParentElement1 = driver.find_element(By.XPATH, '//*[@class="Overview_nav__3Ijus"]')
        # print(getParentElement1.text)
        getParentElement = driver.find_elements(By.XPATH, '//*[@class="Overview_nav__3Ijus"]')
        # print(driver.find_element(By.XPATH, '//div[@class="Overview_nav__3Ijus"]/div[1]').text)
        print("Find Exactly what parent have in elements", getParentElement)
        print("Find parent element Length", len(getParentElement))
        fetchParentElementData = getParentElement[0].get_attribute('innerHTML').count(
            '<div class="Overview_outerDiv__jLbP3">')
        print("Parent inner elements", fetchParentElementData)
        for x in range(1, fetchParentElementData + 1):
            print("***Div{}*** ".format(x))
            print(driver.find_element(By.XPATH, '//div[@class="Overview_nav__3Ijus"]/div[' + str(x) + ']').text)

    print("Driver info", driver)
    # driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.quit()


else:
    print("We are on Main Screen")
    driver.close()
    driver.quit()