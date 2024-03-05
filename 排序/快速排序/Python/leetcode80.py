from leetcode_data import nums

def removeDuplicates(nums):
    start, prob, current_duplicates = 0, 1, 1
    while prob < len(nums):
        if nums[prob] != nums[start]:
            current_duplicates = 1
            nums[start + 1] = nums[prob]
            start += 1
        else:
            current_duplicates += 1
            if current_duplicates <= 2:
                nums[start + 1] = nums[prob]
                start += 1        
        prob += 1
    return start + 1

for i in range(0, removeDuplicates(nums)):
    print(nums[i])
        
        
