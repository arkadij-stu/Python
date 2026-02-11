def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


target_count = int(input())
count = 0
num = 2
while count != target_count:
    if is_prime(num):
        print(num)
        count += 1
    num = num + 1