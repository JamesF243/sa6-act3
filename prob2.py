example = ["ddd", "ccc", "bb", "a"]
sorted_list = sorted(example ,key=lambda x: (len(x), x))
print(sorted_list)