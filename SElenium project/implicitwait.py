from selenium import webdriver

driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')

driver.get("https://mail.i.ua/?_url=/?_rand=2081385608&phcode=6fb459b887e8b47592a1200e8629eae4&_rand=1614155930")

driver.implicitly_wait(10)

driver.find_element_by_name("login").send_keys("Golden5city")
driver.find_element_by_name("pass").send_keys("8046ck")

driver.find_element_by_name("login").click()