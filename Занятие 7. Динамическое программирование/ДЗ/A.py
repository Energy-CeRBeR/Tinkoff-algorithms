n = int(input())
coasts = list(map(int, input().split()))
ans = 0
cur_position = 0
while cur_position <= n - 1:
    coast_1 = coasts[cur_position]
    if cur_position + 1 <= n - 1:
        coast_2 = coasts[cur_position + 1]
        if coast_1 < coast_2:
            ans += coast_1
            cur_position += 1
        else:
            ans += coast_2
            cur_position += 2
    else:
        ans += coast_1
        cur_position += 1

print(ans)

'''
6
1 2 2 3 5 1
Выводит 7, можно сделать 6
'''
