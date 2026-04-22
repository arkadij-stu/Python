nums = list(map(int, input().split()))
k = int(input())
k %= len(nums)
a = nums[-k:] + nums[:-k]
print(*a)