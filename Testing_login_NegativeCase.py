#-----Negative Case------#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#setup browser firefox 
driver = webdriver.Firefox () 
try: 
    
#positive case --login 
#open website 
    driver.get("https://practicetestautomation.com/practice-test-login/")
    username_field = driver.find_element(By.ID, "username") 
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "submit") 

    username_field.send_keys("wrong")
    password_field.send_keys("wrong")
    login_button.click() 


# Cek apakah redirect ke halaman dashboard 
    WebDriverWait(driver, 10).until( 
    EC.presence_of_element_located((By.ID, "error" ))
) 
#Teks print   
    error_text = driver.find_element(By.ID, "error").text.strip()
    print("Login Gagal! Error:", error_text)

except Exception as e: 
    print("Login gagal, namun tidak ada pesan error yang muncul .", str(e))

finally:
#cek url website 
    print ("Current URL: ", driver.current_url)


driver.implicitly_wait (3) 
