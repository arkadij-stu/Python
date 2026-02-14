def is_perfect(n):
    summ = 0
    for i in range(1, n):
        if n % i == 0:
            summ += i
    return summ == n
n = int(input())
count = 0
num = 2
while count != n:
    if is_perfect(num):
        print(num)
        count += 1
    num += 1