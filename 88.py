#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        m= len(nums1)-n
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
        return nums1

