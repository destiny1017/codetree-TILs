import sys

input = sys.stdin.readline

n = int(input())
bombs = [int(input()) for _ in range(n)]

def boom_left(start, step, total_cnt, bombs):
    boom_range = start - step
    cnt = 0
    
    # 폭발 범위까지 폭발 반복
    while bombs:
        next_bomb = bombs.pop()
        if next_bomb < boom_range:
            bombs.append(next_bomb)
            break
        cnt += 1

    # 마지막 터진 폭탄이 있으면 범위 늘려서 재귀호출
    if cnt > 0:
        return boom_left(next_bomb, step+1, total_cnt + cnt, bombs)
    else:
        return total_cnt

def boom_right(start, step, total_cnt, bombs):
    boom_range = start + step
    next_bomb = 0
    cnt = 0
    
    # 폭발 범위까지 폭발 반복
    while bombs:
        if bombs[-1] > boom_range:
            break
        next_bomb = bombs.pop()
        cnt += 1
    # print(start, step, cnt)
    # 마지막 터진 폭탄이 있으면 범위 늘려서 재귀호출
    if cnt > 0:
        return boom_right(next_bomb, step+1, total_cnt + cnt, bombs)
    else:
        return total_cnt

bombs.sort()
max_cnt = 0

for i in range(len(bombs)):
    bomb = bombs[i]
    # cnt = boom_left(bomb, 1, 0, bombs[:i]) + boom_right(bomb, 1, 0, bombs[i:])
    left_cnt = boom_left(bomb, 1, 0, bombs[:i])
    right_cnt = boom_right(bomb, 1, 0, sorted(bombs[i+1:], reverse=True))
    # print(f"bomb = {bomb}, left_cnt={left_cnt}, right_cnt={right_cnt}")
    max_cnt = max(max_cnt, left_cnt + right_cnt + 1)

print(max_cnt)