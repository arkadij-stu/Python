nums = list(map(int, input().split()))
a = int(input())
for i in range(1, len(nums)):
    if nums[i] <= a:
        print(i)
