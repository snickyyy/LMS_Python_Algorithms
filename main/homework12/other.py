class Solution(object):
    def twoSum(self, nums, target):
        """
        task: https://leetcode.com/problems/two-sum/description/
        complexity: Easy

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """1 вариант"""
        entryDeg = {}
        for index, num in enumerate(nums):
            if num in entryDeg:
                return entryDeg[num], index
            delta = target - num
            entryDeg[delta] = index

        # """2 вариант"""
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i, j
    def findMedianSortedArrays(self, nums1, nums2):
        """
        task: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
        complexity: Hard

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lst = sorted(nums1 + nums2)

        if len(lst) % 2 != 0:
            return float(lst[(len(lst) - 1) // 2])

        firstEl = int(((len(lst)) / 2) - 0.5)
        secondEl = int(((len(lst)) / 2) + 0.5)
        print(firstEl, secondEl)

        return (lst[firstEl]+lst[secondEl]) / 2
    def isValid(self, s):
        """
        task: https://leetcode.com/problems/valid-parentheses/
        complexity: Easy
        :type s: str
        :rtype: bool
        """
        for i in s:
            if i not in "{}[]()":
                s.replace(i,"")

        while "{}" in s or "[]" in s or "()" in s:
            s = s.replace("{}", "").replace("[]", "").replace("()", "")
        return False if s else True

    def searchInsert(self, nums, target):
        """
        task: https://leetcode.com/problems/search-insert-position/description/
        complexity: Easy
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        for i in nums:
            if i >= target:
                return nums.index(i)
        return len(nums)

sol = Solution()
print(sol.findMedianSortedArrays([1,2], [3,4]))