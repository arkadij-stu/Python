a = int(input())
b = a % 10
c = a % 100
if 11 <= c <= 14:
    print('грибов')
elif a % 10 == 1:
    print('гриб')
elif 2 <= b <= 4:
    print('гриба')
else:
    print('грибов')