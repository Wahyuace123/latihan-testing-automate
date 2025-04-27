from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time


#setup browser 
driver = webdriver.Firefox ()
driver.maximize_window() 

#Open browseer 
driver.get("https://demoqa.com/webtables")

#------ Delete ------
delete_button = driver.find_element(By.XPATH, "///span[@id='delete-record-3']//*[name()='svg']//*[name()='path' and contains(@d,'M864 256H7')]") 
delete_button.click() 

time.sleep(2)
