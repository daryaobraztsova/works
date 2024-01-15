#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
project = pd.read_csv('C:\\Users\\Даша\\Downloads\\data (1).csv')
#project.head(15)
project.info()



# In[13]:


project ['total_income'] = project ['total_income'].fillna(project ['total_income'].mean())
project ['dob_years'] = project ['dob_years']. replace(0, 43.29337979094077)
project.dropna(axis = 'columns', inplace = True)
def child_final(i):
    if i == 0:
        return 0
    if i == 20: 
        return 2
    if i == 1: 
        return 1
    if i == 3: 
        return 3
    if i == 4: 
        return 4
    if i == 5: 
        return 5
    else:
        return 2
project['children_final'] = project['children'].apply(child_final)
project.info


# In[14]:


project.isnull().sum()


# In[17]:


project['dob_years'] = project['dob_years'].astype('int')
project ['total_income'] = project ['total_income'].astype('int')
project.head(15)


# In[ ]:




