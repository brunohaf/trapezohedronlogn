#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (66.73%)
# Likes:    13156
# Dislikes: 434
# Total Accepted:    4.9M
# Total Submissions: 7.3M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
# 
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# 
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# 
# 
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    def isNagaram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freqs = {"s": {}, "t": {}}
        for i in range(0,len(s)):
            freqs["s"][s[i]] = freqs["s"].get(s[i],0)+1
            freqs["t"][t[i]] = freqs["t"].get(t[i],0)+1
        return freqs["s"] == freqs["t"]
# @lc code=end

sol = Solution()
assert (sol.isAnagram("anagram", "nagaram") == True)
assert (sol.isAnagram("rat", "car") == False)
assert (sol.isAnagram("aaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaa") is True)
assert (sol.isAnagram("z", "b") == False)
assert (sol.isAnagram("anagram", "car") == False)

# Goal: Tell if s and t have the same characters occuring a equal amount of times.
# if len(s) != len(t) -> False
# Sort s and t
# Return sorted_s == sorted_t O(n log n)

# Input: s = "anagram", t = "nagaram"
# Compare len(s) == 7 == len(t)
# Quicksort(s); s = aaagrmn
# Quicksort(t); t = aaagrmn
# Returm s == t ? "aaagrmn" == "aaagrmn" ? -> True

# Input: s = "rat", t = "car"
# Compare len(s) == 3 == len(t)
# Quicksort(s); s = art
# Quicksort(s); t = acr
# Returm s == t ? "art" == "acr" ? -> False
