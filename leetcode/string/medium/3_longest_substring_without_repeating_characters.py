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
-----BEGIN PGP MESSAGE-----

hF4DjxTuSjEZ/v8SAQdAJylz1VEhz6Scczshnff/Icu6KlIupSe4JJhLIa4rFmkw
kF73a1ajBuo9xtOzVG6yz87+cDsvpblYt1uCiwcESIZFjgZA6Uk8NNAWf+t4G5TH
0ukBMDUFEJ08Mn/n6zVkNHIUvfjdu+oPPzqNTC45syDezqlq+NqC9Sxwd/HcKVzf
VOZ8yq8rBsqlTRFv0rXsTbY/VfTT1YXeWMc8DMgCEKtCEyXwV2rskSdbz+kgIcxv
byw6Bu12MiyF11PmfSchfAw6128zqi6kp3N2LXqsylcDajMlgFvtEfw1IH7Yez7S
7ASheqWX18/18BrzRaJfKYkd1eOf9dILukCPDNR0dhzsk3sKI/EIfe3LabFplTgO
RZvoSYNaY1rx3a4lc+tL8da5Vb+bBM+W4La7Buiczbx+uJ39ImbORGT3xH9ds2dj
RgqGQ17s1vMfTw9iALWe97pVuLRZnYuNODo7su8Eb9wTYrTjlTpsSasJwrYwx6f+
CFkzvJWaWk8hF9YEUo0v7N8bj+sfgY0gam53Zyi8C8SRhnFdcJpnD0yAdfAkkNCe
FqWGq6kP8oeqsr6tUR7Xg2ZicIpFbifFi9jDRUIllpGBbArOmvztQKFbcATBuTnS
heRfWeqP+OP8E+S3mokFxU9QxBH3A94JxYBS0zKqBpAMhe0iIhs3IaUPyh3sJY+D
lAmhmQxAVaMJKn7OMpfOUN+IUKdWYV7xGINWdUtHWmfPmHpl3RHJHmeJ562ZYf61
URDmAsReDWQRwJAZ5IIvEZ3oOCR5/r9OHFkJsPe+4QJHZ5hWBOKDB/jMQmn81X6K
72LVPY5AqcXsEM4ONaVvaKl5IUnPTX19mxZLzf6/gTE7w5hiRDmK0JGLciaYM0Ke
/x9ZUTXh9GB0t5rq9UR58/HV6YGJ9rdoTugd2C2apla+BLfCK70xXFaU+q3GUGuW
4ddzBpqIkllFuenAaMYvw1b6IxDMHuEZUM/La9yL+Fd0mkOPmQqbdFfOuw==
=Bfgi
-----END PGP MESSAGE-----
'''