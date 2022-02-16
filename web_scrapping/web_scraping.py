#!/usr/bin/env python
# coding: utf-8

# ## Welcome to your first casestudy
# - In this case study you have to scrape weather data from the website  **"http://www.estesparkweather.net/archive_reports.php?date=200901"**
# - Scrape all the available attributes of weather data for each day from **2009-01-01 to 2018-10-28**
# - Ignore records for missing days
# - Represent the scraped data as **pandas dataframe** object.

# ### Dataframe specific deatails
# - Expected column names (order dose not matter):   
#        ['Average temperature (°F)', 'Average humidity (%)',
#        'Average dewpoint (°F)', 'Average barometer (in)',
#        'Average windspeed (mph)', 'Average gustspeed (mph)',
#        'Average direction (°deg)', 'Rainfall for month (in)',
#        'Rainfall for year (in)', 'Maximum rain per minute',
#        'Maximum temperature (°F)', 'Minimum temperature (°F)',
#        'Maximum humidity (%)', 'Minimum humidity (%)', 'Maximum pressure',
#        'Minimum pressure', 'Maximum windspeed (mph)',
#        'Maximum gust speed (mph)', 'Maximum heat index (°F)']
# - Each record in the dataframe corresponds to weather deatils of a given day
# - Make sure the index column is **date-time format (yyyy-mm-dd)**
# - Perform necessary data cleaning and type cast each attributes to relevent data type

# ### Saving the dataframe
# - Once you are done with you scrapping save your dataframe as pickle file by name 'dataframe.pk'
# 
# #### Sample code to save pickle file
# ```python
# import pickle
# with open("dataframe.pk", "wb") as file:
#     pickle.dump(<your_dataframe>, file)
# ```
#  
#  

# ### Run the below cell to import necessary packages
# - These packages should be sufficient to perform you task
# - In case if you are looking are any other packages run **!pip3 install <package_name> --user with in a cell**

# In[50]:


import re

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# In[51]:


#### Start you code here, you are free to add any number of cells

range_date = pd.date_range(start='1/1/2009', end='11/1/2018', freq='M')
dates = [str(i)[:4] + str(i)[5:7] for i in range_date]

# In[52]:


range_date

# In[53]:


df_list = []
index = []
for k in tqdm(range(len(dates))):
    url = "http://www.estesparkweather.net/archive_reports.php?date=" + dates[k]
    # Our loop will run for the number of elements in dates
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find_all('table')
        type(table)
        # This will give
        # bs4.element.ResultSet
        parsed_data = [row.text.splitlines() for row in table]
        parsed_data = parsed_data[:-9]
        for l in range(len(parsed_data)):
            parsed_data[l] = parsed_data[l][2:len(parsed_data[l]):3]
        for i in range(len(parsed_data)):
            c = ['.'.join(re.findall("\d+", str(parsed_data[i][j].split()[:5]))) for j in range(len(parsed_data[i]))]
            df_list.append(c)
            index.append(dates[k] + c[0])

# In[54]:


from datetime import datetime

f_index = [index[i] for i in range(len(index)) if len(index[i]) > 6]
data = [df_list[i][1:] for i in range(len(df_list)) if len(df_list[i][1:]) == 19]
final_index = [datetime.strptime(str(f_index[i]), '%Y%m%d').strftime('%Y-%m-%d') for i in range(len(f_index))]
col = ['Average temperature (°F)', 'Average humidity (%)',
       'Average dewpoint (°F)', 'Average barometer (in)',
       'Average windspeed (mph)', 'Average gustspeed (mph)',
       'Average direction (°deg)', 'Rainfall for month (in)',
       'Rainfall for year (in)', 'Maximum rain per minute',
       'Maximum temperature (°F)', 'Minimum temperature (°F)',
       'Maximum humidity (%)', 'Minimum humidity (%)', 'Maximum pressure',
       'Minimum pressure', 'Maximum windspeed (mph)',
       'Maximum gust speed (mph)', 'Maximum heat index (°F)']
final_df = pd.DataFrame(data, columns=col, index=final_index)
final_df = final_df.astype(float)
final_df.dtypes

# In[56]:


final_df.drop(index=final_df.index[-1], axis=0, inplace=True)
final_df.drop(index=final_df.index[-1], axis=0, inplace=True)
final_df.drop(index=final_df.index[-1], axis=0, inplace=True)
final_df

# In[63]:


import numpy as np

final_df.index = final_df.index.map(np.datetime64)
final_df.index

# In[64]:
print(final_df)

import pickle

with open("dataframe.pk", "wb") as file:
    pickle.dump(final_df, file)

# In[ ]:
