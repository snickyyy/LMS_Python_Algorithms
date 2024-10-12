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
# def sum_of_intervals(arr):
#     if not arr:
#         return 0
#     arr.sort(key=lambda x: x[0])
#     min_el, max_el = arr[0]
#     intevals = {(min_el, max_el): max_el - min_el}
#     for i in arr[1:]:
#         if i[0] <= max_el:
#             intevals.pop((min_el, max_el))
#             intevals[min_el, i[1]] = i[1] - min_el
#             max_el = i[1]
#             continue
#         intevals[(i[0], i[1])] = i[1] - i[0]
#     return sum(intevals.values())

def sum_of_intervals(arr):
    if not arr:
        return 0
    intervals = []
    arr.sort(key=lambda x: x[0])
    min_el = arr[0][0]
    max_el = arr[0][1]
    for i in arr:
        if i[0] <= max_el:
            # max_el = max(max_el, i[1])
            if i[1] >= max_el:
                max_el = i[1]
        else:
            intervals.append((min_el, max_el))
            min_el, max_el = i[0], i[1]
    intervals.append((min_el, max_el))
    sum_intervals = sum(j - i for i, j in intervals)
    return sum_intervals


    # for first, last in arr:
    #     if not min_interval:
    #         min_interval = [first, last]
    #     elif first < min_interval[1]:
    #         if last - min_interval[0] >= min_interval[1] - min_interval[0] and first >= min_interval[0] and interval_flag:
    #             intervals[tuple(min_interval)] = last - min_interval[0]
    #             min_interval[1] = last
    #             interval_flag = False
    #             continue
    #         elif last - min_interval[0] >= min_interval[1] - min_interval[0] and first <= min_interval[0] and interval_flag:
    #             intervals[tuple(min_interval)] = last - first
    #             min_interval = [first, last]
    #             interval_flag = False
    #             continue
    #     intervals[first, last] = last - first
    # return f"{min_interval}\n{intervals}\n{sum(intervals.values())}"
print(sum_of_intervals(arr))
# assert(sum_of_intervals([(-1_000_000_000, 1_000_000_000)]), 2_000_000_000)

