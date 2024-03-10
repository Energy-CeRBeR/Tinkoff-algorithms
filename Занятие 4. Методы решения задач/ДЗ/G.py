n = int(input())
a = []
cur_position = []
flag = False
for i in range(n):
    t = list(map(int, input().split()))
    t1 = 60 * t[0] + t[1]
    t2 = 60 * t[2] + t[3]
    if t1 < t2:
        a.append([[t1, t2]])
    elif t1 > t2:
        a.append([[t1, 1440], [0, t2]])
        if not flag:
            cur_position = [[t1, 1440], [0, t2]]
            flag = True
a.sort()

if len(a) == 0:
    print(1440)
else:
    if not flag:
        cur_position = a[0]

    temp = [t.copy() for t in cur_position]
    answer = 0
    flag = True
    for i in range(len(a)):
        if a[i] != temp:
            j = 0
            while 0 <= j < len(cur_position):
                for k in range(len(a[i])):
                    if len(cur_position) > 0:
                        if a[i][k][0] > cur_position[j][1] or a[i][k][1] < cur_position[j][0]:
                            cur_position.pop(j)
                            j -= 1
                        else:
                            cur_position[j][0] = max(cur_position[j][0], a[i][k][0])
                            cur_position[j][1] = min(cur_position[j][1], a[i][k][1])
                j += 1

            if len(cur_position) == 0:
                flag = False
                break

    if flag:
        for item in cur_position:
            answer += item[1] - item[0]
    print(answer)
