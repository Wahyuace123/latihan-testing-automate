from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

service = Service("/usr/local/bin/geckodriver") 
driver = webdriver.Firefox(service=service) 
wait = WebDriverWait(driver, 10)
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
driver.maximize_window()

#scroll ke element
dropdown = wait.until(EC.element_to_be_clickable((By.ID,"Select Country")))
driver.execute_script("arguments[0].scrollIntoView();",dropdown)
time.sleep(1)  # tambahin jeda biar scroll selesai
dropdown.click()


#pilih options

option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select")))
option.click()

time.sleep(3)
driver.quit()