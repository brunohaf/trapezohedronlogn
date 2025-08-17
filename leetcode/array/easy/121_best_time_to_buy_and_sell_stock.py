#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (55.46%)
# Likes:    33753
# Dislikes: 1313
# Total Accepted:    6.7M
# Total Submissions: 12.1M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
#
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you
# cannot achieve any profit, return 0.
#
#
# Example 1:
#
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you
# must buy before you sell.
#
#
# Example 2:
#
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit =
# 0.
#
#
#
# Constraints:
#
#
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4
#
#
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for sell in prices:
            if buy < sell:
                max_profit = max(max_profit, sell - buy)
            else:
                buy = sell
        return max_profit


# @lc code=end

print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([2, 4, 1]))
print(Solution().maxProfit([0]))

"""
TODO:
    - Retry this from scratch

@notes post-mortem=start
-----BEGIN PGP MESSAGE-----

hF4DjxTuSjEZ/v8SAQdAXdEqlVbAUz1Vxi/NHM5dw4phj+u1Rsj+uCu7a8TLJn8w
O/mxP1LLB+IGn7wb+K2CKIpNyDjoAs9vQnPVNhcgoVAY2VZjpd164yT+B0jESi/I
0sAbASVXn4GSohuX8+aSmLHy0mcR4OPGUCxhpJ5GmoVcNWdTMtm3KTwUiyKzYbuX
FIAvtnetTb+/cNijfHa+UkIsyQMAybhwe6YhpBO1FSxFA9VQCXTF28cfUvMmaf/v
xqTGGDWgMIQo67sGoeYeAjxzXyl5eTFo8KIBKC7rOkkhSPenanQpTlH2lVN0GTRF
6zIgT6j9AzEaitFNZ68xTlSFciBOS/fFjiX5ipS/Vp23wKDZ2Qr95f2rPgEA2Dz1
nU7Xt6arfbYCPDuYzKf8iYisjzxvGXeC8Xa4QdOj
=HPgx
-----END PGP MESSAGE-----
@notes post-mortem=end

"""
