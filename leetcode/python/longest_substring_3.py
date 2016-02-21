#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#File:longest_substring_3.py
#Author: wangdayao(captainwdy@163.com)
#Date: 2016/02/21 18:43:59
#Descrip: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        time limit exceeded
        """
        index_begin = index_end = 0  #不包含遍历时最后一个的子串下标
        index_2_begin = 0            #包含最后一个字符的字串开始下标
        index = 0
        while index < len(s):
            if s[index] not in s[index_2_begin:index]:
                if index_end - index_begin < index + 1 - index_2_begin:
                    index_begin = index_2_begin
                    index_end = index + 1
                index += 1
            else:
                index_2_begin += s[index_2_begin:index].find(s[index])+1
                index = index_2_begin

        #print index_begin,index_end
        return index_end - index_begin

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        index_begin = index_end = 0  #不包含遍历时最后一个的子串下标
        index_2_begin = 0            #包含最后一个字符的字串开始下标
        index = 0
        while index < len(s):
            if s[index] not in s[index_2_begin:index]:
                if index_end - index_begin < index + 1 - index_2_begin:
                    index_begin = index_2_begin
                    index_end = index + 1
                index += 1
            else:
                index_2_begin += s[index_2_begin:index].find(s[index])+1

        print index_begin,index_end
        return index_end - index_begin

if __name__=='__main__':
    #s = "abcabcbb"
    #s = "bbbbbb"
    s = "abcabcdaefght"    
    solution = Solution()
    print solution.lengthOfLongestSubstring(s)
    
