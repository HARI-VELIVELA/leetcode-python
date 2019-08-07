#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array."""

class Solution(object):
    def searchInsert(self, a, t):
        if t ==0:
            return 0
        if t in a:
            return a.index(t)
        else:
            for i in range(len(a)):
                if a[i]<t:
                    i+=1
                else:
                    return i
            return i


# In[ ]:




