#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-Sudoku/description/
#
# algorithms
# Medium (62.35%)
# Likes:    11597
# Dislikes: 1208
# Total Accepted:    2M
# Total Submissions: 3.3M
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:
#
#
# Each row must contain the digits 1-9 without repetition.
# Each c must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
# without repetition.
#
#
# Note:
#
#
# A Sudoku board (partially filled) could be valid but is not necessarily
# solvable.
# Only the filled cells need to be validated according to the mentioned
# rules.
#
#
#
# Example 1:
#
#
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
#
#
# Example 2:
#
#
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner
# being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it
# is invalid.
#
#
#
# Constraints:
#
#
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.
#
#
#

from typing import List

# @lc code=start
class Solution:
    def getBlockNumber(self, r: int, c: int) -> int:
        if r < 3:
            if c < 3:
                return 0
            if c < 6:
                return 1
            return 2
        if r < 6:
            if c < 3:
                return 3
            if c < 6:
                return 4
            return 5
        if c < 3:
            return 6
        if c < 6:
            return 7
        return 8

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        table = {}
        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val == ".":
                    continue
                block_number = self.getBlockNumber(r, c)
                if table.get(
                    f"r_{r}:{val}",
                    table.get(
                        f"c_{c}:{val}", table.get(f"b_{block_number}:{val}", False)
                    ),
                ):
                    return False
                (
                    table[f"r_{r}:{val}"],
                    table[f"c_{c}:{val}"],
                    table[f"b_{block_number}:{val}"],
                ) = True, True, True
        return True

# @lc code=end

solution = Solution()
assert solution.isValidSudoku(
    [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)
assert not solution.isValidSudoku(
    [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)

assert solution.isValidSudoku(
    [
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]
)

'''
Understanding:
    Goal: To validate if a 9x9 Sudoku is valid (True|False).
    - Rules for rows, columns and 3x3blocks:
        - x can be "." or [1-9]
        - 1 <= x <= 9 (without duplicates)
        - if x != "."; then skip
    - Other:
        - A valid Sudoku board is not the same as a solvable Sudoku.
        Input: [ [x]*9 ]
            {     3x3block    }
            [ x00 | x01 | x02 |... x09 ]
            [ x01 | x11 | x12 |... x19 ]
            [ x20 | x21 | x22 |... x29 ]
            ...
            [ x90 | x91 | x92 |... x99 ]
ICE was not executed :(
Pseudocode: Bruteforce + Hash Table for checking for duplicates.
    Declare the Hashtable: table = {}
    Declare block_number = 0
    For r,row in enumerate(board):
        For c in range(9):
            If row[c] is not a number, then Skip this iteration;
            Set block_number value based on r and c;
            If theres any entry in table for r_0:row[c]|c_0:row[c]|b_0:row[c], then Return False;
            Add r_0:row[c]|c_0:row[c]|b_0:row[c] to table;
    Return True
Hand-Testing:
    Input = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]

    - 0,0: table.get(r_0:5|c_0:5|b_0:5) -> False,False,False,False: OK
    - 0,1: table.get(r_0:3|c_1:3|b_0:3) -> False,False,False: OK
    - 0,2: continue: OK
    - 0,3: continue: OK
    - 0,4: table.get(r_0:7|c_4:7|b_0:7) -> False,False,False: OK
    - 0,5: continue: OK
    - 0,6: continue: OK
    - 0,7: continue: OK
    - 0,8: continue: OK

    - 1,0: table.get(r_1:5|c_0:5|b_0:5) -> False,False,False,False: OK
    - 1,1: continue
    - 1,2: continue
    - 1,3: table.get(r_1:1|c_3:1|b_1:1) -> False,False,False: OK
    - 1,4: table.get(r_1:9|c_4:9|b_1:9) -> False,False,False: OK
    - 1,5: table.get(r_1:5|c_5:5|b_1:5) -> False,False,False: OK
    - 1,6: continue: OK
    - 1,7: continue: OK
    - 1,8: continue: OK

    - 2,0: continue: OK
    - 2,1: table.get(r_2:9|c_1:9|b_0:9) -> False,False,False,False: OK
    - 2,2: table.get(r_2:8|c_2:8|b_0:8) -> False,False,False,False: OK
    - 2,3: continue: OK
    - 2,4: continue: OK
    - 2,5: continue: OK
    - 2,6: continue: OK
    - 2,7: table.get(r_2:6|c_7:6|b_0:6) -> False,False,False,False: OK
    - 2,8: continue: OK
    
    ...

@notes post-mortem=start
-----BEGIN PGP MESSAGE-----

hF4DjxTuSjEZ/v8SAQdApOJMnMZbNh3PyAHWAwKOzGNmpILuKJYOfmis5pe29W4w
0SYdfQasuZnDwjZ6sVCU88yYYs+xQ7ncMc/eRz2sQS4m7UISUKITErvTWrv219nA
0sERAcGLnOjIIqJcbBZXk4nGbxtZV2k80b+zLtXVQBkIQKzpXK09SGGkUVIvsHM5
MlL6+gEZkJW4fKtjaagBnjG8eGEnpGGW9WgallVttHxelJUJ3LhVfnEp5Xv383f/
zySET3v3BDPdO4w/m2Odck4UmwO8zCrCnCXj6zGw539YeCkdULfaAHQ9oZVVeSJd
b6kA3+bFmyfVgPI0CBM3Kvwal9IMVCKlqscZxoyW9ghBjHrXVURQfj/tlXy2za2F
jCG8y3fbsRhYFZveKfiIJs1M2npuVv8alfJYsKinKH+QSZniTI8nwmexVPuaqUdb
jpROLDOszxMvo6SqHGi5MM6mtfke23PlfIzfhIFBbem39/TL+PDlNKRQROZtQlm/
cB6gupmeU6Sc3nqe1tGveuyMIEqvJ9Nh0g1mGqXNyWrH58RcRm9Blv7BjMpzpFBr
DmN4s2Io/jP5Kn8/IGOBNDD2G5l1tlzo2UNoyzJsbZmE80ZS/QWl9MGRGwO1dOUD
ciBE6C++1SWp+iAlWSWim0sE2Y0ombFqPCr+X0A63RVmzVymLemufOphr5DGsit0
2PH8/8nWy3oHlDvhhtSohaDEznQr9ToOl2fI5Onz+cydZbke
=J9Ye
-----END PGP MESSAGE-----
@notes post-mortem=end
'''
