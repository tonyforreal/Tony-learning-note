#!/usr/bin/env python
# coding: utf-8

# In[3]:


def quicksort(x):
    if len(x)<=1:
        return x
    else:
        pivot=x[0]
        less=[i for i in x[1:] if i<pivot]
        equal=[i for i in x[1:] if i==pivot]
        more=[i for i in x[1:] if i>pivot]
        return quicksort(less)+quicksort(equal)+[pivot]+quicksort(more)
    


# In[4]:


alist=[5,4,2,9,7,1,0,4]


# In[6]:


quicksort(alist)


# In[ ]:




