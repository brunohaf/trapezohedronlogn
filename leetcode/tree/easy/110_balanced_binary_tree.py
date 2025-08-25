#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (55.69%)
# Likes:    11512
# Dislikes: 789
# Total Accepted:    2M
# Total Submissions: 3.6M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#
#
# Example 3:
#
#
# Input: root = []
# Output: true
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 5000].
# -10^4 <= Node.val <= 10^4
#
#
#

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_height: int = getHeight(node=node.left)
            right_height: int = getHeight(node=node.right)

            if (
                left_height == -1
                or right_height == -1
                or (abs(left_height - right_height) > 1)
            ):
                return -1

            return max(left_height, right_height) + 1

        return getHeight(node=root) >= 0


# @lc code=end

"""
Test Cases: [1,2,2,3,null,null,3,4,null,null,4]\n[1,2,2,3,3,null,null,4,4]\n[]\n[3,9,20,null,null,15,7]

@notes post-mortem=start
-----BEGIN PGP MESSAGE-----

hF4DjxTuSjEZ/v8SAQdAQ//IKgZun2yXVfMsu70xPibhs4RBuxdmwvHU4YwF3SQw
gH7QV1cIIZCnvvuRWESTXFJ6PDLaJ20eeBK/w4y/TUN7RrHZWI1mhcEmsr1wzMrE
0uoBJ+a7uKubAOSt4iPLiojOJUfjyFt9TGMMsF/vqqfhfF4VdOM7bPQT/PplBtKS
tnvqEl/xG5CzSfxVJrrA1awTKX5wnWM0KcVVty6wPkqCtSUZm4SI2x9vSPCVixNG
IAMmoJG0bfRvb3hRPnhGCptpUYQ9XC7GwJkidHlnS3xn94moUHbzlUVB9PEWuudv
QickaF7ALOllqu5XNnH8NpfsudPs8kolTBUEY7fs5j1rcBaLNNc95MBnvCLYHvhs
bWLLh6qtyV6NNXYhhNwD2k1xqRxXrarw18gZxvxbGIxlVlW+PpvFlgFnygdH+CLE
MaGCjoOtdUEae1EUVQm169cbEeRoEH6l3YREyydbmOqymvLU2Pltz5FV1eGF0GfO
SGltQ757e+LqeWKLowdNosmfV8U4ILY2XYFSD4iZ7kZuTuQde8T5cyFI28tWWD+k
CG3dmHXUl/RglVXuXW1kHioz+cZ3jgnYyWwsDM+nLEmL99TerElY5EVBeOgRb+rf
hk0jQgdrSshZvUyHdvdTywbSmbbyIJTanjfs70UyVGCDd74hdOsp/INIpFxFpapD
9dullG5DCGDQb384V8lk+NikyoDvx5SMnJZfrIXdiANWR1qBIQqeEO5hpi0lMIzN
i9DVZQUKm6uSyV4F+FjrDDxAhgetZ6alu5xYQGvHcinvhOAppEZODRqpmzm/Zfm2
2jLuVn3YnilRd6jt0x4oZTPdUdtDJPr5drFSfC5zm/iCLwNyNu54qwSGVhMsRwdX
K7y8uqin615jPnfn1/hEJyhYBksqxhoAG2m2cL5+GFllERrknV9UMBEkt7aI1Jhk
msxC1MY/wD5iwSbYvLdgjDq98eDj+c8ik56NmYLEsJ8brGkn+T6ofJBzNTNyKOhp
ZOkmHupBoKAFY1Rz9u0T3I2u/KIBXXXyqUyyyITbm1FY6PY+PeWQaDgte4WABgBY
Heh686LMQdXWXwfaUUaHM/35RJftSIbeaQgmg2oWUuNxM6uYeLhR98BCWKAyzNm1
7nJXit9FrjFt9e8mbHDRcLi61x7gY/rCjphRBobZZHR+xpVwWxS1FFqFV2B3u99n
/+hyPUhZwNBe355iZSs3q23ooz9L44EU22Agpj3yM/nAVW/PHouFTs1QoazhZ55D
/DKIPbkNjA5Q2Pnd1oK+JX41A6U96Ppekebcl/zZFx890/lho/JMqaP9kq7RCRVq
fReo3gUYYfvB3NMsmhb8KRjaQJv6X2CM5zMmBpnGtERRJrrA7WBpynZdkGx7f/ch
FfzTkREqNBI8pzeGvSa+f9oRjSVhmEW+1PKDzAQY9by4h0etvUaK9MH/mMX4q6je
Ym0TzmTlIPdV/BDAtoB5aSS1wC8Xg/uA88BdANpHfUP2b5O0r8jOTOiB/BO6y5Vx
MgE04zlBD+ruL249TbFwg7qsML0xt1vHuK7J3+VN42VculDsf+f0Dd73Cyay45g0
kjfJtNKX8sE4y1kx3ZetfrpBafPjYaM70MVD952Y4DWKFeRw6xXQ0eT/gM/0BeRL
of8i8TBsngYdiSZab1veN7+nky9cfVOrViHZKQFizBwxvAwsOe7Xl4hpPfXUy6nd
RMdNcf0FSp92oguJzpKtnD8cCIn4ds6v8bei7T2hESKZKy08hRt9Wguaoek5rcTx
VxAVmKBeNvIENTAceVGQxjS1BA==
=XedV
-----END PGP MESSAGE-----
@notes post-mortem=end
"""
