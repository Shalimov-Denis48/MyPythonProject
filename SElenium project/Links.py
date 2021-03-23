from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')

driver.get("https://bepartner-global.com/")

links = driver.find_elements(By.TAG_NAME, "a")

# Print how many links present in a page
print(len(links))

for link in links:
    print(link.text)

# click on ten link

# driver.find_element(By.LINK_TEXT, "истрация").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "Рег").click()