num = 243
sum_digits = lambda num: sum(int(x) for x in str(num))
print(sum_digits(num))