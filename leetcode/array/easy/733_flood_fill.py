#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#
# https://leetcode.com/problems/flood-fill/description/
#
# algorithms
# Easy (66.79%)
# Likes:    9048
# Dislikes: 927
# Total Accepted:    1.2M
# Total Submissions: 1.8M
# Testcase Example:  '[[1,1,1],[1,1,0],[1,0,1]]\n1\n1\n2'
#
# You are given an image represented by an m x n grid of integers image, where
# image[i][j] represents the pixel value of the image. You are also given three
# integers sr, sc, and color. Your task is to perform a flood fill on the image
# starting from the pixel image[sr][sc].
#
# To perform a flood fill:
#
#
# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent (pixels
# that share a side with the original pixel, either horizontally or vertically)
# and shares the same color as the starting pixel.
# Keep repeating this process by checking neighboring pixels of the updated
# pixels and modifying their color if it matches the original color of the
# starting pixel.
# The process stops when there are no more adjacent pixels of the original
# color to update.
#
#
# Return the modified image after performing the flood fill.
#
#
# Example 1:
#
#
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
#
# Output: [[2,2,2],[2,2,0],[2,0,1]]
#
# Explanation:
#
#
#
# From the center of the image with position (sr, sc) = (1, 1) (i.e., the red
# pixel), all pixels connected by a path of the same color as the starting
# pixel (i.e., the blue pixels) are colored with the new color.
#
# Note the bottom corner is not colored 2, because it is not horizontally or
# vertically connected to the starting pixel.
#
#
# Example 2:
#
#
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
#
# Output: [[0,0,0],[0,0,0]]
#
# Explanation:
#
# The starting pixel is already colored with 0, which is the same as the target
# color. Therefore, no changes are made to the image.
#
#
#
# Constraints:
#
#
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 2^16
# 0 <= sr < m
# 0 <= sc < n
#
#
#
from collections import defaultdict, deque
from typing import List


# @lc code=start
class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        visited: dict[tuple[int, int], bool] = defaultdict(lambda: False)
        bfs: deque[tuple[int, int]] = deque()
        ref_color: int = image[sr][sc]
        bfs.appendleft((sr, sc))
        while len(bfs):
            sr, sc = bfs.pop()
            image[sr][sc] = color

            neighboors: list[tuple[int, int]] = [
                (sr - 1, sc),  # up
                (sr, sc + 1),  # right
                (sr + 1, sc),  # down
                (sr, sc - 1),  # left
            ]

            for r, c in neighboors:
                if (
                    r >= 0
                    and c >= 0
                    and r < len(image)
                    and c < len(image[r])
                    and image[r][c] == ref_color
                ):
                    if not visited.get((r, c), False):
                        bfs.appendleft((r, c))
                        visited[(r, c)] = True
        return image


# @lc code=end


sol = Solution()
sol.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2)
sol.floodFill(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0)

# Get the initial color value
# BFS/queue -> only add neighboors if value == initial value
# Change color by value when popping
# handle n and m bounds

# deque = deque() / appendleft/pop
"""
bfs = deque((sr,sc))
m = len(image)-1
ref_color = image[sr][sc]
while(len(bfs)):
   sr, sc = bfs.pop()
   image[sr][sc] = color
   for (r, c) in [(sr-1, sc),(sr-1, sc+1),(sr, sc+1),(sr+1, sc+1), (sr+1, sc), (sr+1, sc-1), (sr, sc-1), (sr-1, sc-1)]:
        if r > 0 and r < m and c > 0 and c < len(image[r])-1
            bfs.appendleft((r,c))
"""

# Example 1:
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# [1, 1, 1]
# [1, 1, 0]
# [1, 0, 1]
# 0,1
# 1,0

# 0,0
# 0,2
