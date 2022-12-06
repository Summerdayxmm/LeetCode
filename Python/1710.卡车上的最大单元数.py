#
# @lc app=leetcode.cn id=1710 lang=python3
#
# [1710] 卡车上的最大单元数
#


# @lc code=start
class Solution:

    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        res = 0 
        for numberOfBoxes, numberOfUnitsPerBox in boxTypes:
            if numberOfBoxes >= truckSize:
                res += truckSize * numberOfUnitsPerBox
                break
            res += numberOfBoxes * numberOfUnitsPerBox
            truckSize -= numberOfBoxes
        return res
                


# @lc code=end
