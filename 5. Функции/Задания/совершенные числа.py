def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


p = 2
target_count = int(input())
count = 0
num = 2^p - 1
while count != target_count:
    if is_prime(num):
        print(2**(p-1)*(2**p-1))
        count += 1
    p += 1