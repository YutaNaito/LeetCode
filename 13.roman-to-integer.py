#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):

    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    def romanToInt(self, s: str) -> str:
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        y = 0
        for i in s[::-1]:
            if y == 0 or y <= self.dict[i]:
                sum += self.dict[i]
            else:
                sum -= self.dict[i]
            y = self.dict[i]
        return sum        

# @lc code=end