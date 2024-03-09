
# def partition(s, record, start ,end):
#     mid = start + (end - start) // 2
#     pivot = s[mid]
#     less = start
    
#     while start <= end:
#         while start <= end and s[start] > pivot:
#             s[start], s[end] = s[end], s[start]
#             end -= 1
#         while start <= end and s[start] == pivot:
#             start += 1
#         while start <= end and s[start] < pivot:
#             s[start], s[less] = s[less], s[start]
#             less += 1
#             start += 1
#     record[pivot] = len(s) - less - (len(s) - 1 - end)
#     return less - 1, end + 1

# def quick_sort_recursion(s, record, start ,end):
#     if end > start:
#         left_end, right_start = partition(s, record, start, end)
#         quick_sort_recursion(s, record, start, left_end)
#         quick_sort_recursion(s, record, right_start, end)
#     elif end == start:
#         record[s[start]] = 1
        
# def frequencySort(s):
#     index = 0
#     record = dict()
#     nums_s = list(s)
#     quick_sort_recursion(nums_s, record, 0, len(nums_s) - 1)
#     sorted_record = sorted(record.items(), key=lambda x: x[1], reverse=True)
#     for item in sorted_record:
#         for i in range(0, item[1]):
#             nums_s[index] = item[0]
#             index += 1
#     return ''.join(nums_s)


def partition(s, start ,end):
    mid = start + (end - start) // 2
    pivot = s[mid][1]
    less = start
    
    while start <= end:
        while start <= end and s[start][1] > pivot:
            s[start], s[less] = s[less], s[start]
            less += 1
            start += 1            
        while start <= end and s[start][1] == pivot:
            start += 1
        while start <= end and s[start][1] < pivot:
            s[start], s[end] = s[end], s[start]
            end -= 1
    return less - 1, end + 1

def quick_sort_recursion(s, start, end):
    if end > start:
        left_end, right_start = partition(s, start, end)
        quick_sort_recursion(s, start, left_end)
        quick_sort_recursion(s, right_start, end)

def frequencySort(s):
    from collections import Counter
    counts_dict = Counter(s) #统计每个元素出现的次数
    counts_list = list(counts_dict.items()) #把字典变成列表，每个元素都是一个包含2个元素的列表
    quick_sort_recursion(counts_list, 0, len(counts_list) - 1) #对列表排序，按照出现的次数，从高到低排序
    # 列表推导式的语法，遍历counts_list,然后依次生成元素pair[0],给pair[0]重复pair[1]次
    return ''.join(pair[0]*pair[1] for pair in counts_list)
    # nums_s = list()
    # for element in counts_list:
    #     for i in range(element[1]):
    #         nums_s.append(element[0])
    # return "".join(nums_s)


    
s = "traaghhyyuuuwerrrtgvghjjrwwow"
#s = "tree"
#s = "Aabb"
print(frequencySort(s))
    