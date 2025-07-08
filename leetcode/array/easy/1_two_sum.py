#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (55.85%)
# Likes:    62458
# Dislikes: 2263
# Total Accepted:    17.7M
# Total Submissions: 31.7M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# You can return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# 
# 
# Example 3:
# 
# 
# Input: nums = [3,3], target = 6
# Output: [0,1]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
# 
# 
# 
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time
# complexity?
#
from typing import List

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            map[num] = i
        for i, num in enumerate(nums):
            complement = map.get((target-num), None) 
            if (complement and complement != i):
                return [i, complement]
        return []
# @lc code=end
assert Solution().twoSum([1,3,4,2],6) == [1,1]
# ICE:
# I:
# array -> nums
# int -> target
# C:
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
#
# E:
# ...
# Goal: Which are the indices of the 2 numbers in the array (nums)
# with when sum together results in target?
#
# Bruteforce: O(n^2) -> Might not be enough as the input array is too big
# For i,num in enumerate(nums):
#   For j in range(i+1,len(nums)):
#       if target == num + nums[j]:
#           return [i, j]
# Hashing: O(n)
# map = {}
# For i, num in enumerate(nums):
#   map[num] = i # if only one valid answer exists, nums doesnt have duplicated values.
# For i, num in enumerate(nums):
#   complement = map.get(target-num, None)  
#   if (complement):
#       return [i, complement]
#   
# Hashing2: O(n)
# map = {}
# For i, num in enumerate(nums):
#   map[num] = i
#   complement = map.get(target-num, None)  
#   if (complement):
#       return [i, complement]
# For i, num in enumerate(nums):
#   complement = map.get(target-num, None)  
#   if (complement and complement != i):
#       return [i, complement]
#
# Test:
#   Input: nums = [2,7,11,15], target = 9
#   Output: [0,1]
#   map = {2:0, 7:1, 11:2, 15:3}
#   for i=0, num == 2 -> map.get(9-2==7) == 1 -> Ok
# Test:
#   Input: nums = [7,0,-11,14], target = 14
#   Output: [1,3]
#   map = {7:0, 0:1, -11:2, 14:3}
#   for i=0, num == 0 -> map.get(14-0==14) == 3 -> Ok
# Test:
#   Input: nums = [1,3,4,2], target = 6
#   Output: [1,1]
#   map = {7:0, 0:1, -11:2, 14:3}
#   for i=0, num == 1 -> map.get(6-1==5) == None
#   for i=1, num == 3 -> map.get(6-3==3) == 1
'''
@notes post-mortem=start
-----BEGIN PGP MESSAGE-----

hF4DjxTuSjEZ/v8SAQdAoabhGIWpHcysngR/ZeLFA27CaAM2LQeeL+At2ptX51Iw
2lmpjQLKL+nORkD18862RGnknj6GGAKmUGEvyjHL2wXRfoffGk76hElBA1NN+bBb
0sBnAc5tial+HFRnUH+N5v4sPzTIQbEnuAaHycb+tlVENX9YhLggF6qWaTY9/3Uw
kjukHHh9aJyLhWSucTfyjZ3VvPMmMn9/NXDzg8TMHd+MjSq+vV1cGdZhWn7+QCJ/
okt5vFO8SRXSAIpjinGbGax8+w/OlSz3Kaf9ARJS68wqn7W2ErYO8rhrWjq1t1S/
mzYGYDeiPfzkzkYJQeKBPcTCBhwSMb08j/X1AnEdstzc0rPiEKInpr5Xwm8JR3f3
FP6/5pA160QUJwqy+Csv+yBHC05gcK3owN44B7YYS5YpFhvSYP2OrORyezaDnx2v
RigsClr7GLHRLQdvVAUe+leDargHlGVYQ+4NjsrfjiJUHyWziHtUyWLkjem1T5eL
iVKvmINrLkuDhg==
=IcXD
-----END PGP MESSAGE-----
@notes post-mortem=end
'''
