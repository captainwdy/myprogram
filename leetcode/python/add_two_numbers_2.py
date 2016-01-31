#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#File:add_two_numbers_2.py
#Author: wangdayao(captainwdy@163.com)
#Date: 2016/01/31 13:41:34
#Descrip:https://leetcode.com/problems/add-two-numbers/

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = p = ListNode(0)
        plus = 0
        while l1 or l2:
            tmp_sum = plus
            if l1:
                tmp_sum += l1.val
                l1 = l1.next
            if l2:
                tmp_sum += l2.val
                l2 = l2.next
            p.next = ListNode(tmp_sum % 10)
            p = p.next
            plus = tmp_sum / 10
        if plus:
            p.next = ListNode(plus)
        return l3.next

    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        two_sum = self.list_to_int(l1) + self.list_to_int(l2)
        return self.int_to_list(two_sum)

    def list_to_int(self, l1):
        """change list to int"""
        if l1.next == None:
            return l1.val
        return l1.val + self.list_to_int(l1.next) * 10
    
    def int_to_list(self, num):
        """change int to list"""
        l1 = tmp = ListNode(num % 10)
        num /= 10
        while num:
            tmp.next = ListNode(num % 10)
            tmp = tmp.next
            num /= 10
        return l1


def init_list_node(list1):
    """change list to listnode"""
    l1 = ListNode(list1[0])
    tmp = l1
    for num in list1[1:len(list1)]:
        tmp.next = ListNode(num)
        tmp = tmp.next
    return l1


if __name__ == '__main__':
    list1 = [2,4,3]
    list2 = [5,6,4]
    l1 = init_list_node(list1)
    l2 = init_list_node(list2)
    solution = Solution()
    print solution.list_to_int(l1)
    l3 = solution.addTwoNumbers(l1, l2)
    print solution.list_to_int(l3)

