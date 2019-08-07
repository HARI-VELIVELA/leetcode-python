#!/usr/bin/env python
# coding: utf-8

# In[27]:


"""Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself."""

class Solution(object):
    def plusOne(self, digits):
        digits = [str(i) for i in digits]
        digits = int("".join(digits))
        digits = digits+1
        return [int(i) for i in str(digits)]


# In[ ]:




