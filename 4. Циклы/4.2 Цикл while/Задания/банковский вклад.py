start_sum = int(input())
count = 1
target_sum = int(input())
percent = int(input())
mounth_percent = percent / 1200
while start_sum <= target_sum:
    start_sum = start_sum * mounth_percent + start_sum
    print(f'{count} - {start_sum:.2f}')
    count += 1