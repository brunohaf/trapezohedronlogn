#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (42.54%)
# Likes:    26216
# Dislikes: 1918
# Total Accepted:    6.3M
# Total Submissions: 14.9M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
#
# Example 1:
#
#
# Input: s = "()"
#
# Output: true
#
#
# Example 2:
#
#
# Input: s = "()[]{}"
#
# Output: true
#
#
# Example 3:
#
#
# Input: s = "(]"
#
# Output: false
#
#
# Example 4:
#
#
# Input: s = "([])"
#
# Output: true
#
#
# Example 5:
#
#
# Input: s = "([)]"
#
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
#
#
#

# @lc code=start
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_table: dict[str, str] = {"}": "{", ")": "(", "]": "["}
        open_parentheses: set[str] = set(parentheses_table.values())
        stack: deque[str] = deque()
        if len(s) & 1:
            return False
        for i in range(0, len(s)):
            if s[i] in open_parentheses:
                stack.appendleft(s[i])
                continue
            if not len(stack) or parentheses_table.get(s[i], "") != stack.popleft():
                return False
        return len(stack) == 0

    # @lc code=end


#  [{()}]
#         stack (LIFO):
#         push [
#             push {
#                 push (
#                 pop )
#             pop }
#         pop ]
sol = Solution()
assert sol.isValid("))") == False
assert sol.isValid("()") == True
assert sol.isValid("[{()}]") == True
assert sol.isValid("[{(})]") == True

"""
@notes post-mortem=start
-----BEGIN PGP MESSAGE-----

hF4DjxTuSjEZ/v8SAQdAZyaiwZoMh1D6wFvBZgOtUukH7DE7rvTKDXKKdWFQKSUw
Ab6eLgeTskfSg68ULmpkS2eMwSIyE/ycpQy71GmS9S5VpnwBVwBiFm3I3f6Pl56t
0sAmAXv8ahdT2bcYLlU3TN7S/rcke/3IlDW3Bu8dM895yUF0WpZuKKUWy962ZIky
+I90XlmThjPytOTsMMZcDn5LmGV2+gSpWZ3o3F8juFr/QLpGpjCgqabufo6gzcIQ
XkB5tfB7GqWtY/DoO/d/EWeFwXjpeIHKWWOEi/2vpFJ+jnEgTrwf/YRUlehuajei
Jm+zuw0huDX9Ht3qRti1jDENBCcTiuRExPPhvETeQlF6pqb/2D14oWm26MCOGSEv
IRZR9Q69t+Z5ecG9XMNL0z46uDUj9wlV4F/wkcoJnXpeZ//bppldJTs=
=/J/z
-----END PGP MESSAGE-----
@notes post-mortem=end
"""
