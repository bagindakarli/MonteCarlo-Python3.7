#!/usr/bin/env python
# coding: utf-8

# In[58]:


import numpy as np

n = 850
total = 200
ndart = 0

hit = 0
for i in range(total):
    x = np.random.rand()
    y = np.random.rand()
    ndart +=1
    if x**2 + y**2 <= 1:
        hit +=1
        
pi = (hit/total)*4
print(pi)
print(hit)

