from selenium import webdriver

driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
driver.get("https://minfin.com.ua/currency/banks/")

rows = len(driver.find_elements_by_xpath("/html/body/main/div/div/div[1]/div/section[2]/table/thead/tr"))

cols = len(driver.find_elements_by_xpath("/html/body/main/div/div/div[1]/div/section[2]/table/tbody/tr/td[1]"))

print(rows)
print(cols)

for r in range(1,rows +1):
    for c in range(1,cols+1):
        value = driver.find_element_by_xpath("/html/body/main/div/div/div[1]/div/section[2]/table/tbody/tr["+str(r)+"/td["+str(c)+"]").text
        print(value)
# XPath не верный. Необходимо переписать по настоящему сайту
