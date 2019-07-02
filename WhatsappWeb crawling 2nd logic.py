#!/usr/bin/env python
# coding: utf-8



from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
import sys

driver = webdriver.Edge('C:\Windows\System32\MicrosoftWebDriver.exe')
#f=open("D:\EDUCATIONAL\CERT-In\WhatsappWebChats.txt","w")
#f.write("*****Chats Crawled Using Python Script By PHANTOM")
#f.close()
mylist=[]

try:
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 60)
    xarg = '//div[@class="_2WP9Q"]'
    grouptitle = wait.until(EC.presence_of_element_located((By.XPATH, xarg)))
    time.sleep(25)
except:
    print("Please Check Your Internet connection and Try again")
    
for person in driver.find_elements_by_class_name('X7YrQ'):      #Only getting 19 contacts
    people = person.find_element_by_class_name("_19RFN")        #Putting scroll might help
    mylist.append(people.text)                              #as it will load those contacts

length=len(mylist)
#print(length)

for i in range(length):
    #f=open("D:\EDUCATIONAL\CERT-In\WhatsappWebChats.txt","a")
    t=mylist[i]  
    #f.write(t)
    print("\n\nNAME: ",t,"\n")    
    target="\'"+t+"\'"
    x_arg = '//span[contains(@title,' + target + ')]'
    try:
        group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg))) 
        group_title.click()
    except:
        print("Name not found") 
        sys.exit()
    
    xr=driver.find_element_by_xpath("//*[@class='_1_keJ']")
    xr.click()
    for i in range(1500):                       #To be fixed(Static, need mechanism to
          xr.send_keys(Keys.ARROW_UP)  #automatically stop when we reach first message)       
    
    time.sleep(20)
       
    #x=[]
    y=[]
    #x=driver.find_elements_by_xpath("//*[@class='FTBzM' or @class='FTBzM _17BiH' or @class='FTBzM _3CGDY']")
    y=driver.find_elements_by_xpath("//*[@class='selectable-text invisible-space copyable-text']")
    #l=len(x)
    l1=len(y)
#For Chat Details like time,day,media size etc...
    
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
            string="->"+y[i].text
            #f.write(string)
            counter+=1
        except:
            print("\n\n*************",counter," Chats scraped for this contact!********************")
    #f.close()
    







