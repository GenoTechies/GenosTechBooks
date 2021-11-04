#!/usr/bin/env python
# coding: utf-8

# # District Wise Infected Count
# 
# Click the {fa}`rocket` --> {guilabel}`Live Code` button above on this page, and run the code below.

# In[1]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install matplotlib')
get_ipython().system('pip install seaborn')
import requests  # Import the requests library
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns


# In[2]:


from IPython.core.display import display, HTML
display(HTML("<style>.toggle-button { display :none !important; }</style>"))
display(HTML("<style>.toggle-button-hidden { display :none !important; }</style>"))
display(HTML("<style>.fas fa-download { display :none !important; }</style>"))


# Query URL
url = ('https://covid19-healthylk.herokuapp.com/api/districtstotal?startdate=2021-08-31&enddate=2021-09-31')
print(url)
response = requests.get(url)  # Make a GET request to the URL
# Print status code (and associated text)
print(f"Request returned {response.status_code} : '{response.reason}'")
# Print data returned (parsing as JSON)
payload = response.json()  # Parse `response.text` into JSON


# In[3]:


data=pd.json_normalize(payload['data'])
selected=data[["datetext", "counttext","location.formattedAddress"]]
print(selected)


# In[4]:


pivoted = pd.DataFrame(selected.pivot_table(values='counttext', index='datetext', columns='location.formattedAddress', aggfunc='sum'))
#pivoted = pivoted.set_index('datetext')
print(list(pivoted.columns.values))
#print(pivoted)


# In[5]:


# figure size globally set for matplotlib
mpl.rcParams['figure.figsize'] = (20, 20)
mpl.rcParams['axes.grid'] = False

ax = pivoted.plot()
#ax.set_color_palette(sns.color_palette("muted"))
pivoted.plot(ax=ax)
plt.legend(loc='best',prop={'size': 6}) 
plt.show() 

