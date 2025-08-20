#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#
# algorithms
# Medium (68.68%)
# Likes:    11859
# Dislikes: 341
# Total Accepted:    2M
# Total Submissions: 2.9M
# Testcase Example:  '[6,2,8,0,4,7,9,null,null,3,5]\n2\n8'
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node
# of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of
# itself).”
#
#
# Example 1:
#
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
#
#
# Example 2:
#
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant
# of itself according to the LCA definition.
#
#
# Example 3:
#
#
# Input: root = [2,1], p = 2, q = 1
# Output: 2
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q will exist in the BST.
#
#
#


# import logging
# logging.basicConfig(level=logging.INFO)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


# @lc code=start
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        node: TreeNode = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node


# @lc code=end

"""
@+  def getParents(self, root: "TreeNode", target: "TreeNode") -> list["TreeNode"]:
@+     node: TreeNode | None = root
@+     parents: list["TreeNode"] = []
@+     while node is not None:
@+         parents.append(node)
@+         if node.val == target.val:
@+             break
@+         node = node.right if target.val > node.val else node.left
@+     return parents

! def lowestCommonAncestor(
@+     self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
@+ ) -> "TreeNode":
@+     p_parents: list[TreeNode] = self.getParents(root, target=p)
@+     q_parents: list[TreeNode] = self.getParents(root, target=q)
@+ 
@+     lca = None
@+     for pp, qp in zip(p_parents, q_parents):
@+         if pp != qp:
@+             break
@+         lca = pp
@+     return lca


? TEST Stuff
def buildRoot(
    input: list[int | None], p: int, q: int
) -> tuple[TreeNode, TreeNode, TreeNode]:
    nodes = []
    for i in range(len(input)):
        node = TreeNode(input[i])
        node.left = TreeNode(input[2 * i + 1]) if (2 * i + 1) < len(input) - 1 else None
        node.right = (
            TreeNode(input[2 * i + 2]) if (2 * i + 2) < len(input) - 1 else None
        )
        nodes.append(node)
        if node.val == p:
            p = node
        elif node.val == q:
            q = node
    return (nodes[0], p, q)


# @lc code=end
sol = Solution()
assert (
    sol.lowestCommonAncestor(
        *buildRoot(input=[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], p=2, q=8)
    ).val
    == 6
)
assert (
    sol.lowestCommonAncestor(
        *buildRoot(input=[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], p=2, q=4)
    ).val
    == 2
)
assert (
    sol.lowestCommonAncestor(
        *buildRoot(input=[5, 3, 6, 2, 4, None, None, 1], p=1, q=3)
    ).val
    == 3
)

@notes post-mortem=start
-----BEGIN PGP MESSAGE-----

hF4DjxTuSjEZ/v8SAQdAsS1/wKGVlidzxYutI1Dutlm+qx5wywaZHwNjggahSQEw
aYlk/aHSc0b4Y2/OTF5gXU4GTdBbmFBQCiaF4uqNbYIIq+SuNA1zeplvdDh7Ys2Q
0ukBRemRL5y4zMz1n/fjM1RlGI7nPuiSSHw72emEWyTnacRN/On7pOJ+BLKdSYZr
YLDHKCB4V3sd4tgp2Aw/L9XKHkPNZs2siWouNWKpR8z9hcop0VjyoZoy05aVNNvN
C/WYzlAYDeV+nXBMTEHkuyiYpsN34H0wUiLL4jyQY/vsrS4tDdU+G6zKWylvxKtS
OripwyKt+Gz4bNFvKdNZV1lidf0VO2Sk/GNZEyyxqHF4LtdpHeHZeVsc+CHsdlh4
2/5GKgAnA/NK+7vlznCCzjgG01xCA04YBOJ+UVM+deoh6EJAMKGWMuoHlqEciRUt
rDg7JSCTTF60qzr/wRQG9RKC43OFVbIipRuErxv/Wc1WKwmbaxouE7dKrJfXanDh
+gzsVaqglWa81P9qKIes3Z78PFajEPvwsP0UA0bfu13aQnkrwATAfDmCujyS0t+E
GVIG0RW+djnbWmASI0OWPPFWZN6vaXLagsYJqADW6trOv2HLNiT0w79aPwdLOK5/
FKlQQy/bVi64EF3NdALnzbZPzmnFXXol7zZW2V/oVGGX+VBoTqwE8I6hlKN+5Qsj
noRKVdvqOnnrCN16Ymrhmt2Q4tlv1xkja9Qtx8lnoKfVN7f6My/bZkcVzwEi4Pc/
h2qgpLSG6Iw/qWLaRkFqqpHWHmrIXV8/C1TswM+kuusy6cCCFiroP6iIEzgXzxGq
PitxxRL0B++akWJFzounEbOQBLQKrZQlLEXMBO3pUZkgqFvcavk4AIEs0WWg/bUb
kxufXGGVv6YGMNxKCBuBlnBopo0R4Shm2GuHSQAQmfq1gkG/TDYBkSJH1d+nTUlM
8o05cxnTqn3LMubuv0/XCVCbbQxM5K/MFdbvJPrpk27iEvVfYl8GWVZhUQYi3GVG
QPmVJmJ9X1KCPMD0zOFdyblbLyBm1tayYvmgRCzCYhmPNYjN9kHGzaS/nqxFNCE2
jcZRnF3xhmhlnjNJaGLUgs45m+ptasrp6V9IYAU54Im2sRVWF2tT4fdjqsPaGPOg
0Bniz9pXYLu40qVSLn6UvYrqMYxQ1Er7SupP39/5eeOIrL/jDovo0DYlnJP3PFqR
ccx0z1U/K/UnLX09uIy+HDcpnctuhA==
=/m3L
-----END PGP MESSAGE-----
@notes post-mortem=end
"""
