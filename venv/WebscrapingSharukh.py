import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

import unittest
import requests
import os


s = Service('/Users/maham-basharat/Downloads/chromedriver')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(10)



driver.get("https://cityclerk.lacity.org/lacityclerkconnect/index.cfm?fa=ccfi.viewrecord&cfnumber=17-0893")

list_of_pdf= []
my_text=''
for i in range(2, 38):
    new_row = driver.find_elements(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/div/div[6]/div[2]/table/tbody/tr[' + str(i) + ']')
    for j in range(1,4):
        if j ==3:
            try:
                link = driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div/div/div/div[6]/div[2]/table/tbody/tr" + "[" + str(i) + "]" + "/td[" + str(j) + "]")
                #link.click()
                image = driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div/div/div/div[6]/div[2]/table/tbody/tr"+ "[" + str(i) + "]" + "/td[" + str(j) + "]"+"/img")
                driver.execute_script("arguments[0].click();", image)
                time.sleep(1)
                row=driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/table/tbody/tr/td/div')
                print(len(row))
                for r in range (1,len(row)+1):
                    if r >= 2:
                        elemelt = driver.find_element(By.XPATH,
                                                      "/html/body/div[1]/div[2]/table/tbody/tr/td/div[" + str(
                                                          r) + "]/table/tbody/tr/td[1]/a")
                        print(elemelt.text)
                        print(elemelt.get_attribute('href'))
                        continue
                    elemelt= driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/table/tbody/tr/td/div/table/tbody/tr/td["+str(r)+"]/a")
                    '/html/body/div[1]/div[2]/table/tbody/tr/td/div[2]/table/tbody/tr/td[1]/a'
                    print(elemelt.get_attribute('href'))
                    time.sleep(1)




                link_text=link.text
            except NoSuchElementException:
                pass
        else:
            continue



print(len(list_of_pdf))

driver.quit()




if __name__ == "__main__":
    unittest.main()







