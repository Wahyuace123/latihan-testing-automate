from selenium import webdriver
from selenium.webdriver.firefox.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#setup browser
service = Service("/usr/local/bin/geckodriver") 
driver = webdriver.Firefox(service=service) 
wait = WebDriverWait(driver, 10)

#open browser
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

#datepicker
driver.switch_to.frame(driver.find_element(By.CLASS_NAME,"demo-frame"))

#finddatepicker
date_input = driver.find_element(By.ID, "datepicker")

#click
date_input.click()

#wait
wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"ui-datepicker")))

#element tanggal
all_dates = driver.find_elements(By.CSS_SELECTOR, "a.ui-state-default.ui-state-hover")

#selectdate
for date in all_dates:
    if date.text == "12":
        date.click()
        break


time.sleep(3)


