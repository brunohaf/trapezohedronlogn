#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (66.91%)
# Likes:    23522
# Dislikes: 2309
# Total Accepted:    5.3M
# Total Submissions: 8M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made by splicing
# together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
#
# Example 1:
#
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
#
# Example 2:
#
#
# Input: list1 = [], list2 = []
# Output: []
#
#
# Example 3:
#
#
# Input: list1 = [], list2 = [0]
# Output: [0]
#
#
#
# Constraints:
#
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
#
#
#

# @lc code=start
# Definition for singly-linked list.
# from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        node1, node2 = list1, list2
        dummy = ListNode(-1, None)
        current = dummy
        while node1 or node2:
            if not node2:
                current.next = node1
                return dummy.next
            if not node1:
                current.next = node2
                return dummy.next
            if node1.val >= node2.val:
                current.next = node2
                node2 = node2.next
            else:
                current.next = node1
                node1 = node1.next
            current = current.next
        return dummy.next


# @lc code=end

list1 = ListNode(1, ListNode(2, ListNode(4, None)))
list2 = ListNode(1, ListNode(3, ListNode(4, None)))
assert Solution().mergeTwoLists(None, list2) == list2
assert Solution().mergeTwoLists(list1, None) == list1
assert Solution().mergeTwoLists(None, None) is None
Solution().mergeTwoLists(list1, list2)

# ICE:
# input are the heads of two lists
# output is the head of the merged sorted list
# lists size in range [0, 50]. (Bruteforce feasible)
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
# Edge:
# - 2 empty lists -> return empty
# - 1 empty list and 1 non empty -> return the non empty
"""
@notes post-mortem=start
-----BEGIN PGP MESSAGE-----

hF4DjxTuSjEZ/v8SAQdAOjws2oUx1iADYdF8d4VuQdPK4kboC6pVgnMgISRHYxcw
wkYhuqqjWoIVW2i2ASiFtoZgdorN5NRjZ9sEoTh7SdDnyQST8MWkvtFuTCnSt2Vp
0sDlARtyAlJXqWyHqicPV9OZjWaGp956RX4FysuWLoGsAudayRh0bfw7JlNWiYTF
I8uovbQ2IpIRCsopm4yL8Qv6HZuDr8gKlAWg9TAUyZQaamf443HQWLBpRgBPU18a
oeFHcQieIA0Mo5dbCUdyZgFHrmCg7DbRLkrQxg9R5YIBzdbzd2FSHjZtu6esWJnN
v8fJEFugAAQ7A4aPW2IkVoNir4VQwOgU17jMyLmswdF6tGrq2+sFMeC8w0ri5jG8
UKaVKlJv9caKjfajjH/gql7ff0GbjR3RQQtFi5qmJAWucEDq4ZUC4Ao1p9v2Gc0c
c0PE7Tk7NuYr6MZfvxKbGc0NlO70T6fxIS6+UhN6OjSwSLKAoHP73NytDBBq9y9W
20fsnpSzFngpIzFjUUQCxaxW20kTVdB2L0Nlo83cZEzDbE0njNmtQ8Fr1hC0XEBC
h6bSv5zdUTtQmHp0eseNCaYFpxYYYGpV+esX5RT+gSGqySW/9NHcSU/FabKMtL6d
XE6+7qb2pgYZB9RYmXYtvkdnFtaWTLgwVcl1ozmhbA+HrWqodHzAtw==
=y9ql
-----END PGP MESSAGE-----
@notes post-mortem=end
"""
