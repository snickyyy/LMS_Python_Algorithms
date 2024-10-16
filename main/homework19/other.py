def addDigits(num):
    """
    link: https://leetcode.com/problems/add-digits/description/
    complexity: Easy
    :type num: int
    :rtype: int
    """
    while len(str(num)) != 1:
        num = sum(list(map(int, list(str(num)))))
    return num


# arr = ["a", "a", "a", "b", "b"]
arr = ["a", "b", "c", "b", "c"]

def check_three_and_two(array):
    """
    link: https://www.codewars.com/kata/5a9e86705ee396d6be000091/train/python
    """
    res = sorted({i: array.count(i) for i in array}.values()) == [2,3]
    return res


def main():
    print(check_three_and_two(arr))


if __name__ == "__main__":
    main()
