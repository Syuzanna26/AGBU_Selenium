import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://www.google.com")

searchFieldElement = driver.find_element(By.ID,value="APjFqb")
searchFieldElement.clear()
searchFieldElement.send_keys("Ferrari Enzo")
searchFieldElement.send_keys(Keys.ENTER)
time.sleep(5)