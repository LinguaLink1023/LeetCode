
def partition(nums, left, right):
    # 因为只有0，1,2 这三个元素
    pivot = 1
    
    less = left
    while left <= right:
        while left <= right and nums[left] > pivot:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
        while left <= right and nums[left] == pivot:
            left += 1
        while left <= right and nums[left] < pivot:
            nums[left], nums[less] = nums[less], nums[left]
            less += 1
            left += 1
    return less - 1, right + 1

# def quick_sort_recursion(nums, left, right):
#     if right > left:
#         left_end, right_start = partition(nums, left, right)
#         quick_sort_recursion(nums, left, left_end)
#         quick_sort_recursion(nums, right_start, right)
        
def quick_sort(nums):
    partition(nums, 0, len(nums) - 1)
    return nums

nums = [2, 0, 2, 1, 1, 0]
print(quick_sort(nums))

