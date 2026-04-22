def is_palindrome(n):
    new = 0
    was = n
    while n != 0:
        a = n % 10
        n = n // 10
        new = (new * 10) + a
    if was == new:
        return True
    return False

a = int(input())
b = int(input())
for i in range(a, b):
    if is_palindrome(i):
        print(i, end=' ')
