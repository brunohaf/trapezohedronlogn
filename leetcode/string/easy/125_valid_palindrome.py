#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (51.30%)
# Likes:    10610
# Dislikes: 8567
# Total Accepted:    4.5M
# Total Submissions: 8.7M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. Alphanumeric characters include letters and
# numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
#
# Example 1:
#
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
#
# Example 2:
#
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
# Example 3:
#
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters.
# Since an empty string reads the same forward and backward, it is a
# palindrome.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
#
#
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumerics: set[str] = set("abcdefghijklmnopqrstuvxywz1234567890")
        left, right = 0, len(s) - 1
        s = s.lower()
        while left < right:
            while s[left] not in alphanumerics and left < right:
                left += 1
            while s[right] not in alphanumerics and left < right:
                right -= 1
            if s[right] != s[left]:
                return False
            right -= 1
            left += 1
        return True


# @lc code=end
sol = Solution()
assert sol.isPalindrome(s="race a car") == False
assert sol.isPalindrome(s=" ") == True
"""
@notes post-mortem=start
-----BEGIN PGP MESSAGE-----

hF4DjxTuSjEZ/v8SAQdAHnTQopccHZ9kLbXOkTSYdrxC5rHPvtvjrADXbASG9gww
Y8lTkGWvzwMHSR44zUEUZC5SKvFT0W93MqJ7sPvyrHtgnm5oiUa5BPm90S/do2xn
0ksBe4x3BcOvbuJt33sLNRwQG0awSjbZJUGl6Mdc/5/h9RD5qmoYE5+eV/aCl4wH
UEkw/n5kW4BYRbgRDCVCml66PGHwqGfUueIqk3o=
=DOuT
-----END PGP MESSAGE-----
@notes post-mortem=end
"""
