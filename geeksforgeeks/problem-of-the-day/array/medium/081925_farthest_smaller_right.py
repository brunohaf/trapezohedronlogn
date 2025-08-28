# GeeksForGeeks - Problem of the Day

# Farthest Smaller Right
# Difficulty: Medium
# Accuracy: 49.85%
# Submissions: 3K+
# Points: 4

# You are given an array arr[]. For each element at index i (0-based indexing), find the farthest index j to the right (i.e., j > i) such that arr[j] < arr[i]. If no such index exists for a given position, return -1 for that index. Return the resulting array of answers.

# Examples:

# Input: arr[] = [2, 5, 1, 3, 2]
# Output: [2, 4, -1, 4, -1]

# Explanation: arr[0] = 2: Farthest smaller element to the right is arr[2] = 1.
# arr[1] = 5: Farthest smaller element to the right is arr[4] = 2.
# arr[2] = 1: No smaller element to the right → -1.
# arr[3] = 3: Farthest smaller element to the right is arr[4] = 2.
# arr[4] = 2: No elements to the right → -1.

# Input: arr[] = [2, 3, 5, 4, 1]
# Output: [4, 4, 4, 4, -1]
# Explanation: arr[4] is the farthest smallest element to the right for arr[0], arr[1], arr[2] and arr[3].

# Constraints:
# 1 ≤ arr.size() ≤ 10^6
# 1 ≤ arr[i] ≤ 10^6

# ! SuffixMin (precompute) + Iterative BinarySearch


class Solution:
    def farMin(self, arr: list[int]) -> list[int]:
        res = [-1] * len(arr)
        if len(arr) == 1:
            return [-1]

        suffix_min: list[int] = arr.copy()  # arr[:]
        for i in range(len(arr) - 2, -1, -1):
            suffix_min[i] = min(arr[i], suffix_min[i + 1])

        for i in range(len(arr) - 1):
            left, right = i, len(suffix_min) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if suffix_min[mid] < arr[i]:
                    res[i] = max(res[i], mid)
                    left = mid + 1
                else:
                    right = mid - 1
        return res


sol = Solution()

# ! Tests
assert sol.farMin([2]) == [-1]
assert sol.farMin([4, 2]) == [1, -1]
assert sol.farMin([2, 5, 1, 3, 2]) == [2, 4, -1, 4, -1]
assert sol.farMin([2, 3, 5, 4, 1]) == [4, 4, 4, 4, -1]

"""
@notes post-mortem=start
-----BEGIN PGP MESSAGE-----

hF4DjxTuSjEZ/v8SAQdANZu6/tkFJp0eqM4mJZbh8PjzziSU4SDRl0K+4LdUtksw
PXiDrLSqBY1hCThvAr/UGetfvWGZJLreH0vEAtlJ4AdqFEyuHQOGUDa3CwyaHbJJ
0ukBDK1rZOJolzkqEemoIt55CbfX/7plYC9w0mk2L0FZ/kdeABpAp5dOZPn6tdYt
bkbUxvuRfZ6qclwLwna9vH3hutp5qK/zbrT98LG2TJrSUaGiOww/hzYfR3Hdd1Y9
2SmKOM+8UekjPwWtvOKSTZLy5QaNm2zHledzZR3j1YImGjnZNSpcn8qMEFmM2z5U
JSvaujy4gHfvs87/kkX6cQ3fX9VS8L0xN0yQ0SRZ28FMn++Bl8SOdDGVyl+oVKBS
VyaLFjpWpQdSLw4UpUvopQBGeevZRS1BRDKvyuXuLHzR3tNT3WwCtIKXf5Y29rNA
IkpSBnXZTCdCUtA42IoYxJZkdyXVYMc9nH6tVz/lbCr/ETRczbNCUN9BH3ELUkp8
Hr8lQ7j3/U6P1iCDYZ49k7M6ddZg1gHlmGXC0mmQFbJt/i3sMy/y4B0irzOOfjHD
3DYWK0EawZ3zfwjPZ9IHxBb3nUMFGi0Ul9zKuNeDSTHYBTNMht/H/SUsYtXLkw+c
+tKcsp/6FtQbsVWliLwMif/D0BBOYCSaKDYB17tQ6oHy8scrPPWHhOVL0Jj7rRRL
Wo/dNa1uA2LTFLRhOOeFC8S4t6kkd3Anacl9AhDSovWr/YdALHQnQzi35mzTQL2z
Ci5Lf97Mwa50sLAKemFA1NR5v501iUgxHGyyrzgpjfm0HMBsNI/15YhjwLqj2pZ9
gC5BoXx1C6Y1Vs+Kg2rbCQLTHXkbuk+xmMoX+UpcA5G3Pxrj562cJrTFJtOoC6ST
O0Np7LQWRfqNE1o/q8rvGzrcUYUCJtA3DGqLKdr/XUVs9ymxVi5drWNJuemy70ye
bN3rYoHQ3K09oi7vHTR7RsABCwEzexFqHE2qv8wSMh3PKGnFvT75jXGw2YrutE99
6lNn7ZR4WKo38ygUNQaBM8f+4gHkzoD2nBeYRdUNqtFVdSRsBqGyqT+6oubhka6N
hFb2sGc9oFtrOTDBK7HpG6z7gS1/4l2sGF5vhD7/9JPKiCOfN4l4PxkN7oUVd4iO
vTsh2aa7W9yVSqFAWdVWF3rP/A/VxJwIOH8MyGLB8GPCrdhUqaBj5JD85wZve2UR
=xdJ3
-----END PGP MESSAGE-----
@notes post-mortem=end
"""
