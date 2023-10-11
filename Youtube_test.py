import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://www.youtube.com")

searchFieldElement = driver.find_element(By. CLASS_NAME, "search")
searchFieldElement.clear()
searchFieldElement.send_keys("Yanni Nostalgia")
time.sleep(5)
searchFieldElement.send_keys(Keys.ENTER)

firstVideo = driver.find_element(By. XPATH,"//yt-image[@class='style-scope.ytd-thumbnail']//img")
firstVideo.click()
time.sleep(10)

pauseButton = driver.find_element(By. CLASS_NAME,"ytp-play-button.ytp-button")
pauseButton.click()
time.sleep(3)

driver.close()