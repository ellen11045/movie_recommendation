#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


column_names = ['user_id','item_id','rating','timestamp']


# In[5]:


data = pd.read_csv('u.data',sep='\t',names= column_names)


# In[6]:


movie_titles = pd.read_csv('Movie_Id_Titles')


# In[7]:


data = pd.merge(data,movie_titles,on='item_id')


# In[8]:


import matplotlib.pyplot as plt


# In[9]:


import seaborn as sns


# In[10]:


sns.set_style('white')


# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


data.groupby('title')['rating'].mean().sort_values(ascending = False).head()


# In[13]:


data.groupby('title')['rating'].count().sort_values(ascending = False).head()


# In[14]:


ratings = pd.DataFrame(data.groupby('title')['rating'].mean())


# In[15]:


ratings.head()


# In[16]:


ratings['number of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())


# In[17]:


ratings.head()


# In[18]:


sns.jointplot(x='rating',y='number of ratings',data = ratings,alpha = 0.5)


# In[19]:


data.head()


# In[20]:


moviemat = data.pivot_table(index='user_id',columns = 'title',values = 'rating')


# In[21]:


moviemat.head()


# In[22]:


ratings.sort_values('number of ratings',ascending = False).head()


# In[23]:


starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']


# In[24]:


starwars_user_ratings.head()


# In[25]:


moviemat.corrwith(starwars_user_ratings)


# In[26]:


similar_to_starwars = moviemat.corrwith(starwars_user_ratings)


# In[27]:


similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)


# In[28]:


corr_starwars = pd.DataFrame(similar_to_starwars,columns=['Correlation'])


# In[29]:


corr_starwars.dropna(inplace=True)


# In[30]:


corr_starwars.head()


# In[31]:


corr_starwars.sort_values('Correlation',ascending = False).head()


# In[32]:


corr_starwars = corr_starwars.join(ratings['number of ratings'])


# In[33]:


corr_starwars.head()


# In[34]:


corr_starwars[corr_starwars['number of ratings']>100].sort_values('Correlation',ascending = False).head()


# In[35]:


corr_liarliar = pd.DataFrame(similar_to_liarliar,columns=['Correlation'])


# In[36]:


corr_liarliar.dropna(inplace = True)


# In[37]:


corr_liarliar.sort_values('Correlation',ascending = False).head()


# In[38]:


corr_liarliar = corr_liarliar.join(ratings['number of ratings'])


# In[39]:


corr_liarliar.head()


# In[ ]:




