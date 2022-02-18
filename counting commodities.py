#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Libaries
import pandas as pd
import openpyxl


# In[2]:


df = pd.read_csv(r'C:\Users\quinc\OneDrive\Desktop\John Deere Interview/John_deere_python_dirty.csv')


# In[3]:


df.head()


# In[10]:


counting = df.groupby(['County_name'])['Commodity'].nunique()


# In[11]:


counting.to_excel(r"C:\Users\quinc\OneDrive\Desktop\John Deere Interview/Counting.xlsx", sheet_name="Sheet1")


# In[ ]:




