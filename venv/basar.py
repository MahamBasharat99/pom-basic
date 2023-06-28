import os
from selenium import webdriver
from fpdf import FPDF
from selenium.webdriver.common.by import By
import time



pdf=FPDF()
pdf.output("hello world")
driver = webdriver.Chrome(executable_path='/Users/maham-basharat/Downloads/chromedriver')
driver.maximize_window();
driver.get('https://admin-sell-it-marketplace.invo.zone')
time.sleep(10)
#driver.set_page_load_timeout(15)
new_url = driver.current_url
print(new_url)
#Admin login in test cases
if new_url == "https://admin-sell-it-marketplace.invo.zone/sign-in":
    email = driver.find_element(By.XPATH,'//*[@name="email"]')
    email.send_keys("admin@gmail.com")
    password = driver.find_element(By.XPATH, '//*[@type="password"]')
    password.send_keys("admin123e")
    sign_in =driver.find_element(By.XPATH,'//*[@class="button SignIn_button__1SRQa"]')

    time.sleep(2)
    sign_in.click()

    text =driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div/div[1]/div[2]/div')
    print(text.text)
    #message = driver.find_element(By.XPATH,"//*[@class='Toastify']")
    #how to read toastify error message?
    time.sleep(8)
    #print(message)
    #message.is_displayed()
    #print(message.text) #ask???
    new_url2 =driver.current_url
    print("new url "+ new_url2)
    if new_url2 =="https://admin-sell-it-marketplace.invo.zone/":
       #driver.execute_script("alert('Welcome via Selenium')")
       print("Sign in successfully")
#Relative path Case
       # if we use element it just return only one element but if we use elements then it would return all childs in array[]
       #getParentElement1 = driver.find_element(By.XPATH, '//*[@class="Overview_nav__3Ijus"]')
       #print(getParentElement1.text)






       drawerItems= driver.find_elements(By.XPATH, '//*[@class="Sidebar_menu__1ziVd"]')
       print("hey",len(drawerItems))
       dataDrawerLength= drawerItems[0].get_attribute('innerHTML').count('<a class="Sidebar_item__24pNX"')
       print("Elements of parent drawer item",dataDrawerLength)
       for y in range(1,dataDrawerLength + 1):
        dataDrawerItems=driver.find_element(By.XPATH, '//*[@class="Sidebar_menu__1ziVd"]/a[' + str(y) +']')
        print("Items",dataDrawerItems.text)
        if dataDrawerItems.text == "Home":
            print("Home Page Results")
            #getParentElement = driver.find_elements(By.XPATH, '//*[@class="Overview_nav__3Ijus"]')
            #fetchParentElementData = getParentElement[0].get_attribute('innerHTML').count('<div class="Overview_outerDiv__jLbP3">')
            #print("Parent inner elements", fetchParentElementData)
            #for x in range(1, fetchParentElementData + 1):
                #print(driver.find_element(By.XPATH, '//div[@class="Overview_nav__3Ijus"]/div[' + str(x) + ']').text)

        elif dataDrawerItems.text == "Transactions":
            print("Transactions Page Results")
            #get = driver.find_element(By.XPATH, '//*[@class="Page_inner__2ZM6W"]')
            #print("Transaction",get.text)


        elif dataDrawerItems.text == "Users":
            print("Users Page Results")
            #get = driver.find_element(By.XPATH, '//*[@class="Page_container__1JOhd"]')
            #print("Users",get.text)

        elif dataDrawerItems.text == "Listings":
            print("Listings Page Results")
            listing = driver.find_element(By.XPATH,'//*[@href="/listings"]')
            listing.click();
            get2 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[5]/div')
            print('Listings',driver.find_element(By.XPATH,'/html/body/div/div[2]/div[5]/div').text)
        elif dataDrawerItems.text=="Shippings":
            print(dataDrawerItems)
            print("Shiping Page Results")
            get = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[5]/div/div[2]/div/div/div[2]/div/div')
            print("shipping",get.text)

        else:
            print("No item found")

#using Absolute path that starting from root
       #checkLength = driver.find_elements(By.XPATH, '//*[@id="root"]/div[2]/div[5]/div/div[2]/div/div/div[2]/div')
       #print("Check inner div ", type(checkLength))
       #print("parent", len(checkLength))
       #print("46", checkLength[0].get_attribute('innerHTML').count('<div class="Overview_outerDiv__jLbP3">'))
       #print("46", checkLength[0].get_attribute('innerHTML').count('<div class="Overview_outerDiv__jLbP3">'))
       #print("Check length", checkLength)
       #print("Check inner div " + str(checkLength))


#Direct Child checking
       #checkLengthchilds = driver.find_elements(By.XPATH, '//*[@id="root"]/div[2]/div[5]/div/div[2]/div/div/div[2]/div//child::*')
       #print("debug",len(checkLengthchilds))
       #print("Childs path extend",checkLengthchilds)
       #checkLengthchilds = driver.find_elements(By.XPATH, '//div[@class="Overview_nav__3Ijus"]')
       #for i in checkLengthchilds:
           #print("for loop in parent internal divs",i.get_attribute('innerHTML'))
       #print(checkLength[0].find_elements_by_tag_name('div'))



       #print(listingParent.text[0][1])
       #print(listingParent[0])


    #print("Driver info",driver)
    #driver.switch_to.window(driver.window_handles[0])
    #driver.close()
    #driver.quit()


else:
    print("We are on Main Screen")
    #driver.close()
    #driver.quit()