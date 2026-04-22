nums = list(map(int, input().split()))
max = 0
min = 0
for i in range(len(nums)):
    if nums[max] < nums[i]:
        max = i
    if nums[min] > nums[i]:
        min = i
nums[max], nums[min] = nums[min], nums[max]
print(*nums)