from selenium import webdriver
import time
import pymongo
driver = webdriver.Chrome("./chromedriver.exe")
url="http://exam.msrit.edu/eresultseven/"

myclient = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.sy0qm.mongodb.net/?retryWrites=true&w=majority")
mydb =myclient['results']
mycol=mydb['July2022']

branches={
    'CS':147,
}

data=[]
cnt=0
count_not_10 = 0
#years=['19','18','17','16']
years=['18']
driver.get(url)
USN="1MS"
capip=input("Enter The Captcha: ")
capip=capip.upper()
time.sleep(.5)
#print(driver.find_element_by_xpath('//*[@id="main"]/div/table/tbody/tr[10]/td/div/form/table/tbody/tr[2]/td[1]/div/table/tbody/tr[1]/td[2]/input'))
for y in years:
    for b in branches.keys():

        for i in range (1,branches[b]):
            usn=driver.find_element_by_xpath('//*[@id="main"]/div/table/tbody/tr[11]/td/div/form/table/tbody/tr[1]/td[3]/input')
            cap=driver.find_element_by_xpath('//*[@id="main"]/div/table/tbody/tr[11]/td/div/form/table/tbody/tr[2]/td[1]/div/table/tbody/tr[1]/td[2]/input')

            gobtn=driver.find_element_by_xpath('//*[@id="main"]/div/table/tbody/tr[11]/td/div/form/table/tbody/tr[3]/td[1]/input')
            usn.send_keys(USN+str(y)+b+str(i).zfill(3))
            cap.send_keys(capip)
            gobtn.click()
            try:
            #print(driver.find_element_by_xpath('/html/body/div[2]/div/div/div[4]/div/div/div[1]/div/div[3]/div/p'))
                sgpa=driver.find_element_by_xpath('/html/body/div[2]/div/div/div[4]/div/div/div[1]/div/div[3]/div/p').text.strip()
                mydict={}
                sgpa_num = float(sgpa)
                if sgpa_num!=10.0:
                    count_not_10+=1
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
print("SGPA not obtained 10: ", count_not_10)
driver.close()




