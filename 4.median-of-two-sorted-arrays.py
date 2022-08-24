#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums_len = len(nums1) + len(nums2)
        nums = nums1 + nums2
        nums.sort()
        if (nums_len % 2 == 0):
            right_med = nums_len / 2
            answer = (nums[right_med - 1] + nums[right_med]) / 2.0
            return answer
        else:
            med = (nums_len - 1) / 2
            answer = nums[med]
        return answer
# @lc code=end

