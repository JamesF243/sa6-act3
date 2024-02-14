nums = [1, 2, 3, 4, 5, 6]
num2 = [6, 7, 8, 9, 10]
intersection = list(filter(lambda x: x in num2, nums))
print(intersection)