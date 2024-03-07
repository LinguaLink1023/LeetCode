import sys
sys.path.append('/Users/zengxiaowei/STUDY/Github/LeetCode/Python_Engineer/Sort/QuickSort/Python')
from calculate_execute_time import d_calculate_execute_time
from leetcode_data import nums


@d_calculate_execute_time
def counter_sort(nums):
    max_value, min_value = max(nums), min(nums)
    counter_nums = [0 for _ in range(max_value - min_value + 1)]
    #print(max_value - (min_value if min_value < 0 else 0) + 1)
    for value in nums:
        counter_nums[value - min_value] += 1
           
    new_num = 0 
    for j in range(len(counter_nums)):
        if counter_nums[j] > 0:
            for k in range(counter_nums[j]):
                nums[new_num] = j + min_value
                new_num += 1
    return nums
    
    
nums = [2, 5, 3, 0, 2, -2, 3, 0, 3]
print(counter_sort(nums))