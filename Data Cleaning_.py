#!/usr/bin/env python
# coding: utf-8

# In[106]:


import pandas as pd
df = pd.read_excel('/Users/gangasingh/Documents/Final.xlsx')


# In[107]:


df


# In[108]:


df['BATTING'] = df['BATTING'].astype(str)

# Use .loc to remove '(c)' and other similar substrings from 'BATTING' column
df.loc[:, 'BATTING'] = df['BATTING'].str.replace(r'\s*\(c\)†*', '', regex=True)


# In[109]:


df = df.rename(columns = {'Unnamed: 1': 'Out'})


# In[110]:


#Dropping nan values
df = df.dropna()


# In[111]:


df


# In[112]:


df4 = df.copy()


# In[113]:


#Converting datatype object to int
df4.loc[:, 'R'] = pd.to_numeric(df4['R'], errors='coerce')


# In[114]:


df4.loc[:, 'R'] = df4['R'].astype('int')


# In[116]:


players = df4.groupby('BATTING')['R'].sum()
top_10 = players.sort_values(ascending=False).head(10)
top_10


# In[117]:


players = df4.groupby('BATTING')['R'].mean()
top_10 = players.sort_values(ascending=False).head(10)
top_10


# In[128]:


df7 = df4.copy()
df7['SR'] = pd.to_numeric(df7['SR'], errors='coerce')
df7.dropna(subset=['SR'], inplace=True)


# In[129]:


players_avg = df7.groupby('BATTING')['SR'].mean()
highest_avg = players_avg.sort_values(ascending=False).head(10)
highest_avg


# In[130]:


df7


# In[131]:


df7.to_excel(r'/Users/gangasingh/Documents/python/WebScraping/IPL_2024/IPL_2024_All_Matches_Summary.xlsx')


# In[ ]:




