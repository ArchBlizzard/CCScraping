import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"C:\Users\Prabhakar Joshi\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.flipkart.com/")
product = driver.find_element(By.CLASS_NAME,"_3704LK")
product.send_keys("sneakers")
search = driver.find_element(By.CLASS_NAME, "_34RNph")
search.click()
name_sks =[]
category_sks = []
userratings_sks = []
for page in range(0,4):
    # Scraping the "names" of the 'Sneakers'
    name_tags = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for name in name_tags[0:100]:
        name_sks.append(name.text)
    
    # Scraping the "category" of the 'Sneakers'
    category_tags = driver.find_elements(By.XPATH, '//div[@class="_30jeq3"]')
    for category in category_tags[0:100]:
        category_sks.append(category.text)
        
    # Scraping the "User Ratings" given for the 'Sneakers'
    userratings_tags = driver.find_elements(By.XPATH, '//div[@class="_3Ay6Sb"]//span')
    for userratings in userratings_tags[0:100]:
        userratings_sks.append(userratings.text)
    
    # Moving the next page of 'Sneakers'
    next_page = driver.find_element(By.XPATH, '//a[@class="_1LKTO3"]//span')
    next_page.click()
    time.sleep(2)
    
print(len(name_sks),len(category_sks),len(userratings_sks))

# Creating a DataFrame for 'Sneakers'
sneakers_df = pd.DataFrame({'Name':name_sks[0:100], "Category":category_sks[0:100], "User_ratings":userrartings_sks[0:100]})
sneakers_df
