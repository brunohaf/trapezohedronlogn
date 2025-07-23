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
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
# @lc code=end

#ICE:
# input are the heads of two lists
# output is the head of the merged sorted list
# lists size in range [0, 50]. (Bruteforce feasible)
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
# Edge: 
# - 2 empty lists -> return empty
# - 1 empty list and 1 non empty -> return the non empty
'''
@notes post-mortem=start
# Logic:
# Is head1 or head2 empty?
#   Return empty
# is head1 empty?
#   return head2
# is head2 empty?
#   return head1
# Declare node1 = head1
# Declare node2 = head2
# while(node2 != None): # Always alter list1
#   while(node1 != None and node1.val < node2.val):
#       if node1 == None:
#           node1 = node2
#           break
#       node1 = node1.next
#    node1.next = new ListNode(node2.val, node1.next)
#    node2 = node2.next
#    
# 39 mins pseudo
# Test;
## 1 -> 2 ->4
# node2.val | node1.val  | node1.next | node2.next |  node1 != None and node1.val < node2.val
#     1     |   1       |      2    |       3     |    true and false -> false
#     1     |   2       |      3    |       3     |    true and true -> true 
## list1 = 1 -> 1 -> 2 -> 4
#     3    |   2       |      4    |       4     |    true and true -> true 
## list1 = 1 -> 1 -> 2 -> 3 -> 4
#     4    |   4       |      None    |       None     |   true and true -> true 
## list1 = 1 -> 1 -> 2 -> 3 -> 4 -> 4       
# 23 mins half-ass debug and fixing
@notes post-mortem=start
'''