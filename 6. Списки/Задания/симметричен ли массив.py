def is_symmetric(a):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[j][i] != a[i][j]:
                return False
    return True

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
if is_symmetric(a):
    print('YES')
else:
    print('NO')
