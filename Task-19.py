from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set path to Chromedriver exe
serv_obj = Service(r"C:\Drivers_Selenium\chromedriver-win64\chromedriver.exe")

# Create a instance of the Chromedriver
driver = webdriver.Chrome(service=serv_obj)

# Maximize browser window
driver.maximize_window()

# time delay
time.sleep(3)

# Navigate given URL
driver.get('https://www.saucedemo.com/')

# Find username and password and login
driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')

# time delay
time.sleep(3)

driver.find_element(By.ID, 'login-button').click()

# Get the title of webpage
title = driver.title
print(f'Title of the webpage: {title}')

# Get current URL of the webpage
current_url = driver.current_url
print(f'Current URL of the webpage: {current_url}')

# Extract entire contents of webpage and save to a text file
webpage_content = driver.page_source

with open('webpage_task_11.txt', 'w') as file:
    file.write(webpage_content)

# time delay
time.sleep(4)

# Close browser window
driver.close()
