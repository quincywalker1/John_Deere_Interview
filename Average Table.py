#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import numpy as np
import seaborn as sns
import openpyxl

df = pd.read_csv(r'C:\Users\quinc\OneDrive\Desktop\John Deere Interview/John_deere_python_dirty.csv')
df9 = pd.read_csv(r'C:\Users\quinc\OneDrive\Desktop\John Deere Interview/John_deere_python.csv')


# In[27]:


# I Just like to make sure I have the right Data
df.head()


# In[28]:


# I set this portion up so I can view all of my 'Average' Data
pd.set_option('display.max_rows', None)


# In[29]:


# For these next series of Code I used the data I cleaned in SQL to find average price for each commodity in each County.
Average_Modal = df9.groupby(['County_name', 'Commodity', 'Year'], as_index = False)['Modal_price($)'].mean()
print(Average_Modal)


# In[30]:


Average_Arrivals = df.groupby(['County_name', 'Commodity', 'Year'], as_index = False)['Arrivals_in_ton'].mean()
print(Average_Arrivals)


# In[31]:


Average_Min = df.groupby(['County_name', 'Commodity', 'Year'], as_index = False)['Min_price($)'].mean()
print(Average_Min)


# In[32]:


Average_Max = df.groupby(['County_name', 'Commodity', 'Year'], as_index = False)['Max_price($)'].mean()
print(Average_Max)


# In[33]:


df2 = pd.merge(Average_Arrivals, Average_Min, on=['County_name', 'Commodity', 'Year'])


# In[34]:


df3 = pd.merge(df2, Average_Max, on=['County_name', 'Commodity', 'Year'])


# In[35]:


df4 = pd.merge(df3, Average_Modal, on=['County_name', 'Commodity', 'Year'])


# In[38]:


df4.to_excel(r"C:\Users\quinc\OneDrive\Desktop\John Deere Interview/Averages.xlsx", sheet_name="Sheet1")


# In[37]:


print(df4)


# In[25]:





# In[ ]:





# In[ ]:





# In[ ]:




