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
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars: set[str] = set()
        max_len, left = 0, 0
        for right in range(len(s)):
            while s[right] in seen_chars:
                seen_chars.remove(s[left])
                left += 1
            seen_chars.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len


# @lc code=end

sol: Solution = Solution()
assert sol.lengthOfLongestSubstring(s="") == 0
assert sol.lengthOfLongestSubstring(s="          ") == 1
assert sol.lengthOfLongestSubstring(s="bbbbb") == 1
assert sol.lengthOfLongestSubstring(s="au") == 2
assert sol.lengthOfLongestSubstring(s="dvdf") == 3
assert sol.lengthOfLongestSubstring(s="abcabcbb") == 3

"""
@notes post-mortem=start
-----BEGIN PGP MESSAGE-----

hF4DjxTuSjEZ/v8SAQdA5mWDYmC2tUBfsozkl8o5PGsIkuyuSep0zEjcWtZ1xG4w
zG5hbaiZuadLkE9JkKCPvCATUq5Qkyi1toHjTcsyDJUlMc7pacAfhHCz6n2DM1Hc
0uoBzlI2PjSIW1v7lh08O7ol76UjzrTDW23ls7LyuH8iVybHfVCEWZcqVowKXy/q
twNiPqQbySzJUQqioC2KzOYD62LVOLdMWPuAOMh99Ctl54tjq8bUVbTDHNFS5IH7
MuvcHjJSfVzMDdQyiIPMRZgC7B2fwuusYi3E1Tpr4iCzawaT4/YyZimOJ+s3Xxzm
tnffQXgsOUAUdDceah156eaLE+57XNxMXWmOe1opliCuY/6pOccHGcMhuueqdqN9
4VpJFVuf/rZi+NGXQekMxUlpUaagt4mD6gEHs+wBHUIm1NvzcIpCqinY38ZLIoR6
JippLiNcdnOP3WtESeqmkKd730xBvMaTH7GagECbD64t5wC0D4rqoIYgteZCvyuX
8p1kkbHTqw85vY9/wVbGhNNwdlD8h4u+k/MWXpDAENtZSso2s8VMwE568YMcubPQ
Qkm8b/+8RXXQxMV6QvHuKNSCQqIcBQA1A7YgHTiZRwgLC4U42GvzlnsWQ0N7FC0a
Lg4Ru0yHnz/OiDETycexGtMGT7JsT2PArQ6jRUYU6DFrYovLhOeeJf2Kvvyu4KDg
aqaic6AAxHMhr3lgGBpgQFr9PR0d7MAj90YuksAAEkYi72E0NAnpMDzxGiT1puIo
AsE/aY7Eu+A5AG9H5Wt7jQ8PbF7o3/v6RIaXJiOJ3pvzmydjMmt3Ldxt7Kbl5/BS
mB7ZLafMu5t0PmVSu8+NVw09Tx3dBh2WzAihqgcNFDYv4UG7kUc5/IHV8DojADcr
8bWKcxnCMnGl5UVf/ZKuYUI/83kYpOhjNRy8Ws973kJoLhkUDI56Qj0qgig32p3m
TINk1dGK3rA+W2L4p6TK5RdIuwH5Q9myX8Qs8AFBXVkggOtJg+7Ngpyv+nfiUMic
X9IojvGEFamIWwDRUGHcY9DN0vzOPVrMtehxN3biMSdBgRjHK2eCWEB26Io+aUHW
0y55juqoGYYvNPoszE9VKLyiHG+wsPptyOunisr8h5gh/QJVNznQjkVpH3SEmAmz
P6ECZQkX4lJTY90CKt0J5Hf554aKpSyBpbQNfU9nLYMRSMdiZ+rrfdvF4nBNtT3v
IUCLRBH2FApI2MzaRHPgmPi5DgEZdEN6KrZqJagMe53jZHnfga3XRkun2D507DV6
/OfyEKk0b/4v5+it3spPiHd/5yoCGrL8+LhOmCnMBFFGzO6iGf3Mq9u/ie+ePJhD
1+I4E/C3oQZZYVdzbEXsF9evFJ/V0sWE5Hb9luEB5UYJtQWzQ2d1Uq2xmhVa8twQ
2TPSziIAzoGP6LWXDJRk9QGRiw4mEu2gIIrD7qPJojFDPYCrmhjzdrXQ393m9UQx
LhRWx6RrRhOpXzrBTRx6eJEIFDp5A/5qwg6r079RyqBCu49RNpB1
=y9R/
-----END PGP MESSAGE-----
@notes post-mortem=end
"""
