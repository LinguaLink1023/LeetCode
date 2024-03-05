from leetcode_data import nums
import time
import random
from calculate_execute_time import d_calculate_execute_time



def partition(nums, start, end):
    # mid = start + (end - start) // 2
    # pivot = sorted([nums[start], nums[mid], nums[end]])[1]
    # #或者
    mid = random.randint(start, end)
    pivot = nums[mid]
    minimum = start
    while start <= end:
        while start <= end and nums[start] > pivot:
            nums[start], nums[end] = nums[end], nums[start]
            end -= 1
        while start <= end and nums[start] == pivot:
            start += 1
        while start <= end and nums[start] < pivot:
            nums[start], nums[minimum] = nums[minimum], nums[start]
            start, minimum = start + 1, minimum + 1
    return minimum - 1, end + 1

def quick_sort_recursion(nums, start, end):
    if end > start:
        left, right = partition(nums, start, end)
        quick_sort_recursion(nums, start, left)
        quick_sort_recursion(nums, right, end)      


@d_calculate_execute_time
def quick_sort(nums):
    nums = sorted(nums)
    quick_sort_recursion(nums, 0, len(nums) - 1)
    return nums

quick_sort(nums)

# nums = [5, 2, 3, 1]
# print(quick_sort(nums))