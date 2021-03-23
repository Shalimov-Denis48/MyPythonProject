from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

inputboxes = driver.find_elements(By.CLASS_NAME, "text_field")

print(len(inputboxes))

status = driver.find_element(By.ID, "RESULT_TextField-1").is_displayed()
print("Displayed or not:", status)

status = driver.find_element(By.ID, "RESULT_TextField-1").is_enabled()
print("Enable or not:", status)


driver.find_element(By.ID, "RESULT_TextField-1").send_keys("Denis")
driver.find_element(By.ID, "RESULT_TextField-2").send_keys("Shalim")

driver.find_element_by_id("RESULT_TextField-3").send_keys("068644215")