from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
import time 
import os 

#Browser firefox 
service = Service("/usr/local/bin/geckodriver")
driver = webdriver.Firefox(service=service)
wait = WebDriverWait(driver, 10) 

#buka website 
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window() 

#regist 
wait.until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys("Portgas")
driver.find_element(By.ID, "lastName").send_keys("Ace") 
driver.find_element(By.ID, "userEmail").send_keys("ace@example.com") 
driver.find_element(By.XPATH, "//label[@for='gender-radio-1']").click() 
driver.find_element(By.ID, "userNumber").send_keys("081234567890") 

#Tanggal lahir 
dob_field =driver.find_element(By.ID, "dateOfBirthInput") 
dob_field.click()
dob_field.send_keys(Keys.CONTROL + "a")
dob_field.send_keys("12 Apr 1995") 
dob_field.send_keys(Keys.ENTER)


#scroll 
driver.execute_script("window.scrollBy(0, 500);") 

#upload pict 
file_path = "/Users/wahyurunnianto/Documents/MyDocs/2_copy.jpg" 
driver.find_element(By.ID, "uploadPicture").send_keys(file_path) 

# submit form 
driver.find_element(By.ID, "submit").click() 

#Validasi hasil submit 
try: 
    success_modal = wait.until(EC.presence_of_element_located((By.ID, "example-modal-sizes-title-lg")))
    print("Registrasi berhasil termasuk upload foto!") 
except TimeoutException: 
    print("Gagal submit atau popup tidak muncul.")

#Tunggu 
time.sleep(3) 
driver.quit()
