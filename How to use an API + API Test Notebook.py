#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'15',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '0ad53085-1cb2-4eb8-ad9e-3ffbd7e56509',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


# In[2]:


type(data)


# In[7]:


import pandas as pd

#This allows you to see all the columns, not just like 15
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# In[8]:


#This normalizes the data and makes it all pretty in a dataframe
df = pd.json_normalize(data['data'])
df['timestamp'] = pd.to_datetime('now')
df


# In[14]:


def api_runner():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'15',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '0ad53085-1cb2-4eb8-ad9e-3ffbd7e56509',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    
    df2 = pd.json_normalize(data['data'])
    df2['timestamp'] = pd.to_datetime('now')
    df
    #df_append = pd.DataFrame(df2)
    #df = pd.concat([df2,df_append])
    
    if not os.path.isfile(r'C:\Users\User\Desktop\Pandas Tutorials\API.csv'):
        df.to_csv(r'C:\Users\User\Desktop\Pandas Tutorials\API.csv', header = 'column_names')
    else:
        df.to_csv(r'C:\Users\User\Desktop\Pandas Tutorials\API.csv', mode='a', header=False)      
        


# In[15]:


import os 
from time import time
from time import sleep

for i in range(333):
    api_runner()
    print('API Runner completed successfully!')
    sleep(60) #sleep for 1 minute
exit()


# In[17]:


df72=pd.read_csv(r'C:\Users\User\Desktop\Pandas Tutorials\API.csv')
df72


# In[16]:


df


# In[19]:


pd.set_option('display.float_format', lambda x: '%.5f' % x)


# In[20]:


df


# In[24]:


df3 = df.groupby('name', sort=False)[['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d', 'quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d']].mean()
df3


# In[25]:


df4 = df3.stack()
df4


# In[26]:


type(df3)


# In[27]:


type(df4)


# In[28]:


df5 = df4.to_frame(name='values')
df5


# In[30]:


df5.count()


# In[33]:


index = pd.Index(range(90))
#df6 = df5.set_index(index)
df6 = df5.reset_index()
df6


# In[34]:


df7 = df6.rename(columns={'level_1':'percent_change'})
df7


# In[40]:


df7['percent_change'] = df7['percent_change'].replace(['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d', 'quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d'], ['1h','24h','7d','30d','60d','90d'])
df7


# In[35]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[41]:


sns.catplot(x='percent_change',y='values',hue='name',data=df7, kind='point')


# In[44]:


df10 = df[['name','quote.USD.price','timestamp']]
df10 = df10.query("name == 'Bitcoin'")
df10


# In[47]:


sns.set_theme(style="darkgrid")
sns.lineplot(x = 'timestamp', y='quote.USD.price', data = df10)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




