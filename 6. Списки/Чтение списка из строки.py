# I способ (с помощью функции map)
nums1 = list(map(int, input().split()))
# input().split() -
# map()
# list()

# II способ (с помощью генераторов)
nums2 = [int(i) for i in input().split()]

print(nums1)
print(nums2)