def twoSum(nums, target):
    for i in nums:
        for j in nums:
            if i + j == target:
                return nums.index(i), nums.index(j)
    return tuple()

print(twoSum([3, 3], 6))

