#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (52.83%)
# Likes:    16720
# Dislikes: 1518
# Total Accepted:    4.1M
# Total Submissions: 7.8M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given head, the head of a linked list, determine if the linked list has a
# cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can
# be reached again by continuously following the next pointer. Internally, pos
# is used to denote the index of the node that tail's next pointer is connected
# to. Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return
# false.
#
#
# Example 1:
#
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to
# the 1st node (0-indexed).
#
#
# Example 2:
#
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to
# the 0th node.
#
#
# Example 3:
#
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
#
#
# Constraints:
#
#
# The number of the nodes in the list is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked-list.
#
#
#
# Follow up: Can you solve it using O(1) (i.e. constant) memory?
#
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow: ListNode = head
        fast: ListNode = head
        while slow or fast:
            if not slow.next or not fast.next or not fast.next.next:
                break
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# @lc code=end
"""
@notes post-mortem=start
-----BEGIN PGP MESSAGE-----

hF4DjxTuSjEZ/v8SAQdAQzEwdJnfjyeloLYdsxmHFXIgIQeoQqgIG7wQ4Y58jV8w
ZycCiTqchVKkzMZC3K0Jl44Mztizog6sM3AW4WJVsV0wlA2nsNnupDfGfS4wnX72
0oQB32kk6wY05dioSKyKo6z18pI7DUOAGs8fFFospxqoeJyMj0v62zNrG7AOx722
fBuySbF/0AQAb0QdvkrjhyFgXVDBwevNIYVAQ8JfJbqcqhyhQdEeihi12WTbSedG
4dbMvhFF6LdBv+99kqiZPVMKYllQuQ4UHsjts2i7ApvbjTkOoDE=
=rexi
-----END PGP MESSAGE-----
@notes post-mortem=end
"""
