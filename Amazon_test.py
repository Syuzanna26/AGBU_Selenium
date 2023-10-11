
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://www.amazon.com")
fieldEnter = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By. XPATH, "//div[@id='nav-signin-tooltip']/a/span" )))
fieldEnter.click()

loginFieldElement = driver.find_element(By. ID, "ap_email")
loginFieldElement.clear()
loginFieldElement.send_keys("syuzanna26.12@gmail.com")
continueFieldElement = driver.find_element(By. CLASS_NAME, "a-button-input").click()

passwordFieldElement = driver.find_element(By. ID, "ap_password")
passwordFieldElement.clear()
passwordFieldElement.send_keys("Davit2602")
time.sleep(7)
signFieldElement = driver.find_element(By. ID, "signInSubmit").click()
time.sleep(5)
driver.quit()
