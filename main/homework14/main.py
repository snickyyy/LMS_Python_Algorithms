nums = [13,25,83,77] # out [1,3,2,5,8,3,7,7]
# nums = [7,1,3,9] # out [7,1,3,9]
def separateDigits(nums: list[int]) -> list[int]:
        """
        link: https://leetcode.com/problems/separate-the-digits-in-an-array/description/
        difficulty: Easy
        """
        return list(map(int, list("".join(list(map(str, nums))))))

def maximumWealth(accounts: list[list[int]]) -> int:
        """
        link: https://leetcode.com/problems/richest-customer-wealth/description/
        difficulty: Easy
        """
        max_data = 0
        for i in accounts:
                if sum(i) > max_data:
                        max_data = sum(i)
        return max_data
