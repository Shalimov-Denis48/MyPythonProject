from selenium import webdriver

driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

status = driver.find_element_by_id("RESULT_RadioButton-7_1").is_selected()
print(status)

driver.find_element_by_id("RESULT_RadioButton-7_1").click()

status = driver.find_element_by_id("RESULT_RadioButton-7_1").is_selected()
print(status)

# Working with check boxes

driver.find_element_by_id("RESULT_CheckBox-8").click()
driver.find_element_by_id("RESULT_CheckBox-8_3").click()



