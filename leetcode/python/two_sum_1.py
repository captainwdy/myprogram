#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#File:two_sum_1.py
#Author: wangdayao(captainwdy@163.com)
#Date: 2016/01/29 13:44:38
#Descrip:https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1 in range(len(nums)):
            for index2 in range(len(nums))[-1:index1:-1]:
                if nums[index1] + nums[index2] == target:
                    return (index1 + 1, index2 + 1)

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict((value, index) for index, value in enumerate(nums))
        for index, value in enumerate(nums):
            if target - value in dic:
                if index == dic[target-value]:
                    continue
                return (index + 1, dic[target-value] + 1)
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index, value in enumerate(nums):
            if target - value in dic:
                return (dic[target-value] + 1, index + 1)
            dic[value] = index

if __name__ == '__main__':
    nums_array = [[2,7,11,15], [3,2,4]]
    target_array = [9,6]
    solution = Solution()
    for index, nums in enumerate(nums_array):
        target = target_array[index]
        print solution.twoSum(nums, target)

