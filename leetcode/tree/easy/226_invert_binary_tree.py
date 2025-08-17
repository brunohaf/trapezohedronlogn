#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# https://leetcode.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (79.17%)
# Likes:    14748
# Dislikes: 246
# Total Accepted:    2.7M
# Total Submissions: 3.4M
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# Given the root of a binary tree, invert the tree, and return its root.
#
#
# Example 1:
#
#
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
#
#
# Example 2:
#
#
# Input: root = [2,1,3]
# Output: [2,3,1]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
#


from collections import deque
from typing import Any, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        nodestack: deque[Optional[TreeNode]] = deque([root])
        while len(nodestack):
            node = nodestack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                nodestack.append(node.left)
            if node.right:
                nodestack.append(node.right)
        return root


# @lc code=end


tree: Any = Solution().invertTree(
    root=TreeNode(
        val=4,
        left=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)),
        right=TreeNode(val=7, left=TreeNode(val=6), right=TreeNode(val=9)),
    )
)
# in a array represented binary tree we have teh properties:
# 2i+1 = left node
# 2i+2 = right node
# iterate through the array, inverting 2i+1 with 2i-1.
# Edge cases: empty array, is it unbalanced? if so check positions before acessing.

# TODO:
#   - Retry this from scratch
