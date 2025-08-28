# GeeksForGeeks - Problem of the Day
#    - https://www.geeksforgeeks.org/problems/maximize-number-of-1s0905/1

# Maximize Number of 1's
# Difficulty: MediumAccuracy: 39.46%
# Submissions: 67K+
# Points: 4
# Average Time: 20m

# Given a binary array arr[] containing only 0s and 1s and an integer k, you are allowed to flip at most k 0s to 1s. Find the maximum number of consecutive 1's that can be obtained in the array after performing the operation at most k times.

# Examples:

# Input: arr[] = [1, 0, 1], k = 1
# Output: 3
# Explanation: By flipping the zero at index 1, we get the longest subarray from index 0 to 2 containing all 1’s.

# Input: arr[] = [1, 0, 0, 1, 0, 1, 0, 1], k = 2
# Output: 5
# Explanation: By flipping the zeroes at indices 4 and 6, we get the longest subarray from index 3 to 7 containing all 1’s.

# Input: arr[] = [1, 1], k = 2
# Output: 2
# Explanation: Since the array is already having the max consecutive 1's, hence we dont need to perform any operation. Hence the answer is 2.

# Constraints:
# 1 ≤ arr.size() ≤ 105
# 0 ≤ k ≤ arr.size()
# 0 ≤ arr[i] ≤ 1


class Solution:
    def maxOnes(self, arr, k):
        flipped = 0
        best = 0
        left = 0
        for right in range(len(arr)):
            if arr[right] == 0:
                flipped += 1
            while flipped > k:
                if arr[left] == 0:
                    flipped -= 1
                left += 1
            best = max(best, ((right - left) + 1))
        return best


# 1 1 0 1 0 1 1

# l r flipped best
# 0 0  0       0
# 0 1  0       1
# 0 2  1       2
# 0 3  1       3
# 0 4  2       4
# 1 4  2       4
# 2 4  1       4
# 3 4  1       4
# 3 5  1       4
# 3 6  1       4

"""
@notes post-mortem=start
-----BEGIN PGP MESSAGE-----

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
=u6em
-----END PGP MESSAGE-----
@notes post-mortem=end
"""
