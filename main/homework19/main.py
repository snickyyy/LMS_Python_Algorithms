arr = [1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 6, 7, 7, 2] # 6
arr = [3, 4, 7, 6, 6, 3, 2, 3, 4, 9] # 5
arr = [1, 4, 2, 5, 6, 1, 2, 8, 8, 7, 0, 2, 3, 6, 9] # 8
arr = [1, 4, 8, 7, 8, 9, 7, 10] # 2
arr = [1, 3, 2, 4, 3, 5, 5, 6, 3, 7] # 3
arr = [1, 2, 2, 4, 5, 6, 4, 7, 6, 6, 4, 3, 4, 6] # 3
arr = [1, 2, 2, 4, 5, 4, 6, 7, 6, 6, 4, 3, 4, 6, 6, 3, 2, 1] # 3
arr = [1,2,3,4,5,4, 3, 2, 3, 6,1,7] # 5
arr = [1,6,1,2] # 1
arr = [1, 4, 2, 5, 8, 7, 5, 5, 6, 4, 5, 8, 9, 9, 10, 3] # 4
arr = [1, 2, 3, 4, 3, 2, 1] # 0
arr = [0, 0, 0, 0, 0] # 0
arr = [5, 3, 6, 1, 4, 2, 7] # 4
arr = [9, 1, 2, 1, 9] # 8
arr = [0, 2, 1, 3, 4, 1, 5] # 3
arr = [7, 5, 3, 6, 8, 7, 2, 5, 9] # 6
arr = [1, 2, 1, 2, 1, 2, 1, 2] # 1
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # 0
arr = [1, 3, 2, 5, 4, 6, 3, 8, 7] # 3
arr = [1, 7, 3, 6, 2, 5, 9] # 5
arr = []

def maximum_depth(arr: list):
    """
    Прикреплю что было сделано за пол часа.
    А сумарно ушло 3:12:05
    Зато скорость O(n)
    """
    if not arr:
        return 0
    arr.reverse()
    last_first = arr[0]
    for _ in arr[1:]:
        if _ >= last_first:
            arr.remove(last_first)
            last_first = _
        else:
            break
    arr.reverse()
    last = arr[0]
    hill_flag = False
    current_hill = 0
    current_depth = 0
    all_depths = []
    for i in arr[1:]:
        if i < last:
            if not hill_flag:
                hill_flag = True
                current_hill = last
                current_depth = current_hill - i
            else:
                current_depth = current_hill - i
        else:
            if i >= current_hill and last != i:
                hill_flag = False
                all_depths.append(current_depth)
                current_hill = i
                current_depth = 0
        last = i
    if hill_flag:
        current_depth -= (current_hill - last)
        all_depths.append(current_depth)
    try:
        return max(all_depths)
    except ValueError:
        return 0


def main():
    print(maximum_depth(arr))

if __name__ == "__main__":
    main()















# def maximum_depth(arr: list):
#     min_depth = min(arr)
#     arr = "".join(map(str, arr))
#     arr = arr.split(str(min_depth))
#
#     left_arr = list(map(int, list(arr[0])))
#     right_arr = list(map(int, list(arr[1])))
#     left_arr.reverse()
#
#     max_left, max_right = max(left_arr), max(right_arr)
#
#     min_all = min(max_left, max_right)
#
#     return min_all - min_depth
