import sys

input = sys.stdin.readline

n = int(input())
bombs = [int(input()) for _ in range(n)]

def boom(start, step, total_cnt, direction, bombs):
    boom_range = start - step if direction == 'LEFT' else start + step
    next_bomb = 0
    cnt = 0
    
    # 폭발 범위까지 폭발 반복
    while bombs:
        if direction == 'LEFT' and bombs[-1] < boom_range:
            break
        elif direction == 'RIGHT' and bombs[-1] > boom_range:
            break
        next_bomb = bombs.pop()
        cnt += 1

    # 마지막 터진 폭탄이 있으면 범위 늘려서 재귀호출
    if cnt > 0:
        return boom(next_bomb, step+1, total_cnt + cnt, direction, bombs)
    else:
        return total_cnt

bombs.sort()
max_cnt = 0

for i in range(len(bombs)):
    bomb = bombs[i]
    left_cnt = boom(bomb, 1, 0, 'LEFT', bombs[:i])
    right_cnt = boom(bomb, 1, 0, 'RIGHT', sorted(bombs[i+1:], reverse=True))
    max_cnt = max(max_cnt, left_cnt + right_cnt + 1)

print(max_cnt)