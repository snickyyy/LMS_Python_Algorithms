# arr = [
#    [1, 4],
#    [7, 10],
#    [3, 5]
# ] # out 7 because 10 - 7 = 3, 5 - 1 = 4 || intr = [[7, 10], [1, 5]]
# arr = [
#    [1, 2],
#    [6, 10],
#    [11, 15]
# ]
arr = [
   [1, 5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] # out 19
# arr = [
#    [0, 20],
#    [-100000000, 10],
#    [30, 40]
# ]

"""
[1, 4],
[3, 5],
[7, 10],
]
------------------------------------
[1, 5],
[1, 6],
[5, 11]
[10, 20],
[16, 19],
"""

def sum_of_intervals(arr):
    if not arr:
        return 0
    intervals = []
    arr.sort(key=lambda x: x[0])
    min_el = arr[0][0]
    max_el = arr[0][1]
    for i in arr:
        if i[0] <= max_el:
            if i[1] > max_el:
                max_el = i[1]
        else:
            intervals.append((min_el, max_el))
            min_el, max_el = i[0], i[1]
    intervals.append((min_el, max_el))
    sum_intervals = sum(j - i for i, j in intervals)
    return sum_intervals


print(sum_of_intervals(arr))

