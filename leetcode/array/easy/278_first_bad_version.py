#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#
# https://leetcode.com/problems/first-bad-version/description/
#
# algorithms
# Easy (46.18%)
# Likes:    8784
# Dislikes: 3402
# Total Accepted:    2M
# Total Submissions: 4.3M
# Testcase Example:  '5\n4'
#
# You are a product manager and currently leading a team to develop a new
# product. Unfortunately, the latest version of your product fails the quality
# check. Since each version is developed based on the previous version, all the
# versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first
# bad one, which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which returns whether version
# is bad. Implement a function to find the first bad version. You should
# minimize the number of calls to the API.
#
#
# Example 1:
#
#
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
#
#
# Example 2:
#
#
# Input: n = 1, bad = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= bad <= n <= 2^31 - 1
#
#
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        def findFirstBad(left, right) -> int:
            if left >= right:
                return left
            mid: int = (left + right) // 2
            if isBadVersion(version=mid):
                return findFirstBad(left=left, right=mid)

            return findFirstBad(left=mid + 1, right=right)

        return findFirstBad(left=1, right=n)


# @lc code=end

"""
BAD_VERSION: int = 0


def isBadVersion(version: int) -> bool:
    return version == BAD_VERSION


solution: Solution = Solution()

import random

BAD_VERSION = 1
print(f"N=1, BAD_VERSION = {BAD_VERSION}, OUT={solution.firstBadVersion(n=1)}")
BAD_VERSION = 1
print(f"N=4, BAD_VERSION = {BAD_VERSION}, OUT={solution.firstBadVersion(n=4)}")

BAD_VERSION = 19
print(f"N=30, BAD_VERSION = {BAD_VERSION}, OUT={solution.firstBadVersion(n=30)}")
BAD_VERSION = 485
print(f"N=990, BAD_VERSION = {BAD_VERSION}, OUT={solution.firstBadVersion(n=990)}")
BAD_VERSION = 2**16 - random.randint(a=0, b=(2**16) - 1)
print(f"N=2^16, BAD_VERSION = {BAD_VERSION}, OUT={solution.firstBadVersion(n=2**16)}")
BAD_VERSION = 924121
print(
    f"N=114124121, BAD_VERSION = {BAD_VERSION}, OUT={solution.firstBadVersion(n=114124121)}"
)
@notes post-mortem=start
-----BEGIN PGP MESSAGE-----

hF4DjxTuSjEZ/v8SAQdAIsboGvgg5UJjhFjkUyMOINxexsXjVU9WtwtZl2C1XmEw
hCBskhT+oXA/qmRt+LAgVJa/vR9INYe28TMkP+s0/mdYlCv+IoJDrzF6oAvDm8r2
0ukBEeP3YPFgZ3x0UgFnVKncE5POyNxYnma+T392YkVHwiANVzq2pDDOMJ8Bzoxi
qsSg8gJxv4t1TnveXJRd1Vu+xAHVQvDhgZqXR2iA1/mDb+cRFNFIWpBso4sedPHN
GA6zo9RAuf4ucZufxpdTa3ePZ40QLuJndCXu0l4tYmvM568VQTdzpWXeR20mCDW1
zGq3DItkAl2mM9ibTv0tkSMc8EsLnmw4oN4+8/cJkWe7SlXsrCehBZ6Xr4jmggPW
8QU54S4B6gpsQRiLwHFb9CovKLUW7hKu20LcukFUfvxcmx+8yZw0mge+wSJOhh2p
n2SdnZN/Oov0dW6vgSi03PStmIYmP71oqLiR2ASHS2yOpBjDYBp5ttD2GpRujbkk
h8xpNdnhQUu+18Z/wMOndo+BVibbv4E8+XUcyZOf29vTjc/lmDxiQWDzHAip6yx6
TWQOgixMFKdy/GSGGApGYEZz8Jt/xkzn8A8rSPqj+wat3UW6LzkecxpU3tMksz+V
dLqjlBgsABQSUi/pL33/LGqf4lZBFPlTBPzDqIYdpA8d04KPm6pxvuxC38bRV/z3
qOEz4iHZtX/WeS4kDsuHDTC6M8Si0Z/02SUZLDQcfoad+cf35ooYRAEhvRxLhF3v
084o/tV4HNRSQWqeBRBJSMN2XKaIt35zpjpNKFhojYCvPWBe4/LF05y9PuI3AuFR
d7SpgN3K0e3jRY/FJ5q+4QHWhKf+7weSjCNAVxr5pjeEs/qCcyqZJNQ7iT8rkyVg
HllkaZWMeU1Kr3jU3n1QxtAqYi+isaQIP0BgSRMr1bac+0A=
=cbMr
-----END PGP MESSAGE-----
@notes post-mortem=end


"""
