# nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums_2 = sorted(list(set(nums)))
    nums_3 = [] + nums_2
    for i in range(len(nums) - len(nums_2)):
        nums_3.append("_")
    return nums_2

print(removeDuplicates(nums))