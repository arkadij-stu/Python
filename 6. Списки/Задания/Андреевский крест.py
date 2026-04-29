n = int(input())
matrix = [[1 if i == j or i + j == n - 1 else 0 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()