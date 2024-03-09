def bucket_sort(nums):
    if min(nums) < 0:
        bias = -min(nums)
    else:
        bias = 0
    nums = [num + bias for num in nums]
    min_value, max_value = min(nums), max(nums)
    bucket_range = (max_value - min_value) // len(nums) + 1
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

def first_missing_positive(nums):
    sorted_nums = bucket_sort(nums)
    first_positive = -1
    for i in range(len(sorted_nums)):
        if sorted_nums[i] <= 0:
            continue
        else:
            first_positive = i
            break
    if first_positive < 0 or sorted_nums[first_positive] > 1:
        return 1
    for i in range(first_positive, len(sorted_nums) - 1):
        if sorted_nums[i + 1] - sorted_nums[i] > 1:
            return sorted_nums[i] + 1   
    return sorted_nums[len(sorted_nums) - 1] + 1    
        
#nums = [38, -159, -53648, 129, 128, 317, 42537]
#nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 10000, 10000, 9999, 9999, 9998, 9998, 9997, 9997, 9996, 9996]
nums = [-2000000000, 2000000000]
nums = [3, 4, 1, -1]
nums = [7, 8, 9, 11, 12]
nums = [-5]
nums = [1]
print(first_missing_positive(nums))