from selenium import webdriver
import bs4 as bs
import time

driver = webdriver.Chrome()
url="http://exam.msrit.edu/"
driver.get(url)
USN="1MS19CS"

capip=input("Enter The Captcha: ")
capip=capip.upper()
for i in range (1,150):
    time.sleep(1.5)
    usn=driver.find_elements_by_id("usn")[0]
    cap=driver.find_element_by_id("osolCatchaTxt0")
    gobtn=driver.find_element_by_class_name("buttongo")
    usn.send_keys(USN+str(i).zfill(3))
    cap.send_keys(capip)
    gobtn.click()
    try:
        sgpa=driver.find_element_by_xpath('//*[@id="main"]/div/table/tbody/tr[11]/td/table/tbody/tr/td[2]/table/tbody/tr/td[4]/div/span[2]').text.strip()
        print(USN+str(i).zfill(3)+"\t"+sgpa)
    except:
        print("USN: "+USN+str(i).zfill(3)+" Doesnt Exist")
    finally:
        driver.back()
driver.close()