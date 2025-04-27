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

#wait page load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "ReactTable"))
)

#---Create data--- 
#Tambah DATA
add_button = driver.find_element(By.ID, "addNewRecordButton")
add_button.click() 

#Tunggu form tampil
WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "firstName"))
)

#isi form 
driver.find_element(By.ID, "firstName").send_keys("Portgas")
driver.find_element(By.ID,"lastName").send_keys("D Ace")
driver.find_element(By.ID,"userEmail").send_keys("Portgasdace@mailsac.coom")
driver.find_element(By.ID,"age"). send_keys("29")
driver.find_element(By.ID, "salary").send_keys("10000000")
driver.find_element(By.ID, "department").send_keys("IT")
driver.find_element(By.ID, "submit"). click()

time.sleep(2)


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
search_box.send_keys("Kierra")

time.sleep(2)

#Verifikasi data
table_data = driver.find_element(By.CLASS_NAME, "rt-td").text
if "Portgas" in table_data: 
    print("Data berhasil ditambahkan")

else : 
    print("Data tidak ditemukan")

#------ Delete ------
delete_button = driver.find_element(By.XPATH, "///span[@id='delete-record-3']//*[name()='svg']//*[name()='path' and contains(@d,'M864 256H7')]") 
delete_button.click() 

time.sleep(2)


