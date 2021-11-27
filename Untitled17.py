#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


file = 'https://raw.githubusercontent.com/alyanien/DATASAINS/main/toyota.csv'
dataset = pd.read_csv(file, sep=',')
dataset.head()


# In[6]:


#MEMPERLIHATKAN KOLOM MODEL, PRICE, DAN TRANSMISSION


# In[8]:


data_1 = dataset[['model','price', 'transmission',]]
data_1.head()


# In[9]:


#MENAMPILKAN HANYA TRANSMISSION AUTOMATIC


# In[31]:


df_automatic = data_1[data_1['transmission'] == 'Automatic']
df_automatic.head()


# In[30]:


#MENAMPILKAN HANYA MODEL COROLLA DENGAN TRANSMISSION AUTOMATIC


# In[60]:


df_model = data_1[(data_1.transmission == "Automatic") & (data_1.model == " Corolla")]
df_model.head()


# In[62]:


#MENCARI RATA RATA HARGA MOBIL COROLLA YANG AUTOMATIC


# In[63]:


df_model['price'].mean()


# In[64]:


df_model['price'].max()


# In[65]:


df_model['price'].min()


# In[66]:


#MENCARI TAU MOBIL COROLLA MANA DENGAN HARGA MAX


# In[70]:


df_max = dataset[(dataset.transmission == "Automatic") & (dataset.model == " Corolla")& (dataset.price == 29450)]
df_max.head()


# In[71]:


#MENCARI TAU MOBIL COROLLA MANA DENGAN HARGA MIN


# In[72]:


df_min = dataset[(dataset.transmission == "Automatic") & (dataset.model == " Corolla")& (dataset.price == 899)]
df_min.head()

