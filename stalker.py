from selenium import webdriver
import time
import pymongo
myclient = pymongo.MongoClient("mongodb+srv://<your username>:<your password>@cluster0-e1dhw.mongodb.net/test?retryWrites=true&w=majority")
mydb =myclient['results']
mycol=mydb['dec2019']
driver = webdriver.Chrome()
url="http://exam.msrit.edu/"
driver.get(url)
USN="1MS18CS"
mylist=[]
capip=input("Enter The Captcha: ")
capip=capip.upper()
for i in range (1,150):
    time.sleep(1.2)
    usn=driver.find_elements_by_id("usn")[0]
    cap=driver.find_element_by_id("osolCatchaTxt0")
    gobtn=driver.find_element_by_class_name("buttongo")
    usn.send_keys(USN+str(i).zfill(3))
    cap.send_keys(capip)
    gobtn.click()
    time.sleep(1.2)
    try:
        sgpa=driver.find_element_by_xpath('//*[@id="main"]/div/table/tbody/tr[11]/td/table/tbody/tr/td[2]/table/tbody/tr/td[4]/div/span[2]').text.strip()
        name=driver.find_element_by_xpath('//*[@id="main"]/div/table/tbody/tr[8]/td/table/tbody/tr/td[2]/table/tbody/tr/td[3]').text
        print(USN+str(i).zfill(3)+"\t"+sgpa+"\t"+name)
        sgpa=float(sgpa)
        mydict={}
        mydict['name']=name
        mydict['sgpa']=sgpa
        mydict['usn']=USN+str(i).zfill(3)
        mylist.append(mydict)
    except:
        print("USN: "+USN+str(i).zfill(3)+" Doesnt Exist")
    finally:
        driver.back()
x = mycol.insert_many(mylist)
print(x.inserted_ids)
driver.close()