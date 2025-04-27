#------Case-------# 
#form login
#input ussername & password 
#input salah --> munculin error message 

#-----Positive Case------#

from selenium import webdriver
from selenium.webdriver.firefox.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#setup browser firefox 
driver = webdriver.Firefox () 

#open website 
driver.get ("https://practicetestautomation.com/practice-test-login/")

#positive case --login 
username_field = driver.find_element(By.ID, "username") # ---> username di dapat dari inspect element website di field username dengan ID :Username  #
password_field = driver.find_element(By.ID, "password") # ---> password di dapat dari inspect element website di field username dengan ID :Password #
login_button = driver.find_element(By.ID, "submit") # ---> submit di dapat dari inspect element website di button dengan ID :Submit #

username_field.send_keys("student")
password_field.send_keys("Password123")
login_button.click() 

# Tunggu sebentar --> tunggu proses aplikasi berjalan (running)#
time.sleep(2)

# Cek apakah redirect ke halaman dashboard 
WebDriverWait(driver, 10).until( 
    EC.presence_of_element_located((By.TAG_NAME,"h1" ))
) 

#Teks print success  
success_message = driver.find_element(By.TAG_NAME, "h1").text 
print("Success message:", success_message)

#validasi heading 
assert "Logged In Successfully" in success_message

print("Positive login case PASSED!")


