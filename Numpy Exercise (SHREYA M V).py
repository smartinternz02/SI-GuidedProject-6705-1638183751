#!/usr/bin/env python
# coding: utf-8

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# In[1]:


import numpy as np


# #### Create an array of 10 zeros 

# In[5]:


np.zeros(shape=10)


# #### Create an array of 10 ones

# In[3]:


np.ones(shape=10)


# #### Create an array of 10 fives

# In[6]:


np.ones(10)*5


# #### Create an array of the integers from 10 to 50

# In[7]:


np.arange(10,51)


# #### Create an array of all the even integers from 10 to 50

# In[8]:


np.arange(10,51,2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[14]:


arr=np.arange(0,9).reshape(3,3)
arr


# #### Create a 3x3 identity matrix

# In[11]:


np.eye(N=3)


# #### Use NumPy to generate a random number between 0 and 1

# In[12]:


np.random.rand(1)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[15]:


np.random.randn(5,5)


# #### Create the following matrix:

# In[17]:


np.linspace(start=0.01,stop=1,num=100).reshape(10,10)


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[18]:


np.linspace(start=0,stop=1,num=20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[16]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[23]:


mat[2:,1:]


# In[19]:


mat[3,4]


# In[24]:


mat[0:3,1].reshape(3,1)


# In[25]:


mat[4,0:]


# In[26]:


mat[3:,0:]


# ### Now do the following

# #### Get the sum of all the values in mat

# In[20]:


mat.sum()


# #### Get the standard deviation of the values in mat

# In[21]:


np.std(mat)


# #### Get the sum of all the columns in mat

# In[22]:


mat.sum(axis=0)


# 
