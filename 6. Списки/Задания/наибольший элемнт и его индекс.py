nums = list(map(int, input().split()))
a = 0
b = 0
for i in range(len(nums)):
    if nums[i] > a:
        a = nums[i]
    if nums[i] == a:
        b = i
print(a, b)