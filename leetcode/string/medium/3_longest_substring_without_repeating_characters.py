#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (36.88%)
# Likes:    42290
# Dislikes: 2056
# Total Accepted:    7.6M
# Total Submissions: 20.7M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without duplicate
# characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# 
# 
#

# @lc code=start
class Solution:
    def getSubstringLen(self, s: str, end: int, start: int = 0) -> str:
        substring = {}
        for i in range(start, end):
            c = s[i]
            if substring.get(c, False): 
                return len(substring.keys())
            substring[c] = True
        return len(substring.keys())
        

    def lengthOfLongestSubstring(self, s: str) -> int: 
        if not len(s):
            return 0
        # bruteforce: I will consider there's only 1 longest substr.
        longest_len = 0
        for i, c in enumerate(s):
            substr_len = self.getSubstringLen(s, len(s), i)
            if substr_len > longest_len:
                longest_len = substr_len
        return longest_len

# @lc code=end

# sol = Solution()
# assert sol.lengthOfLongestSubstring("abcabcbb") == 3
# assert sol.lengthOfLongestSubstring("bbbbb") == 1
# assert sol.lengthOfLongestSubstring("pwwkew") == 3
# assert sol.lengthOfLongestSubstring("") == 0
# assert sol.lengthOfLongestSubstring(" ") == 1
# assert sol.lengthOfLongestSubstring("          ") == 1
# print("SUCCESS!")

## input: 
## s - string: 0 < len(s) < 50.000 | \w, \d, \s and symbols.
#
## longest substring without duplicated chars
## at least O(n) because I need to check all possibilities
#
## subproblems:
## 1 - iterate s from 0 to len(s)-1.
## 2 - build one substrings 
##      - iterate from i storing the chars
##      - stop if char is already stored.
##      - save substring and its len.
## 3 - repeat 2, incrementing i until i == len(s)-1
#
## edge caes:
## len(s) == 0
## many/all duplicated chars? worst case O(n)
## more than one longest substring?
#
## toolbox:
## reusable hashmap for subproblem 2.
## 

'''
@notes post-mortem=start
-----BEGIN PGP MESSAGE-----

hF4DjxTuSjEZ/v8SAQdAIOLtuSJD/eyKNzcPPh2N2WaK0CEglGysL+XRPnpfwwYw
NulplL60xxLr0aRPUHxPUPf/teuvRPbFSeuHnQiABm7YJmPYEKmoabaZvHafe5wd
0ukBBirMhBV6aniAuHqSf35m6lGBWl9jnPMobS2hxOvWOFoQMNcMPZll8Gm1Irhe
duRqzgFslK90dpYMk6iHkgfqfi7E65XfWRtxVStYuCS4/FYNPnGrJJ6cx4BvoUgl
wOiyJTrACl3ZOyZGxibjoEXR3k4ICa6rGKDEuh9QuPkOOabSX9zjPjNMf1L2svu5
7p0c1pKZbkgQnm3MFpTy7aSqvkEhUfBIBvSK79P9i5ZTf14hgFNRIkrXMM67fu+L
0clkmXeoH1+HDd2VJvzrYsfgwfz0rgGBrJyi+x+pVrV+9WwBLEIG06k06B5g8OAz
TehReo/yUA3/STrxTar+1dQaDefZEWjzMQJpezRp5n0NPZ4FUhuTRwwkXzDWt8c1
9qr3HJ1kKtA4LezTvnrnzinH8GwR5ph+9AiMXl+I8WI5ksh1WGM8RoCEHqGebc+E
S5okvlp772AmL+1jNHDt9OfsVemxPAi3AMKqfcv/gcdpK0usdvpoahO6ipk9dU37
eHLql8nQeFH+g9b9M6gM85qqtFkvq5j59i5O8cOwS2rWMZi67LIR671i6pUQuINd
3DSwhjsbuGWF+O1f+eEcrI/8Ac+aHOWxWgx4qBGDm7h5P2R6KKUAXZj5hOtegYtY
kFhQN1Ybg+FIdwE0kLfyzUqdbKPqP7FQxzZQZrJXlGab1YH5M3yTJ5pVDibqn5IX
DM6HuJg645sNpZ82J58J7UXL8UfvvGv9n4x/dQLynnRy0/qyOIXl6iB7vEd6S2ll
cuupjoXgaA5pw0LkPQ/1+CQ0woy0jtMbpjJcma89jpvRZFpwbK199Y3aqoHc6v3i
zmgJFfPnuZOd3cr53oN/jaqJvzY=
=9Gz5
-----END PGP MESSAGE-----
@notes post-mortem=end
'''
