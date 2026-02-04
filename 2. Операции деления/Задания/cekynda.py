a = int(input())
b = a // 60
cek = a % 60
hour = b // 60
min = b % 60
print(f'{hour}:{min}:{cek}')