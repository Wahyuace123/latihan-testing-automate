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

#------ READ ------
search_box = driver.find_element(By.ID, "searchBox")
search_box.send_keys("Portgas")

time.sleep(2)

#Verifikasi data
table_data = driver.find_element(By.CLASS_NAME, "rt-td").text
if "Portgas" in table_data: 
    print("Data berhasil ditambahkan")

else : 
    print("Data tidak ditemukan")
