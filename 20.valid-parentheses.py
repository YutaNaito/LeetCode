#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = []
        parentheses_dict = {"]": "[", "}": "{", ")": "("}
        for c in s:
            if c in parentheses_dict.values():
                tmp.append(c)
            elif tmp != [] and parentheses_dict[c] == tmp[-1]:
                tmp.pop()
            else:
                return False

        return tmp == []


# @lc code=end
