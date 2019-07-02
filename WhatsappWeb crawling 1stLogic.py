#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge('C:\Windows\System32\MicrosoftWebDriver.exe')
mylist=[]

try:
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 60)
    xarg = '//div[@class="_2WP9Q"]'
    grouptitle = wait.until(EC.presence_of_element_located((By.XPATH, xarg)))
    time.sleep(25)
except:
    print("Please Check Your Internet connection and Try again")
    
for person in driver.find_elements_by_class_name('X7YrQ'):
    people = person.find_element_by_class_name("_19RFN")
    print("\n\nNAME: ",people.text,"\n")    
    mylist.append(people.text)
    people.click()
    
    xr=driver.find_element_by_xpath("//*[@class='_1_keJ']")
    xr.click()
    for i in range(1500):               #To be fixed- need mechanism so that automatically 
        xr.send_keys(Keys.ARROW_UP)     #scroll stops when first chat found 
         
    time.sleep(20)
       
    #x=[]
    y=[]
    #x=driver.find_elements_by_xpath("//*[@class='FTBzM' or @class='FTBzM _17BiH' or @class='FTBzM _3CGDY']")
    y=driver.find_elements_by_xpath("//*[@class='selectable-text invisible-space copyable-text']")
    #l=len(x)
    l1=len(y)
#For Details of chats like time,day,media size etc...(x has its path)
    
#    counter=0
#    for i in range(l+1):
#        try:
#            print(x[i].text)
#            counter+=1
#        except:
#            print("\n\n",counter," Chats scraped!")            
    counter=0
    
#For only chats    
    for i in range(l1+1):
        try:
            print("->",y[i].text)
            counter+=1
        except:
            print("\n\n*************",counter," Chats scraped for this contact!********************")   
            
    #Below code for scroll using key not working: [Major Issue] -first priority
    
    #xl=driver.find_element_by_xpath("//*[@class='_2HS9r']")
    #xl.click()
    #xl.send_keys(Keys.ARROW_DOWN)
    driver.execute_script("arguments[0].scrollIntoView()",people )#scroll working but abnormal behaviour and only 18 names   
    time.sleep(2)
    
length=len(mylist)
print("\n\n",length," Contacts/Groups Crawled.")


