#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#File:two_sum_1.py
#Author: wangdayao(captainwdy@163.com
#Date: 2016/01/29 13:44:38
#Descrip:

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1 in range(len(nums)):
            for index2 in  range(len(nums))[-1:index1:-1]:
                if nums[index1] + nums[index2] == target:
                    return (index1 + 1, index2 + 1)

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    solution = Solution()
    print solution.twoSum(nums, target)

