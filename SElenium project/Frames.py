from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
driver.get("http://testautomationpractice.blogspot.com/")

driver.switch_to_frame("intercom-frame")
driver.find_element_by_link_text("/my/inbox/4706468/").click()
time.sleep(3)

driver.switch_to.default_content()

driver.switch_to_frame("frame name 2")
driver.find_element_by_link_text("Webdriver"frame name 2).click()
time.sleep(3)

driver.switch_to.default_content()
time.sleep(3)

driver.switch_to_frame("frame name 3")
driver.find_element_by_xpath("frame name 3")
