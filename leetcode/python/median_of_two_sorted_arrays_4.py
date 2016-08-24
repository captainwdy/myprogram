#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#File:median_of_two_sorted_arrays_4.py
#Author: wangdayao(captainwdy@163.com)
#Date: 2016/08/22 10:22:41
#Descrip:https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findkth(self, nums1, n, nums2, m, k):
        """find k th"""
        if n > m:
            return self.findkth(nums2, m, nums1, n, k)
        if n == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0]) 
        pa = min(k/2, n)
        pb = k - pa
        if nums1[pa-1] < nums2[pb-1]:
            return self.findkth(nums1[pa:], n-pa, nums2, m, k-pa)
        elif nums1[pa-1] > nums2[pb-1]:
            return self.findkth(nums1, n, nums2[pb:], m-pb, k-pb)
        else:
            return nums1[pa-1]
        
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        k = n + m
        if k % 2 == 0:
            return (self.findkth(nums1, n, nums2, m, k/2) + self.findkth(nums1, n, nums2, m, k/2+1)) / 2.0
        else:
            return self.findkth(nums1, n, nums2, m, k/2+1)

if __name__ == '__main__':
    solution = Solution()
    nums1 = [4]
    nums2 = [1,2,5]
    print solution.findMedianSortedArrays(nums1, nums2)
                                            
