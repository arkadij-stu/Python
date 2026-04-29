n = int(input())
matrix = [[0 if i == j or i + j == n - 1 else 1 if i > j and i + j < n - 1 else 2 if i > j and i + j >= n - 1 else 3 if i < j and i + j > n - 1 else 4 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()