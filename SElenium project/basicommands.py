from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')

driver.get("http://www.seleniumframework.com/")

print(driver.title)

print(driver.current_url)

driver.find_element_by_xpath("//*[@id='main-nav']/li[8]/a/span").click()

time.sleep(5)

driver.close()
