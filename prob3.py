def find_max(list_nums, greater_function):
    max = -1000
    for i in list_nums:
        if greater_function(i, max):
            max = i
    return max


nums = [1, 2, 3, 4, 5]
print(find_max(nums, lambda x, y: x if x >= y else y))