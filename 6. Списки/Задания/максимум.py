n, m = list(map(int, input().split()))
l = []
maxi = 0
maxj = 0
for i in range(n):
    l.append(list(map(int, input().split())))
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[maxi][maxj] < l[i][j]:
            maxj = j
            maxi = i
print(maxi, maxj)