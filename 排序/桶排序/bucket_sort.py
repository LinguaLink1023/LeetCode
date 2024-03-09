import math
# import sys
# sys.path.append('/Users/zengxiaowei/STUDY/Github/LeetCode/Python_Coding/排序')

# from 排序.calculate_execute_time import d_calculate_execute_time
# from 排序.leetcode_data import nums

#@d_calculate_execute_time
def bucket_sort(nums):
    if min(nums) < 0:
        bias = -min(nums)
    else:
        bias = 0
    nums = [num + bias for num in nums]
    min_value, max_value = min(nums), max(nums)
    bucket_range = math.ceil((max_value - min_value) / len(nums))
    bucket_range = bucket_range + 1 if bucket_range < 1 else bucket_range
    bucket_list = [[] for _ in range((max_value - min_value) // bucket_range + 1)]
    for num in nums:
        bucket_list[(num - min_value) // bucket_range].append(num)
    sorted_nums = []
    for bucket in bucket_list:
        if not bucket:
            continue
        sorted_nums.extend(insertion_sort(bucket))
    sorted_nums = [num - bias for num in sorted_nums]
    return sorted_nums



def insertion_sort(nums):
    for i in range(len(nums)):
        preIndex = i-1
        current = nums[i]
        while preIndex >=0 and nums[preIndex] > current:
            nums[preIndex+1] = nums[preIndex]
            preIndex-=1
        nums[preIndex+1] = current
    return nums
        
#nums = [38, -159, -53648, 129, 128, 317, 42537]
#nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 10000, 10000, 9999, 9999, 9998, 9998, 9997, 9997, 9996, 9996]
nums = [0]
print(bucket_sort(nums))