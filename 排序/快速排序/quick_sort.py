from leetcode_data import nums
import time
import random

def d_calculate_execute_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execute_time = end_time - start_time
        print(f"函数{func.__name__}的执行时间为:{execute_time}秒")
        return result
    return wrapper

def exchange(nums, start, end):
    mid = random.randint(start, end)
   # mid = start + (end - start) // 2 #每次选取中间那个元素为蓝色值
    if nums[start] != nums[mid]:
        nums[start], nums[mid] = nums[mid], nums[start] #交换中间与第一个元素
    
    # 从第2个元素开始循环遍历
    i, green_final_pos, red_first_pos = start + 1, start, start
    while i <= end:
        if nums[i] <= nums[start]: # 绿色元素
            if red_first_pos > start: # 当前绿色的前面已经有红色值了，交换当前绿色和第一个红色的值
                nums[i], nums[red_first_pos] = nums[red_first_pos], nums[i]
                green_final_pos = red_first_pos
                red_first_pos += 1
            else:
                green_final_pos = i
        else: # 红色元素
            if red_first_pos == start: # 第一个红色元素
                red_first_pos = i
        i += 1
    if nums[start] != nums[green_final_pos]:
        nums[start], nums[green_final_pos] = nums[green_final_pos], nums[start]
    return green_final_pos

def quick_sort_recursion(nums, start, end):
    if end - start > 0: # 递归的结束条件是数组只有一个元素
        mid = exchange(nums, start, end)
        quick_sort_recursion(nums, start, mid - 1)
        quick_sort_recursion(nums, mid + 1, end)

@d_calculate_execute_time
def quick_sort(nums):
    quick_sort_recursion(nums, 0, len(nums) - 1)
    return nums
nums = [4, -1, 5, -1, 9, 6, 7, 7, 3, 2, 1]

print(exchange(nums, 0, len(nums) - 1))

quick_sort(nums)
print(nums)
