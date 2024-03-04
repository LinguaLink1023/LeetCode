
def delete_same_element(nums):
    start, prob = 0, 1
    while prob < len(nums):
        if nums[prob] != nums[start]:
            start += 1
            nums[start] = nums[prob]
        prob += 1
    return start + 1

nums = [0,0,1,1,1,2,2,3,3,4]
print(delete_same_element(nums))