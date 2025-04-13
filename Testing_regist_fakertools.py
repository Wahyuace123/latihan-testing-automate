from selenium import webdriver 
from selenium.webdriver.firefox.service import Service 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys     
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from faker import Faker
import time 

#Setup 
fake = Faker() 
service = Service("/usr/local/bin/geckodriver") 
driver = webdriver.Firefox(service=service) 
wait = WebDriverWait(driver, 10)

#Generate data fake 
first_name = fake.first_name() 
last_name = fake.last_name() 
email = fake.email() 
phone = fake.msisdn() [:10] 
address = fake.address().replace("\n", " ")
birth_date = fake.date_of_birth(minimum_age=18, maximum_age=40).strftime("%d %b %Y") 

print(f"Data yang diisi:{first_name}{last_name}|{email}|{phone}| {birth_date}") 

#Open website  
driver.get("https://demoqa.com/automation-practice-form") 
driver.maximize_window() 

#Isi form 
wait.until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys(first_name) 
driver.find_element(By.ID, "lastName").send_keys(last_name) 
driver.find_element(By.ID, "userEmail").send_keys(email) 
driver.find_element(By.XPATH, "//label[@for='gender-radio-1']").click() 
driver.find_element(By.ID, "userNumber").send_keys(phone) 

#Dob 
dob_field = driver.find_element(By.ID, "dateOfBirthInput") 
dob_field.click() 
dob_field.send_keys(Keys.CONTROL + "a") 
dob_field.send_keys(birth_date) 
dob_field.send_keys(Keys.ENTER) 

#Subject 
subject_input = driver.find_element(By.ID, "subjectsInput") 
subject_input.send_keys("Math") 
subject_input.send_keys(Keys.ENTER) 

#Hobbies 
driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']").click() #--> Sport 

#Upload Foto 
file_path = "/Users/wahyurunnianto/Documents/MyDocs/2_copy.jpg" 
driver.find_element(By.ID, "uploadPicture").send_keys(file_path) 

#Alamat 
driver.find_element(By.ID, "currentAddress").send_keys(America) 

#scroll 
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 

#State & City 
wait.until(EC.element_to_be_clickable((By.ID, "state"))).click() 
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class=' css-1uccc91-singleValue']"))).click() 
wait.until(EC.element_to_be_clickable((By.ID, "city"))).click() 
wait.until(EC.element_to_be_clickable((By.ID, "//div[contains(text(),'Delhi')]"))).click() 

#Submit 
driver.find_element(By.ID, "submit").click() 

#Validasi 
try: 
    wait.until(EC.presence_of_element_located((By.XPATH, "example-modal-sizes-title-lg"))) 
    print("Registrasi berhasil dengan data randpm dari Faker!") 
except: 
    print("Registrasi gagal!") 

time.sleep(3) 
driver.quit()     