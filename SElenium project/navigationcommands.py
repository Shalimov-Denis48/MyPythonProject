from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')

driver.get("http://www.seleniumframework.com/")

print(driver.title)

driver.get("https://galactika.com.ua/")

time.sleep(5)

print(driver.title)

driver.back()

print(driver.title)

driver.forward()

print(driver.title)

driver.close()