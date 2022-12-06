#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#


# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sum_to_now = [0]
        for i in nums:
            self.sum_to_now.append(self.sum_to_now[-1] + i)

    def sumRange(self, left: int, right: int) -> int:
        return self.sum_to_now[right + 1] - self.sum_to_now[left]


# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums = nums

#     def sumRange(self, left: int, right: int) -> int:
#         return sum(self.nums[left : right + 1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end
