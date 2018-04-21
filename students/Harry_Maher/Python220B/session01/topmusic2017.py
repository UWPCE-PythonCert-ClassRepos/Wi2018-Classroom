
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


music = pd.read_csv("featuresdf.csv")


# In[3]:


music.head()


# In[4]:


music.describe()


# In[11]:


songs = [x for x in list(zip(music.danceability, music.loudness, music.artists, music.name)) if x[0] > .8 and x[1] < -5.0]


# In[12]:


songs


# In[17]:


songs = sorted(songs) # Yeah I should have put them in a different order and used a key, but lazy.


# In[18]:


top_5_songs = songs[::-1][:5]


# In[19]:


for i, j in enumerate(top_5_songs):
    print(f"{i+1}. {j[3]} By: {j[2]}. Danceability: {j[0]}. Loudness: {j[1]} ")

