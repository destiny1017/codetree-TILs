import sys

input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))


max_cnt = 1

for num in arr:
    tmp = arr.copy()
    for i in range(len(tmp)):
        if tmp[i] == num:
            tmp[i] = -1

    repeat_cnt = 1
    jump_cnt = 1
    for i in range(1, len(tmp)):
        if tmp[i] == -1:
            jump_cnt += 1
            continue

        if tmp[i] == tmp[i-jump_cnt]:
            repeat_cnt += 1
        else:
            max_cnt = max(repeat_cnt, max_cnt)
            repeat_cnt = 1

        jump_cnt = 1

print(max_cnt)