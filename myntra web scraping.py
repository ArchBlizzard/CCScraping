from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from prettytable import PrettyTable

driver = webdriver.Chrome(r"C:\Users\Prabhakar Joshi\Downloads\chromedriver_win32\chromedriver.exe")
url = "https://www.myntra.com/shoes?p="

#Creating a loop to iterate through first 4 pages
for i in range(1, 5):
    print ("Page", i)
    driver.get(url + str(i))
    element = driver.find_elements(By.CLASS_NAME, "product-base")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") 
    parameter = {}
    count = 0

    for shoe in element:
        try:
            lineskip = shoe.text.split('\n')
            rating = lineskip[0]
            name = lineskip[3] + "   " + lineskip[4]
        except:
            count = count + 1
            continue

#Shoes with categories that include the word "Sneakers"
        if "sneaker" in name.lower():    
            parameter[name] = rating
    
    print (count, "products do not return their entries.")

file = open("Dataframe.csv", "w", newline="")  
Writer = csv.writer(file)

# Scraping the "Product name" of the "Sneakers"
A = ["Product Name"] + list(parameter.keys())
# Scraping the "category" of the "Sneakers"
B = ["Category", "Sneakers"]
# Scraping the "User Ratings" given for the "Sneakers"
C = ["User Ratings"] + list(parameter.values())

# Creating a DataFrame for "Sneakers"
dataframe = PrettyTable(["Product Name", "Category", "User Ratings"])

for j in range(0, len(A), 1):
    row = []
    row.append(A[j])
    if j == 0:
        row.append(B[0])
    else:
        row.append(B[1])
    row.append(C[j])

    Writer.writerow(row)
    if j>0:
        dataframe.add_row(row)
    

print ("dataframe created""\n", dataframe)

file.flush()
file.close()
driver.close()
