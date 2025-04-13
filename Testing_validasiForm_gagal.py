from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time 

service = Service("/usr/local/bin/geckodriver")
driver = webdriver.Firefox(service=service)
wait = WebDriverWait(driver, 10)

#GeneradeData 
username ="Dummytest" #--> username
email = "" #--> dikosongkan 
password = "TestPassword123" 

#Open w3school
driver.get("https://profile.w3schools.com/login") 
driver.maximize_window() 

#Input username & Login 
email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
email_input.send_keys(email)

#Input password
password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password_input.send_keys(password)


#Button submit
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_btn.click()

#TUnggu dan tutup browser

time.sleep(3)
driver.quit()