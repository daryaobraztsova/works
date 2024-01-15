#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import ttest_ind
import seaborn as sns
games=pd.read_csv("C:\\Users\\Даша\\Downloads\\games.csv")
games.head(10)
games.info()


# In[12]:


def percent_hbar(df, old_threshold=None):
    percent_of_nulls = (df.isnull().sum()/len(df)*100).sort_values().round(2)
    threshold = percent_of_nulls.mean() 
    ax = percent_of_nulls.plot(kind='barh', figsize=(17, 8), title='% of NaN (из {} строк)'.format(len(df)), color='#86bf91', legend=False, fontsize=12)
    ax.set_xlabel('Count of NaN')
    i=0
    dict_percent = dict(percent_of_nulls)
    for k in dict_percent:
        color = 'blue'
        if dict_percent[k] > 0:
            if dict_percent[k] > threshold:
                color = 'red'
            ax.text(dict_percent[k]+0.1, i + 0.09, str(dict_percent[k])+'%', color=color, fontweight='bold', fontsize='large')
        i += 0.98
    if old_threshold is not None:
        pit.axvline(x=old_threshold,linewidth=1, color='r', linestyle='--') 
        ax.text(old_threshold+0.3, 10, '{0:.2%}'.format(old_threshold/100), color='r', fontweight='bold', fontsize='large')
                
        pit.axvline(x=threshold, linewidth=1, color= 'green', linestyle='--')
        ax.text(threshold+0.3, 7, '{0:.2%}'.format(threshold/100), color ='green', fontweight='bold', fontsize= 'large')
    else:
        plt.axvline(x=threshold,linewidth=1, color='r',linestyle='--')
        ax.text(threshold+0.3, 7, '{0:.2%}'.format(threshold/100), color='r', fontweight='bold', fontsize='large') 
    ax.set_xlabel('')
    return ax, threshold
plot, threshold = percent_hbar(games)


# In[13]:


games.query('Critic_Score.isnull() & Rating.isnull() & User_Score.isnull()')


# In[14]:


games.columns = games.columns.str.lower()


# In[15]:


games['user_score'].unique()


# In[17]:


games[games['user_score'] == 'tbd']


# In[25]:


games['user_score'] = games['user_score'].replace('tbd', np.NaN)
games['user_score'] = games['user_score'].astype('float')

games['critic_score'] = games['critic_score'].fillna(-1)
games['user_score'] = games['user_score'].fillna(-1)

print('Количество пропусков в столбце critic_score - {}'.format(games['critic_score'].isnull().sum()))
print('Количество пропусков в столбце user_score - {}'.format(games['user_score'].isnull().sum()))


# In[26]:


percent_hbar(games, threshold)


# In[29]:


games['sales_total'] = games['na_sales'] + games['eu_sales'] + games['jp_sales'] + games['other_sales']
def create_any_bar(groupby_column, func, y='name'):
    plt.style.use('seaborn-v0_8')
    df_to_plot = games.groupby (groupby_column) [y]
    if func == 'count':
        df_to_plot_calculated = df_to_plot.count()
        figsize = (15,5) 
        plot = df_to_plot_calculated.plot(kind='bar', y=y, figsize=figsize, ec='black')
                                         
                                        
    elif func == 'sum':
        df_to_plot_calculated = df_to_plot.sum().sort_values()
        figsize = (15,10)
        plot = df_to_plot_calculated.plot(kind='barh', y=y, figsize=figsize, ec='black')

create_any_bar('platform','sum','sales_total')


# In[30]:


create_any_bar ('platform','sum','sales_total')


# In[31]:


games.groupby('platform')['sales_total'].sum().to_frame('sales_total').sort_values(by='sales_total', ascending=False).head(10)


# In[ ]:




