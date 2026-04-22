a = []
n = int(input())
for i in range(n):
    a.append(list(map(int, input().split())))
b = [0] * len(a[0])
for i in range(len(a)):
    for j in range(len(a[i])):
        b[j] += a[i][j]
        print(f'{a[i][j]:<3}', end='')
    print(sum(a[i]))
print(*b)