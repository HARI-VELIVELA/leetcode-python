#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = list(s.split())
        n = len(s)
        if n==0:
            return 0
        else:
            return len(s[n-1])
        

