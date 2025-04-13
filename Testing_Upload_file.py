from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import Select
import time

# Setup Browser
service = Service("/usr/local/bin/geckodriver")
driver = webdriver.Firefox(service=service)
wait = WebDriverWait(driver, 10) 

# Buka Browser
driver.get("https://bebeclub.eydendigital.co.id/tools/poop-tracker")
driver.maximize_window()

#pathfile
uploadfoto = "/Users/wahyurunnianto/Downloads/poop 2.jpeg" 

#input file 
upload_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "upload-photo"))) 

#scroll 
driver.execute_script("arguments[0].scrollIntoView();", upload_input) 

#upload file
upload_input.send_keys(uploadfoto) 

# Tunggu
time.sleep(3) 

#menampilkan popup
driver.find_element(By.ID, "username-login-otp").send_keys("081234567889")

#buttonvalidasi
driver.find_element(By.ID, "btn_verifikasi_nomor_handphone").click()
driver.switch_to.default_content() 

time.sleep(3)


#inputdata
driver.find_element(By.ID, "fullname-member").send_keys("lala")
driver.find_element(By.ID, "fullname-child-member").send_keys("aaa")

#datepicker
driver.find_element(By.ID, "children_dob").send_keys("2022-02-22")

#tunggu kalender
wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"datepick-form")))

#pilih tanggal
driver.find_element(By.CLASS_NAME, "day").click()

#submit
driver.find_element(By.ID, "btn_simple_regist_poop_tracker").click()

#otp 2
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://devoneloyalty.daninaportal.id/DANONEUAT/main.aspx?appid=70005542-33f4-eb11-8a50-827175cb47ff&pagetype=entitylist&etn=dis_sms_activity&viewid=27fd7d07-72bc-4832-8f8e-2ac779508e26/081234567889")

#tungguotp
otp_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='Grid9f608489-a8fa-425c-8184-5cb716048791_headerButtonsubject']//div//div[@class='ms-Stack root-141']")))
otp_code = otp_element.text.strip()
print("kode otp:", otp_code)

#tab3
driver.switch_to.window(driver.window_handles[0])

#inputotp
driver.find_element(By.CLASS_NAME, "modal-verifikasi-otp-poop-tracker_iner").send_keys(otp_code)


time.sleep(5)


