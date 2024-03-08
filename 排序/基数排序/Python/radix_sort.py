import sys
sys.path.append('/Users/zengxiaowei/STUDY/Github/LeetCode/Python_Engineer/Sort/QuickSort/Python')
from calculate_execute_time import d_calculate_execute_time
from leetcode_data import nums

def max_digit(max_value):
    counts = 0
    while max_value > 0:
        counts += 1
        max_value //= 10
    return counts

def find_digit_number(number, digit):
    while digit > 0:
        number //= 10
        digit -= 1
    number %= 10
    return number

@d_calculate_execute_time
def radix_sort(nums):
    min_value, max_value = min(nums), max(nums)
    for i in range(len(nums)):
        nums[i] += (abs(min_value) + 1)
    max_value += (abs(min_value) + 1)
    # 获得最大数的位数
    counting_digit = max_digit(max_value)
    print(f"max_value = {max_value}, counting_digit = {counting_digit}")
    # 开始根据每一位进行排序
    for i in range(0, counting_digit):
        bucket = [[] for _ in range(10)]
        for value in nums:
            bucket[find_digit_number(value, i)].append(value)
        new_index = 0
        for i in range(10):
            if len(bucket[i]) > 0:
                for item in bucket[i]:
                    nums[new_index] = item
                    new_index += 1
    for i in range(len(nums)):
        nums[i] -= (abs(min_value) + 1)
    return nums


#nums = [38, -159, -53648, 129, 128, 317, 42537]
radix_sort(nums)