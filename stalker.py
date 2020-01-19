from selenium import webdriver
import bs4 as bs
driver = webdriver.Chrome()
url="http://exam.msrit.edu/"
driver.get(url)
usn=driver.find_elements_by_id("usn")[0]
usn.send_keys("1MS18CS050")
cap=driver.find_element_by_id("osolCatchaTxt0")
cap.send_keys("eden")
gobtn=driver.find_element_by_class_name("buttongo")
gobtn.click()