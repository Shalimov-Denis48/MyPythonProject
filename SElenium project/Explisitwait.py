from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebriverWait

driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')

driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://www.expedia.com/")

driver.implicitly_wait(5)

driver.find_element_by_class_name("uitk-tab-anchor").click()

driver.find_element(By.ID, "location-field-leg1-origin-input").send_keys("HHC")

time.sleep(2)

driver.find_element(By.ID, "location-field-leg1-destination-input").send_keys("NYC")

driver.find_element(By.ID, "d1-btn").clear()
driver.find_element(By.ID, "d1-btn").send_keys("Departing March 10, 2021")

driver.find_element(By.ID, "d2-btn").clear()
driver.find_element(By.ID, "d2-btn").send_keys("Returning March 14, 2021")

driver.find_element(By.XPATH, "//*[@id='wizard-flight-pwa-1']/div[3]/div[2]/button").click()
wait = WebDriverWait(driver,10)
element = wait.unit(EC.unit_to_be_clickable())


