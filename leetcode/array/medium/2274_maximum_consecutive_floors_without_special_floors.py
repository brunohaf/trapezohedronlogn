#
# @lc app=leetcode id=2274 lang=python3
#
# [2274] Maximum Consecutive Floors Without Special Floors
#
# https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/description/
#
# algorithms
# Medium (52.11%)
# Likes:    423
# Dislikes: 39
# Total Accepted:    38K
# Total Submissions: 72.8K
# Testcase Example:  '2\n9\n[4,6]'
#
# Alice manages a company and has rented some floors of a building as office
# space. Alice has decided some of these floors should be special floors, used
# for relaxation only.
#
# You are given two integers bottom and top, which denote that Alice has rented
# all the floors from bottom to top (inclusive). You are also given the integer
# array special, where special[i] denotes a special floor that Alice has
# designated for relaxation.
#
# Return the maximum number of consecutive floors without a special floor.
#
#
# Example 1:
#
#
# Input: bottom = 2, top = 9, special = [4,6]
# Output: 3
# Explanation: The following are the ranges (inclusive) of consecutive floors
# without a special floor:
# - (2, 3) with a total amount of 2 floors.
# - (5, 5) with a total amount of 1 floor.
# - (7, 9) with a total amount of 3 floors.
# Therefore, we return the maximum number which is 3 floors.
#
#
# Example 2:
#
#
# Input: bottom = 6, top = 8, special = [7,6,8]
# Output: 0
# Explanation: Every floor rented is a special floor, so we return 0.
#
#
#
# Constraints:
#
#
# 1 <= special.length <= 10^5
# 1 <= bottom <= special[i] <= top <= 10^9
#  All the values of special are unique.
#
#
#
from typing import List


# @lc code=start
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        maximum: int = max(special[0] - bottom, top - special[-1])
        for i in range(len(special) - 1):
            maximum = max(maximum, special[i + 1] - special[i] - 1)
        return maximum


# @lc code=end
assert Solution().maxConsecutive(bottom=2, top=9, special=[4, 6]) == 3
assert Solution().maxConsecutive(bottom=6, top=8, special=[7, 6, 8]) == 0
# assert Solution().maxConsecutive(bottom=10, top=30, special=[19, 10, 15])
# Input:

"""
@notes post-mortem=start
-----BEGIN PGP MESSAGE-----

hF4DjxTuSjEZ/v8SAQdALv1udOIAGCgThdHlJd0mozrusdA3WPxe/ixinJSkwT0w
LUXtpdffircugQUQ/jp2ujeeB80dquA547s/gKBEjNnyY0YD2enSloWv3fxB5q4u
0ukBBcaKqc6FDdQEiCkalytKYULEt6R23W4TY6imr6BKPwUFRVDcB28toIaDNy+y
ZtCCXzhHLOgZ8FbHFoJHkUFuY5tWg9Oicz1RqA/FprH1Y33ZbBfTXY8VtgQUZ5G0
0829h+3nEx7TvBKiO9RS2YgZt1qvh1MEFkNRLs63sRPSJqsRvEDEAAuJohi/32tj
W+o3QzmaB6G9lv9FAYxx7uJ+Cw1FGTSUx5T2jEskdeS72UDv/zPN1RqtO2CrINtC
R/eze9JUcxqmHvnC3A1Lzhd3W2to/TVBjlVxw4egywb93ppLk6Zz22Ep9B0YOfn8
Hukfx9tyBC8JBZoHw9CmFf880JXYnbEtmlk9OoUXC4g6WydtcyDVoeFx+QdXky60
9u7lRMWkPND+qFsNNxOFfLkqUyv3VnloUXZy/0Q5IpNMP5bwNpOUCKahAmR19bAv
vJnMGL6R9mo1onHnhHUSR9+sR7a//o3GH1EDhPtu8jbfbbC9evo97f3SmXLItwX1
R1chHb6di3whgN0cSygVD5XBHdN/YyU/DmTF5iMe5EHSFW2WixUce4Po/k2KutgC
bynJ/bg15xLlEhSH0W84R0i/BnOt+F5bU9rN1f5ShFIxkqNTq6TllLPAc22W+u2g
OJQmEeV4ZuGa4hLW+a3Jt0oH727IMV2kSe7U4nKO8svphcEwwxwTekkXN+QRW6Tg
dXPiPCHVXI3zSW1aSvqIv21H1OhkfUY8Pc9yFzUdXUI8BbX86bZs3rrFWoEWx3PM
gRHcQ7fMjr/7u7Mlbk1P0qEl/AwVoKjLSNIA4pbO9Wf4bPAmbMMwlGhPFrLm+n1e
XprhYuyhjWr27VR8GMVcj618+xEo7jOoudhwACFVGJYVpKvn6L8noBOymB9LF2TN
8PbiSZ01K5sfnG4hBa5JNqKpJH+mvAl6u2IRzEdwGvXYWJQYvie7brx6IxnnpXxh
xKV4PxVWEMpv58ftKkLpxQl/0XzQjfeihQGTPVc/U9eKkn34b5njShPl/jac0eZH
O7mLk7Uyei0myZ/ZDmA3Yb8ueeDlbYuRGeutrZyGCzTq49FLmhBR0ry8YisWBoyX
k1yNxw8goEzkPuqQv3pxEB5tKswlXqHTs5XSPrKdK+FiSxGDwvf81MLnNX6hgXdc
tp4T9mYfIUvOYJ+edyx0h/katoZb7GftYKmWm6BfRRC5NI3wqK4Ld9UNkqi/QPge
jUX6UqOjnsejCw6EUWz6yoPybF6wr7TCYMN+eHteSfbiREo/e4032WNOfs9SN3W9
CSuGzW4hpYQ5LUwi6fQ2a7CbShmefX4M+SRkW+UwvuaoKqA3kWUn31RR8GVphjNt
QN3dSg==
=b8tQ
-----END PGP MESSAGE-----
@notes post-mortem=end
"""
