#!/usr/bin/env python
# coding: utf-8

# In[6]:


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys


# In[7]:

#Scroll methods which are not working

#driver.execute_script("window.scrollBy(0,1050)")
#people.location_once_scrolled_into_view#error
#people.scrollIntoView()#error
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#driver.execute_script("element.scrollBy(0,1080)")#error


# In[8]:

#Using Microsoft Edge driver. Incase of any other browser download its webdriver and 
#put its .exe path below

driver = webdriver.Edge('C:\Windows\System32\MicrosoftWebDriver.exe')
mylist=[]

try:
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 60)
    print("Scan the QR code and type done: ") #Type anything, just to give time to confirm if whatsappweb opened successfully
    input()
    xarg = '//div[@class="_2WP9Q"]'
    grouptitle = wait.until(EC.presence_of_element_located((By.XPATH, xarg)))
    time.sleep(20)
except:
    print("Please Check Your Internet connection and Try again")
    sys.exit()
    
for person in driver.find_elements_by_class_name('X7YrQ'):
    people = person.find_element_by_class_name("_19RFN")
    print("\n\nNAME: ",people.text,"\n")    
    mylist.append(people.text)
    people.click()
    
    #Logic 1- on right side using arrow up key and waiting for 60
    #seconds so that all chats can be loaded and then scrap it.
    #driver.find_element_by_xpath("//*[@class='_1_keJ']").send_keys(Keys.ARROW_UP) #To be fixed
    #time.sleep(60)
    
    #Below code for sending page up key also not working
    #z=driver.find_elements_by_xpath("//*[@class='_1_q7u']").click()
    #ActionChains(driver) \
    #            .key_down(Keys.PAGE_UP)
    #time.sleep(30)
    
#    x=[]
    y=[]
#    x=driver.find_elements_by_xpath("//*[@class='FTBzM' or @class='FTBzM _17BiH' or @class='FTBzM _3CGDY']")
    y=driver.find_elements_by_xpath("//*[@class='selectable-text invisible-space copyable-text']")
#    l=len(x)
    l1=len(y)
#For Details like time,day,media size etc...
    
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
            time.sleep(5)
            #Logic 2- Using scroll of right panel. Working but behaviour is abnormal
            driver.execute_script("arguments[0].scrollIntoView()",y[i]) #need fixing of scroll if key page down does not work
            #driver.execute_script("arguments[0].scrollIntoView()",x[i])
            counter+=1
        except:
            print("\n\n*************",counter," Chats scraped for this contact!********************")   
            
    driver.execute_script("arguments[0].scrollIntoView()",people )#scroll working but abnormal behaviour and only 18 names are retrieved  
    time.sleep(2)
    
length=len(mylist)
print("\n\n",length," names found.")
#print(mylist)