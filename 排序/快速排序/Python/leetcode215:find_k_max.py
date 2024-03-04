import random


def partition(nums, left, right):
    mid = left + (right - left) // 2
    pivot = sorted([nums[left], nums[mid], nums[right]])[1]
    
    while left <= right:
        while nums[left] < pivot:
            left += 1
        while nums[right] > pivot:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
    return left

def select_recursion(nums, left, right, k_largest):
    if left == right:  # If the list contains only one element,
        return nums[left]  # return that element
    # find the pivot position in a sorted list
    pivot_index = partition(nums, left, right)
    # the pivot is in its final sorted position
    if len(nums) - pivot_index >= k_largest:
        return select_recursion(nums, pivot_index, right, k_largest)
    else:
        return select_recursion(nums, left, pivot_index-1, k_largest)


def findKthLargest(nums, k):
    return select_recursion(nums, 0, len(nums)-1, k)
    

nums = [3,2,3,1,2,4,5,5,6]
#nums = [3, 2, 1, 5, 6, 4]
print(findKthLargest(nums, 1))