#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
# https://leetcode.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (64.81%)
# Likes:    16001
# Dislikes: 1103
# Total Accepted:    4.9M
# Total Submissions: 7.5M
# Testcase Example:  '"III"'
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
#
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, 2 is written as II in Roman numeral, just two ones added
# together. 12 is written as XII, which is simply X + II. The number 27 is
# written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:
#
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
#
#
# Given a roman numeral, convert it to an integer.
#
#
# Example 1:
#
#
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
#
#
# Example 2:
#
#
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
#
#
# Example 3:
#
#
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].
#
#
#

from collections import deque


# @lc code=start
class Solution:
    def parse(self, symbol: str) -> int:
        return {
            "i": 1,
            "iv": 4,
            "v": 5,
            "ix": 9,
            "x": 10,
            "xl": 40,
            "l": 50,
            "xc": 90,
            "c": 100,
            "cd": 400,
            "d": 500,
            "cm": 900,
            "m": 1000,
        }.get(symbol) or 0

    def romanToInt(self, s: str) -> int:
        q = deque(list(s.lower()))
        result = 0
        while len(q) > 0:
            s1, s2 = q.popleft(), (q[0] if len(q) else "")
            if f"{s1}{s2}" in ["iv", "ix", "xl", "xc", "cd", "cm"]:
                result += self.parse(f"{s1}{q.popleft()}")
            else:
                result += self.parse(f"{s1}")
        return result


assert Solution().romanToInt("III") == 3, "ERROR: III != 3"
assert Solution().romanToInt("LVIII") == 58, "ERROR: LVIII != 58"
assert Solution().romanToInt("MCMXCIV") == 1994, "ERROR: MCMXCIV != 1994"
"""
@notes post-mortem=start
-----BEGIN PGP MESSAGE-----

hF4DjxTuSjEZ/v8SAQdAeFbqRcmFvdo5AgE5zJBXX81FLiotg4aOi1gGskp9Di0w
i//bp/+dgA7Owv38vrNCQJGTJWtB/RgLEywqwUQbKoz0TNF/lfChzHfkT0D3M1D1
0sEhAcQFzf1mjPRcIEbbTj1a4gBKeibgdDyri1DjbLwyU7RvPd8PuJUUQ92k7jmn
AEoCJllRTMutNaJG0j8oZ7FgIxyyngQQfxxMzqq1P7ysrtGWLjMCVv0TFovWpLvH
un7i9Ot6CIjymEq6WR6QkBZfvubHenRlDdfeBCwWaR67u0TiJHAygkP7VQ2j6k2Y
1R1iPa9uZm6k5JrYx/pC11KuBj07G+6NELobCqLlkhTRPx2bhEkzC49NY0Fq7xTy
Xq7TJu3Xgcrk3LaKt/6NqZnM8A46098kOyVkYefBaNC2kgpOqmOQdwqF0xEi/YqT
0IVlOvt04YYbcCOBWMRaoFCsGpdvMw6+CMmGY51pF5MhY9jc7Kthzdh0yxlPoQbo
2frOBuPslSuFOYBnulQe6dFmjx7Mrb7KURJNbP/wYHl8H8ddZlXdc0YZdPVlDNLA
uTcbZwRvyPv/g19sWavLPGbVNyHTXL3WVjlQEKYSt+/XWG5Kk+SGik02FFHqelpu
qU/sQnWIYe/UjfuAgsdlMGeXpCslc/WHDtdaA+4unYz4QwDxLhuHgakDONVx+XM+
vRg1Vsn7ib3fy0P+nbkLuruTRyLpz4xIhMDiXHYc57azdrG35knJ9IahsIeYMnZf
sG/QZA==
=16B+
-----END PGP MESSAGE-----
@notes post-mortem=end
"""
