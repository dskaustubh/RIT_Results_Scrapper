from selenium import webdriver
import time
import pymongo
driver = webdriver.Chrome("./chromedriver.exe")
url="http://exam.msrit.edu/"

myclient = pymongo.MongoClient("mongodb+srv://kds:<password>@cluster0-e1dhw.mongodb.net/results?retryWrites=true&w=majority")
mydb =myclient['results']
mycol=mydb['june2020']

branches={
    'CS':147,
    'EC':140,
    'AT':77,
    'BT':65,
    'CH':68,
    'CV':132,
    'EE':73,
    'EI':66,
    'TE':65,
    'IM':64,
    'IS':137,
    'ME':216,
    'ML':65
}

data=[]
cnt=0
years=['19','18','17','16']
driver.get(url)
USN="1MS"
capip=input("Enter The Captcha: ")
capip=capip.upper()
time.sleep(.5)
for y in years:
    for b in branches.keys():   
        for i in range (1,branches[b]):
            usn=driver.find_element_by_xpath('//*[@id="usn"]')
            cap=driver.find_element_by_xpath('//*[@id="osolCatchaTxt0"]')
            gobtn=driver.find_element_by_xpath('//*[@id="main"]/div/table/tbody/tr[8]/td/div/form/table/tbody/tr[3]/td[1]/input')
            usn.send_keys(USN+str(y)+b+str(i).zfill(3))
            cap.send_keys(capip)
            gobtn.click()
            try:
                sgpa=driver.find_element_by_xpath('//*[@id="main"]/div/table/tbody/tr[11]/td/table/tbody/tr/td[2]/table/tbody/tr/td[4]/div/span[2]').text.strip()
                name=driver.find_element_by_xpath('//*[@id="main"]/div/table/tbody/tr[8]/td/table/tbody/tr/td[2]/table/tbody/tr/td[3]').text
                mydict={}
                mydict['name']=name
                mydict['sgpa']=sgpa
                mydict['usn']=USN+str(y)+b+str(i).zfill(3)
                print(mydict)
                data.append(mydict)
            except:
                print("USN: "+USN+str(y)+b+str(i).zfill(3)+" Data Couldnt be  Retrieved")
                cnt=cnt+1
            finally:
                print(f"Missed : {cnt} USNS")
                driver.back()


x = mycol.insert_many(data)
print(x.inserted_ids)
driver.close()