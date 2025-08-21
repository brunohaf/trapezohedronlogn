#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (46.91%)
# Likes:    20223
# Dislikes: 517
# Total Accepted:    2.5M
# Total Submissions: 5.3M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
#
# Example 1:
#
#
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
#
# Example 2:
#
#
# Input: coins = [2], amount = 3
# Output: -1
#
#
# Example 3:
#
#
# Input: coins = [1], amount = 0
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
#
#
#
from typing import List


# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp: list[int] = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] != -1:
                    dp[i] = (
                        min(dp[i], dp[i - coin] + 1)
                        if dp[i] != -1
                        else dp[i - coin] + 1
                    )
        return dp[-1]


# @lc code=end
sol: Solution = Solution()
assert sol.coinChange(coins=[1, 2, 5], amount=11) == 3
assert sol.coinChange(coins=[2], amount=3) == -1
assert sol.coinChange(coins=[1], amount=0) == 0
assert sol.coinChange(coins=[3, 18, 5], amount=11) == 3
"""
@notes post-mortem=start
-----BEGIN PGP MESSAGE-----

hF4DjxTuSjEZ/v8SAQdAHRoRBateNjErbPMy2zsZwbIwCVS0Er20Vz/KyKtxTBYw
BYDEQqp0ZAWy+3lDcxeYWSajN1IRJPKp8Izqbmw2raUd1NItfHipivIwIdH7COxwW
0sCVASlV6Q8QXet3REz6d1v+vJ9Yy5DSpJzZaUpp25SvKlEMnJ46CCx+zQYLgEVB
by5bXRDQeYF0oG9/gngj+ZjpgynjYvdgo/5jGmeHEPspl4LLdPRYIvfrAew+GrOz
daMNvBwpl/pket2cxMmKh0OWlQbfcWMM/fIK10a2fzNn1f3fzdWjLdzjMhzsCeZX
wd9yM0qKH7gWGhA8VEUMvqeamLQj4ywLt3justSt7xjio6JtYK9Mf5J+vwGn0t1+
huwfhInoGoPW17naxFoI79diDW6sRT92rC5TYVAhl94s/YjNXU/H3V2GJ4rJ3R/a
rJbHOlC6RZfKX8yVzrDpI8sPeHkw4hkL1bdTScwUSylA7tsPQDZYZqrHd1LCs75N
DksKTMI3AZlufiEPDaku040gjjOvI1wqgvDhK9EZDrRUTp/+VZ614wia8pUYrSwi
vSdPeXSv3qk=
=H7V1
-----END PGP MESSAGE-----
@notes post-mortem=end
"""
