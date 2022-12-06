#
# @lc app=leetcode.cn id=1796 lang=python3
#
# [1796] 字符串中第二大的数字
#

# @lc code=start
class Solution:
    def secondHighest(self, s: str) -> int:
       mask = reduce(or_, (1 << int(c) for c in s if c.isdigit()), 0)
       cnt = 0
       for i in range(9, -1, -1):
           if (mask >> i) & 1:
               cnt += 1
               if cnt == 2:
                   return i
       return -1
# @lc code=end
# class Solution:
#     def secondHighest(self, s: str) -> int:
#         first = second = -1
#         for c in s:
#             if c.isdigit():
#                 num = int(c)
#                 if num > first:
#                     second = first
#                     first = num
#                 elif second < num < first:
#                     second = num
#         return second
