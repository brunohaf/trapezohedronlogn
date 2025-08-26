#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (64.85%)
# Likes:    5459
# Dislikes: 533
# Total Accepted:    1.7M
# Total Submissions: 2.6M
# Testcase Example:  '"a"\n"b"'
#
# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
#
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
#
# Constraints:
#
#
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote and magazine consist of lowercase English letters.
#
#
#

# @lc code=start


from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_table: defaultdict[str, int] = defaultdict(lambda: 0)
        for char in magazine:
            magazine_table[char] += 1
        for char in ransomNote:
            if magazine_table.get(char, 0):
                magazine_table[char] -= 1
            else:
                return False
        return True


# def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#     ransomNoteCounter: Counter[str] = Counter(ransomNote)
#     magazineCounter: Counter[str] = Counter(magazine)
#     for char, count in ransomNoteCounter.items():
#         if magazineCounter.get(char, 0) < count:
#             return False
#     return True


# @lc code=end
solution: Solution = Solution()
assert solution.canConstruct(ransomNote="a", magazine="b") is False
assert solution.canConstruct(ransomNote="aa", magazine="ab") is False
assert solution.canConstruct(ransomNote="aa", magazine="aab") is True
"""

"""
