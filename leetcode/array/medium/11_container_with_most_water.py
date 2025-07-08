#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (57.85%)
# Likes:    31538
# Dislikes: 2023
# Total Accepted:    4.2M
# Total Submissions: 7.2M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the i^th line are (i, 0) and (i,
# height[i]).
# 
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
# 
# Return the maximum amount of water a container can store.
# 
# Notice that you may not slant the container.
# 
# 
# Example 1:
# 
# 
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
# 
# 
# Example 2:
# 
# 
# Input: height = [1,1]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    def getBaseLine(self, height: List[int]) -> int:
        for i, h in enumerate(height):
            if h>0:
                return i
            
    def maxArea(self, height: List[int]) -> int:
        max_water_area=0
        base_line=self.getBaseLine(height)
        for i in range(len(height)-1,base_line-1,-1):
            for j in range(base_line, i):
                if j >= i:
                    break
                water_area = (i-j) * min(height[i], height[j])
                if water_area > max_water_area:
                    max_water_area = water_area
        return max_water_area
# @lc code=end
sol = Solution()
assert sol.maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert sol.maxArea([1,1]) == 1

# water_area = (i-base_line) * min(height[i], height[base_line])
# max_water_area = 0
# base_line = 0
# Get the first non-zero line
# From farthest_line to base_line: do
# Get the tallest line
#   if water_area > max_water_area:
#       max_water_area = water_area
# Return max_water_area

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
## base_line = 1
## lines | water_area
## 8,1   |   7 * 7             