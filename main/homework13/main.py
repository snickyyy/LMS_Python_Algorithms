# arr = ["dog", "racecar", "car"] # out "fl"
# arr = ["flower", "floor", "flosk"]
# arr = ["flower", "flower", "flower"]
# arr = ["Python", "Pytak", "Pyyyyyy"]
# arr = ["Py", "srgPy", "efwrgrPy"]
arr = ["ab", "a"]


def longestCommonPrefix(arr):
    """
    link: https://leetcode.com/problems/longest-common-prefix/
    complexity: easy
    """
    idx = 0
    prefix = ""
    for i in arr[0]:
        for j in arr:
            try: 
                if j[idx] != i:
                    return prefix
            except IndexError:
                return prefix
        prefix += i
        idx += 1
    return prefix
print(longestCommonPrefix(arr))

# arr = [1, 2], [3] # out 2
# arr = [1,2], [3,4] # out 2.5 because (2 + 3) / 2 = 2.5
# arr = [1, 2], [6, 12] # out 4 because (2 + 6) / 2 = 4.0


def findMedianSortedArrays(nums1, nums2) -> float:
    """
    link: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
    complexity: Hard
    """
    arr = sorted(nums1 + nums2)
    len_array = len(arr)

    if len_array % 2 != 0:
        return float(arr[(len_array - 1) // 2])
    
    return (arr[int(((len_array - 1) / 2) - 0.5)] + arr[int(((len_array - 1) / 2) + 0.5)]) / 2