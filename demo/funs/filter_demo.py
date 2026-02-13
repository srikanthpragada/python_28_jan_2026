def ispositive(n):
    return n > 0


nums = [1, -20, -5, 50, -30, 4]

for v in filter(ispositive, nums):
    print(v)
