#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
from bs4 import BeautifulSoup 
import requests
import smtplib
import time
import datetime


# In[23]:


# Connect to Website
url = 'https://www.amazon.com/Feelin-Good-Tees-Equation-Valentines/dp/B01B3ET8IG/ref=sr_1_26_sspa?crid=1A3UR4H5ASKLE&keywords=data%2Banalyst%2Btshirt&qid=1699538691&sprefix=data%2Banalyst%2Btshir%2Caps%2C194&sr=8-26-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&psc=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate, br","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "DNT":"1","Connection":"close","Upgrade-Insecure-Requests":"1"} 

page = requests.get(url, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()
#price = soup2.find(class_='a-price-symbol',class_='a-price-whole',class_='a-price-fraction').get_text(strip=True)
price = soup2.find('span', {'class': 'a-price-symbol'}).get_text(strip=True)
whole_price = soup2.find('span', {'class': 'a-price-whole'}).get_text(strip=True)
fractional_price = soup2.find('span', {'class': 'a-price-fraction'}).get_text(strip=True)

full_price = f"{price}{whole_price}{fractional_price}"


print(title)
print(full_price)


# In[24]:


price = full_price.strip()[1:]
title = title.strip()

print(title)
print(price)


# In[30]:


import datetime

today = datetime.date.today()

print(today)


# In[31]:


import csv

header = ['Title','Price', 'Date']
data = [title, price, today]

with open('AmazonWebScraperDataset.csv', 'w', newline ='', encoding ='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    


# In[36]:


import pandas as pd
df = pd.read_csv(r"C:\Users\User\AmazonWebScraperDataset.csv")
df


# In[35]:


# Now we are appending data to the csv

with open('AmazonWebScraperDataset.csv', 'a+', newline ='', encoding ='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[ ]:


def check_price():
    url = 'https://www.amazon.com/Feelin-Good-Tees-Equation-Valentines/dp/B01B3ET8IG/ref=sr_1_26_sspa?crid=1A3UR4H5ASKLE&keywords=data%2Banalyst%2Btshirt&qid=1699538691&sprefix=data%2Banalyst%2Btshir%2Caps%2C194&sr=8-26-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&psc=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate, br","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "DNT":"1","Connection":"close","Upgrade-Insecure-Requests":"1"} 

    page = requests.get(url, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()
    price = soup2.find('span', {'class': 'a-price-symbol'}).get_text(strip=True)
    whole_price = soup2.find('span', {'class': 'a-price-whole'}).get_text(strip=True)
    fractional_price = soup2.find('span', {'class': 'a-price-fraction'}).get_text(strip=True)
    full_price = f"{price}{whole_price}{fractional_price}"
    
    price = full_price.strip()[1:]
    title = title.strip()

    import datetime
    today = datetime.date.today()
    
    import csv
    header = ['Title','Price', 'Date']
    data = [title, price, today]
    
    
    with open('AmazonWebScraperDataset.csv', 'a+', newline ='', encoding ='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
    if(price < 14):
        send_mail()



# In[ ]:


#this is check the price every single day
while(True):
    check_price()
    time.sleep(86400)


# In[ ]:


import pandas as pd
df = pd.read_csv(r"C:\Users\User\AmazonWebScraperDataset.csv")
df


# In[ ]:


def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('hazalbilge5@gmail.com', 'xxxxxxxx')
    subject  = "The Shirt you want is below $15! Now is your chance to buy!"
    body = "Hazal, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess up!"
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'hazalbilge5@gmail.com',
    msg)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




