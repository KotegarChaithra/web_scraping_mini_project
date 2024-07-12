from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/hp/Documents/softwares/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = s)

driver.get("https://www.google.com/")

search = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
search.send_keys("House of the dragon")
search.send_keys(Keys.ENTER)
time.sleep(2)

# driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()

driver.find_element(By.XPATH,"/html/body/div[4]/div/div[13]/div[4]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div[1]/div/div/span/a/h3").click()
time.sleep(3)

driver.save_screenshot("C:/Users/hp/Documents/Github/Web_Scraping/dragon.png")

