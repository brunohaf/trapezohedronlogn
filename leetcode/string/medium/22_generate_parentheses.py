#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (77.38%)
# Likes:    22426
# Dislikes: 1044
# Total Accepted:    2.5M
# Total Submissions: 3.2M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
#
#
# Example 1:9
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
#
#
# Constraints:
#
#
# 1 <= n <= 8
#
#
#
from typing import List


# @lc code=start
class Solution:
    def backtrackParenthesesGen(
        self,
        n: int,
        open_count: int = 1,
        closed_count: int = 0,
        current_str: str = "(",
        result: List[str] = [],
    ) -> None:
        if len(current_str) == 2 * n:
            result.append(current_str)
            return

        # Shortcut for current_str with all open parentheses processed.
        if open_count == n and closed_count < open_count:
            result.append(current_str + (")" * (open_count - closed_count)))
            return

        if open_count < n:
            self.backtrackParenthesesGen(
                n=n,
                open_count=open_count + 1,
                closed_count=closed_count,
                current_str=current_str + "(",
                result=result,
            )
        if closed_count < open_count:
            self.backtrackParenthesesGen(
                n=n,
                open_count=open_count,
                closed_count=closed_count + 1,
                current_str=current_str + ")",
                result=result,
            )

    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ["()"]
        result: List[str] = []
        self.backtrackParenthesesGen(n=n, result=result)
        return result


# @lc code=end

"""
@notes post-mortem=start
-----BEGIN PGP MESSAGE-----

hF4DjxTuSjEZ/v8SAQdA/lppmO11sBSkXvua6T3dkVg+3vEYjB9hU6jU5futfmIw
SGRqqf9PutEkcwcVG0QrsAyMCwIxsJdTnKl/7QnlwEESo4sPMaouCEPO6v8t2Sbj
0sDZAWCqFBv0iPoso9dWqCBBtsRJgKgYK4hpxODfptglPLGYfPna3ZtNhVxgQkqR
lFDEXV0Uxb5MuE9jv1hhiuo0OqO5GgJJAhP8zBhMRVca9hgtkepSiAdCO2VctFeZ
3dmu+2L8drgxV3txB4E8QeiWNrpm+mUcIZp6Wb9tE1X0qrzp1QVGMxGQc/Ig821f
Q/9ixG77MqB+EgsOJhTHQgYTCYWu2gsbGkK85B/KcHu8RNNZ1Ma5QPOCDOFc87Ug
qVLFqBY0fVZ0rSDZvnIHM4FV2VapLpJT79Q9BlQzqdf30ih1QEi/c7doCD0KQ9UK
AHcHCyy3+cbURPv9gG4a120eDwWQ9M4dVIxsTP01uclY+CTcNTihgSwXNzP4Wfg9
1gzZwI6Po/NqQShIwyM7KJZvLsq8FxnXl8vkzlHyXvgqutt2Z+01nhhksO62g+ag
EPCMVLW8augO58niwuNPIstXtV7odsdtVONnJiL9W10jHD++V6esekOMammV0cKv
h5IrKzcV3VA6MVeXGfnLE+owmYblHmqirsGvxg==
=3pIL
-----END PGP MESSAGE-----
@notes post-mortem=end
"""
