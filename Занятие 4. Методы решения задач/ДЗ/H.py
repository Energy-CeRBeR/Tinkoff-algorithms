n, c = map(int, input().split())
times = list()
for i in range(1, n + 1):
    s = input().split()
    start = int(s[0])
    end = start + int(s[1])
    times.append((start, end, i))

times = sorted(times, key=lambda x: x[1])

ans = []
cur_info = times.pop(0)
start = cur_info[0]
end = cur_info[1]
ans.append(cur_info[2])
cur_end = end
while len(times) > 0:
    cur_info = times.pop(0)
    start = cur_info[0]
    end = cur_info[1]
    if start >= cur_end:
        ans.append(cur_info[2])
        cur_end = end

print(len(ans) * c)
print(len(ans))
print(*ans, sep=" ")
