#
# @lc app=leetcode.cn id=304 lang=python3
#
# [304] 二维区域和检索 - 矩阵不可变
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), (len(matrix[0]) if matrix else 0)
        self.sums = [[0]*(n+1) for _ in range(m)]
        _sums = self.sums
        
        for i in range(m):
            for j in range(n):
                _sum[i][j+1] = _sums[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sums = self.sums
        total = sum(_sums[i][col2 + 1] - _sums)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

