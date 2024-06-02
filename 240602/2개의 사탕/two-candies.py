'''
# BFS 사용
1. R,B,O 좌표 변수 선언
2. 상하좌우 기울이며 기울이는 방향에 가까운 캔디부터 이동시키기
3. 이동시킨 결과 queue에 저장
4. R == O and B != O 이면 break
'''

from collections import deque
import copy


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
O = [-1, -1]
R, B = [-1, -1], [-1, -1]
board = []
visit_set = set()

for i in range(n):
    board.append([])
    for j, char in enumerate(input()):
        if char == 'O':
            O = [i, j]
        if char == 'R':
            char = '.'
            R = [i, j]
        elif char == 'B':
            char = '.'
            B = [i, j]
        board[i].append(char)

def drawing(red, blue):
    board[red[0]][red[1]] = 'R'
    board[blue[0]][blue[1]] = 'B'
    for row in board:
        print("".join(row))
    board[red[0]][red[1]] = '.'
    board[blue[0]][blue[1]] = '.'


def move(x, y, PR, PB, direction):
    nx, ny = x, y
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if board[nx][ny] == '#' or [nx, ny] == PR or [nx, ny] == PB: # 벽이거나 다른 사탕과 겹치면
            break
        if [nx, ny] == O: # 도착점이면
            return [nx, ny]
        x, y = nx, ny
    return [x, y]

def lean(direction, nr, nb):
    MR, MB = [0, 0], [0, 0]

    # 기울이는 방향에 가까운 사탕부터 이동 시키기
    firstR = True
    if direction == 0:
        firstR = nr[0] < nb[0]
    elif direction == 1:
        firstR = nr[0] > nb[0]
    elif direction == 2:
        firstR = nr[1] < nb[1]
    elif direction == 3:
        firstR = nr[1] > nb[1]
    
    if firstR:
        MR = move(nr[0], nr[1], nr, nb, direction)
        if MR == O: # 빨간 사탕이 도착했으면 부호반전해서 좌표 벗어나도록
            MR = [-1, -1]
        
        MB = move(nb[0], nb[1], MR, nb, direction)
        if MB == O: # 파란 사탕도 도착하면 경로 폐기
            return None, None
        
    else:
        MB = move(nb[0], nb[1], nr, nb, direction)
        if MB == O: # 파란 사탕 먼저 도착하면 경로 폐기
            return None, None
        MR = move(nr[0], nr[1], nr, MB, direction)
        if MR == O: # 빨간 사탕 도착하면 정답
            return [-1, -1], MB
    
    if MR == nr and MB == nb: # 제자리면 경로 폐기
        return None, None
    
    return MR, MB

queue = deque([])
queue.append([R, B, 1])
result = -1
while queue:
    arrival = False
    nr, nb, cnt = queue.popleft()

    if cnt > 10:
        break

    # 상하좌우 순서로 한번씩 기울여보기
    for i in range(4):
        r, b = lean(i, nr, nb)

        if r == None and b == None: # None이면 pass
            continue
        elif r[0] < 0 and r[1] < 0: # 음수 좌표면 도착
            arrival = True
            break

        # 방문하지 않았던 위치면 다음 탐색 진행
        coord_key = f"{r[0]}{r[1]}{b[0]}{b[1]}"
        if coord_key not in visit_set:
            queue.append([r, b, cnt+1])
            visit_set.add(coord_key)

    if arrival:
        result = cnt
        break

print(result)