#!/usr/bin/env python
# coding: utf-8

# # District Chart
# 
# 

# In[1]:


import requests  # Import the requests library
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
# Query URL
url = ('https://covid19-healthylk.herokuapp.com/api/districtstotal?startdate=2021-08-31&enddate=2021-09-31')
print(url)
response = requests.get(url)  # Make a GET request to the URL
# Print status code (and associated text)
print(f"Request returned {response.status_code} : '{response.reason}'")
# Print data returned (parsing as JSON)
payload = response.json()  # Parse `response.text` into JSON


# In[2]:


data=pd.json_normalize(payload['data'])
selected=data[["datetext", "counttext","location.formattedAddress"]]
print(selected)


# In[3]:


pivoted = pd.DataFrame(selected.pivot_table(values='counttext', index='datetext', columns='location.formattedAddress', aggfunc='sum'))
#pivoted = pivoted.set_index('datetext')
print(list(pivoted.columns.values))
#print(pivoted)


# In[4]:


# figure size globally set for matplotlib
mpl.rcParams['figure.figsize'] = (20, 20)
mpl.rcParams['axes.grid'] = False

ax = pivoted.plot()
#ax.set_color_palette(sns.color_palette("muted"))
pivoted.plot(ax=ax)
plt.legend(loc='best',prop={'size': 6}) 
plt.show() 

