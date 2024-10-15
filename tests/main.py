arr = [0,1,0,2,1,0,1,3,2,1,2,1] # 6

def count_depth(arr: list):
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
    all_depths = []
    for i in arr[1:]:
        if i < last:
            if not hill_flag:
                hill_flag = True
                current_hill = last
                all_depths.append(current_hill - i)
            else:
                all_depths.append(current_hill - i)
        elif i >= current_hill and last != i:
            hill_flag = False
        last = i
    try:
        return sum(all_depths)
    except ValueError:
        return 0


def main():
    print(count_depth(arr))

if __name__ == "__main__":
    main()
