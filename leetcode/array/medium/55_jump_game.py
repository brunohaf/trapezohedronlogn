#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (39.44%)
# Likes:    20675
# Dislikes: 1399
# Total Accepted:    2.7M
# Total Submissions: 6.7M
# Testcase Example:  '[2,3,1,1,4]'
# You are given an integer array nums. You are initially positioned at the
# array's first index, and each element in the array represents your maximum
# jump length at that position.
# 
# Return true if you can reach the last index, or false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
        
    def canJump(self, nums: List[int]) -> bool:
        destination = len(nums)-1
        max_reach = 0
        for i, jumplen in enumerate(nums): #Greedy O(n)
            if i > max_reach: 
                return False
            if jumplen+i > max_reach:
                max_reach = jumplen+i 
            if max_reach >= destination:
                return True
        return False
# @lc code=end

# Goal: Check if there's a path from index 0 to len(nums) - 1
# How:
## At each index i, nums[i] tells me the max number of steps I can jump forward.
## If nums[i] >= (last_index - i), I can directly reach the end => True
## Otherwise, I try intermediate jumps from i+1 to i + nums[i]
## Jumps are only forward, and are valid only if nums[i] > 0
# I stop when:
## - nums[i] == 0 and I'm not already at the last index => deadend
## - All jumps from i have been exhausted and none lead to the end
# Possibilities:
## Recursive(DFS) or iterative(Greedy)
# For Iterative Greedy:
# destination = len(nums)-1
# max_reach = 0
# For each i, jumplen in enumerate(nums):
#   if i > max_reach: Then there's a deadend -> Return False
#   if jumplen+i > max_reach -> Then max_reach = jumplen+i 
#   if max_reach >= destination -> Return True
# Return False

# @notes post-mortem=start
-----BEGIN PGP MESSAGE-----

hF4DjxTuSjEZ/v8SAQdAzWwNn4bMtKC0j1WijdVNtNUNpnT4sK+MH6tUQQ3nOSEw
C5hR8QDoos2SaH+ShNIq/Fd3NoQMUMLrnByYd66qcF1M1ue2LrlSVWlG7qK03mVF
0ukBMVOgQc5Bjt/2evcFkdo4Gm7dIh3Slil+w1v6rXjooIItcYKVTt+IXX3mMttu
EzE/4z34mSH7bG13pJCERu8x54kb3tXLMKb613n9REWa75CtpCcv5mZEad0JyOjW
6GEBuIcvTzOBtDHHWX857za0zxBDAkf4XjB2xgVE1pZxMyb6pdbgtif9n09xvro/
VqlfWU2JLp5salP1kAurtIatK5inpBFeGQ9yrJ4l40X5xL/FpqDb3IMCgBiRsJ2K
YCWE8DzJMZSk+CS9Q9ABnhJ98c90PEFzrEnajuBAS9gIRQVEScu8xmqrt9jo1eRd
/x0/wUHl3fQgFbgCUAkvDElCj8iPOhLr7Reaihv4uSE8vcHwBDHLTnDNiOWa5oks
Sxio2qwNoScox/IFxz+XBEznKt0Xru9h38D1gkWbVCV6/uA8guL0W1Ef/5GWwNAv
JB9lUzMgnqcdBnabehqo5NFo6vcJnwCr60RWUq0jJTPIjQy59jsL2SPG4noGt1Xy
N0B463zBfAXL/YqHT+wA6w7sxn8ALa/wJmjHAsrwmyEs0yyXIN7BPp1aMOAouk9M
m0X9QprSOyQcKHrioOyg3N/ALo3pe7rnpFY+FoDn8fG4JRCR0wePHgyu4r/N0Vhl
hxdfGcpWP5kfCppzSpUnb2SvU0YZg2X5Md9qj97oPr74ocCCuKZuHja89XDvCe+b
M2phT4V52UMMiNz8FJbTE7jtK41uNRC+PEyFBABnZVeUTsqISGhDRuHmZnXAmZtl
1BiIWR1FLcFASZaP500IbioLg4bLrPcDqdtWYLMdIYsR3Tq3QSLaDCwKDWdB7mi0
HjrEX7VsqmRI71PWVfh2BFlQmiLGOKB/KsFwUb71yNIAaa5SMTp8ans0VT6AoJUE
sx9tMYHJVE0pNHjuFQezRA5vhI/pqhjUdneIWGo31LOo/wehOiFEEHB4wB1ulX9C
rXd5UTRA/fADbkqz2sia1zhVJpV1VtSQy5p4S6lJO8fj7IJiBS1aH++d0PoJWRWX
xjR/TuMHKODW1zuDKpX83+R8WQQZjXLHwFfGlroz6N1F0AQ5UUA8PDMh3EuLD6WP
I6DSfbB4MlZKnZLyGbyZ+75vRgkb+w==
=PH3J
-----END PGP MESSAGE-----
# @notes post-mortem=end
