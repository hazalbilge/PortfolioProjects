#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
from bs4 import BeautifulSoup 
import requests
import smtplib
import time
import datetime


# In[ ]:


url = 'https://www.trendyol.com/sr?q=t-shirt&qt=t-shirt&st=t-shirt&os=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate, br","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "DNT":"1","Connection":"close","Upgrade-Insecure-Requests":"1"} 

data_list = []
num_pages = 5
for page_number in range(1, num_pages + 1):
    current_url = url.format(page_number)
    
page = requests.get(url, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find_all(class_='prdct-desc-cntnr-ttl')
owner = [title.get_text().strip() for title in title]

product = soup2.find_all(class_= 'prdct-desc-cntnr-name hasRatings')
product_name = [title.get_text().strip() for title in product]

price_elements = soup2.find_all(class_='prc-box-dscntd')
price = [element.text.strip().replace('TL','') for element in price_elements]

rating_elements = soup2.find_all(class_ = 'ratingCount')
rating = [element.text.strip().replace('(','').replace(')','') for element in rating_elements]

min_length = min(len(owner), len(product_name), len(price), len(rating))

#for i in range(min_length):
    #row = [owner[i], product_name[i], price[i], rating[i]]
    #data.append(row)
data ={
    'Seller': owner[:min_length],
    'Product': product_name[:min_length],
    'Price': price[:min_length],
    'Rating Count': rating[:min_length]
}

data_list.append(data)

df = pd.DataFrame(data_list)
df.head()

df.to_csv(r'C:\Users\User\Desktop\Python Tutorials\Trendyol.csv', index=False)


# In[108]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url_template = 'https://www.trendyol.com/sr?q=t-shirt&qt=t-shirt&st=t-shirt&os=1&page={}'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
           "Accept-Encoding": "gzip, deflate, br",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
           "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

data_list = []

# Define the number of pages you want to scrape
num_pages = 5  # You can change this to the desired number of pages

for page_number in range(1, num_pages + 1):
    current_url = url_template.format(page_number)

    page = requests.get(current_url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find_all(class_='prdct-desc-cntnr-ttl')
    product = soup2.find_all(class_='prdct-desc-cntnr-name hasRatings')
    price_elements = soup2.find_all(class_='prc-box-dscntd')
    rating_elements = soup2.find_all(class_='ratingCount')

    for t, p, pe, re in zip(title, product, price_elements, rating_elements):
        data = {
            'Seller': t.get_text().strip(),
            'Product': p.get_text().strip(),
            'Price': pe.text.strip().replace('TL', ''),
            'Rating Count': re.text.strip().replace('(', '').replace(')', '')
        }
        data_list.append(data)

# Create a DataFrame from the list of data
df = pd.DataFrame(data_list)

df.to_csv(r'C:\Users\User\Desktop\Python Tutorials\Trendyol.csv', index=False)


# In[109]:


def check_price():
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    
    url_template = 'https://www.trendyol.com/sr?q=t-shirt&qt=t-shirt&st=t-shirt&os=1&page={}'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
           "Accept-Encoding": "gzip, deflate, br",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
           "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    data_list = []

    # Define the number of pages you want to scrape
    num_pages = 5  # You can change this to the desired number of pages

    for page_number in range(1, num_pages + 1):
        current_url = url_template.format(page_number)

        page = requests.get(current_url, headers=headers)
        soup1 = BeautifulSoup(page.content, "html.parser")
        soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

        title = soup2.find_all(class_='prdct-desc-cntnr-ttl')
        product = soup2.find_all(class_='prdct-desc-cntnr-name hasRatings')
        price_elements = soup2.find_all(class_='prc-box-dscntd')
        rating_elements = soup2.find_all(class_='ratingCount')

        for t, p, pe, re in zip(title, product, price_elements, rating_elements):
            data = {
                'Seller': t.get_text().strip(),
                'Product': p.get_text().strip(),
                'Price': pe.text.strip().replace('TL', ''),
                'Rating Count': re.text.strip().replace('(', '').replace(')', '')
            }
            data_list.append(data)

    # Create a DataFrame from the list of data
    df.to_csv(r'C:\Users\User\Desktop\Python Tutorials\Trendyol.csv', index=False)
    


# In[ ]:


#this is check the price every single day
while(True):
    check_price()
    time.sleep(86400)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




