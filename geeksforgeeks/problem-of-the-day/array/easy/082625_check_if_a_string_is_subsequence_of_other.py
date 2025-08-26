"""
    - https://www.geeksforgeeks.org/problems/given-two-strings-find-if-first-string-is-a-subsequence-of-second/1
Check if a String is Subsequence of Other
Difficulty: Easy
Accuracy: 51.68%
Submissions: 29K+
Points: 2

Given two strings s1 and s2. You have to check that s1 is a subsequence of s2 or not.
Note: A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

Examples:

Input: s1 = "AXY", s2 = "YADXCP"
Output: false
Explanation: s1 is not a subsequence of s2 as 'Y' appears before 'A'.

Input: s1 = "gksrek", s2 = "geeksforgeeks"
Output: true
Explanation: If we combine the bold character of "geeksforgeeks", it equals to s1. So s1 is a subsequence of s2.

Constraints:
1 ≤ s1.size(), s2.size() ≤ 10^6

"""


class Solution:
    def isSubSeq(self, s1: str, s2: str) -> bool:
        if not len(s1) or len(s1) > len(s2):
            return False
        s1_found = 0
        for c in s2:  # O(n)
            if c == s1[s1_found]:
                s1_found += 1
            if s1_found == len(s1):
                return True
        return False


solution: Solution = Solution()

assert solution.isSubSeq(s1="gksrek", s2="geeksforgeeks") is True
assert solution.isSubSeq(s1="AXY", s2="YADXCP") is False
assert solution.isSubSeq(s1="1234", s2="AJSND1OA2SND434OAS4ND") is True
assert solution.isSubSeq(s1="1234", s2="AJSND1OA2SND3OAS3ND") is False
assert solution.isSubSeq(s1="", s2="ABC") is False
assert solution.isSubSeq(s1="ABC", s2="") is False
assert solution.isSubSeq(s1="", s2="") is False

"""
@notes post-mortem=start
-----BEGIN PGP MESSAGE-----

hF4DjxTuSjEZ/v8SAQdA8FC3yA7fdvMdG/sHUpBsiOtDYXxDCCpN6L3AAxxRhUkw
CrQCl9K4gYfUACIMNwJXqpqNbDrPdYn6sE/FL8LkTz38XssxrLjCV/dOrVCa0ULc
0qsBiG6FOfX5kizQEgPIQmvwb850fCo3Q10V1GosIcCcoLo69zlvCobmWDE7zOSu
AfX5st4gX4OSPesnz8jv+v6pVC0ZPIOcsaw3zGRcliZD0IN3/zXcfpX8Tg0x+h+h
Esw6tad/CMLPwECm23Jz+1FL+7p82svOvR8bkayhsdB/DR7z3u4U+a6KXanaJtjQ
cDRhXgbrmF4oca3DosoL3b5/2M73t7n4/Tmil+s=
=Sfcb
-----END PGP MESSAGE-----
@notes post-mortem=end
"""
