#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None

df = pd.read_csv(r'C:\Users\quinc\OneDrive\Desktop\John Deere Interview\Counties\Monroe.csv')
pd.set_option('display.max_rows', None)


# In[2]:


df.head()


# In[3]:


# missing data
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))


# In[4]:


df = df.sort_values(by = ['County_name', 'Commodity', 'Townships', 'Date'])
df


# In[5]:


sns.regplot(x="Min_price($)", y="Arrivals_in_ton", data=df, scatter_kws={"color":"red"} ,line_kws={"color": "blue"})
plt.xlabel('Min Price')
plt.ylabel('Arrivals in Ton')
plt.title('Min Price v Arrivals in Ton')


# In[6]:


correlation_matrix = df.corr(method='spearman')


# In[7]:


sns.heatmap(correlation_matrix, annot=True)

plt.title('Initial Correlation')


# In[8]:


df_numerized = df

for col_name in df_numerized.columns:
    if (df_numerized[col_name].dtype == 'object'):
        df_numerized[col_name] = df_numerized[col_name].astype('category')
        df_numerized[col_name] = df_numerized[col_name].cat.codes
        
df_numerized


# In[9]:


df_num_corr = df_numerized.corr()


# In[10]:


correlation_mat = df.apply(lambda x: x.factorize()[0]).corr()

corr_pairs = correlation_mat.unstack()

print(corr_pairs)


# In[11]:


sns.heatmap(df_num_corr, annot=True)
plt.title('Overall Correlation')


# In[12]:


sorted_pairs = corr_pairs.sort_values()

print(sorted_pairs)


# In[13]:


strong_pairs = sorted_pairs[abs(sorted_pairs) < .9]

print(strong_pairs)


# In[ ]:





# In[ ]:




