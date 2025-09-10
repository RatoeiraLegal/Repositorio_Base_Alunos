from selenium import webdriver
from selenium.webdriver.common.by import By
import time


patch = []

driver = webdriver.Chrome()
url1 = driver.get('https://www.guiltygear.com/ggst/en/news/post-category/patch/')
time.sleep(5)
href = driver.find_elements(By.CLASS_NAME, 'entry')
for url in href:
    print(url.get_attribute("href"))

url2 = driver.get('https://www.guiltygear.com/ggst/en/news/post-category/patch/page/2')
time.sleep(5)
href = driver.find_elements(By.CLASS_NAME, 'entry')
for url in href:
    print(url.get_attribute("href"))
    
url3 = driver.get('https://www.guiltygear.com/ggst/en/news/post-category/patch/page/3')
time.sleep(5)
href = driver.find_elements(By.CLASS_NAME, 'entry')
for url in href:
    print(url.get_attribute("href"))

url4 = driver.get('https://www.guiltygear.com/ggst/en/news/post-category/patch/page/4')
time.sleep(5)
href = driver.find_elements(By.CLASS_NAME, 'entry')
for url in href:
    print(url.get_attribute("href"))
driver.quit()