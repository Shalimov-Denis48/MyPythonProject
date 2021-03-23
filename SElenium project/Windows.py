from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')

driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle)

handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

driver.quit()
