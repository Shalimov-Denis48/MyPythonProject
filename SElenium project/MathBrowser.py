from selenium import webdriver

driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')

driver.get("http://nnmclub.to/")


# Title of the page
print(driver.title)
# Close the browser
driver.close()