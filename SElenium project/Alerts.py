from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')

driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)
# driver.switch_to_alert().accept()
# Открытие выпадающего меню

driver.switch_to_alert().dismiss()
# №закрытие выпадающего меню
