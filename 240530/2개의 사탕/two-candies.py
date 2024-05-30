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
o = [-1, -1]
board = []

for i in range(n):
    board.append([])
    for j, char in enumerate(input()):
        if char == 'O':
            o = [i, j]
        board[i].append(char)


def move(x, y, direction, tboard):
    nx, ny = x, y
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if tboard[nx][ny] == '#' or tboard[nx][ny] == 'R' or tboard[nx][ny] == 'B':
            break
        x, y = nx, ny
    return [x, y]

def lean(tboard, direction):

    r, b = [0,0], [0,0]
    sti, edi, operi = 0, 0, 0
    stj, edj, operj = 0, 0, 0
    
    if direction == 0:
        sti, edi, operi = 0, n, 1
    elif direction == 1:
        sti, edi, operi = n-1, -1, -1
    elif direction == 2:
        stj, edj, operj = 0, m, 1
    elif direction == 3:
        stj, edj, operj = m-1, -1, -1

    if direction in [0, 1]:
        for i in range(sti, edi, operi):
            for j in range(m):
                if tboard[i][j] == 'R':
                    tboard[i][j] = '.'
                    r = move(i, j, direction, tboard)
                    if r == o:
                        tboard[r[0]][r[1]] = 'O'
                    else:
                        tboard[r[0]][r[1]] = 'R'
                if tboard[i][j] == 'B':
                    tboard[i][j] = '.'
                    b = move(i, j, direction, tboard)
                    tboard[b[0]][b[1]] = 'B'
    elif direction in [2, 3]:
        for j in range(stj, edj, operj):
            for i in range(n):
                if tboard[i][j] == 'R':
                    tboard[i][j] = '.'
                    r = move(i, j, direction, tboard)
                    if r == o:
                        tboard[r[0]][r[1]] = 'O'
                    else:
                        tboard[r[0]][r[1]] = 'R'
                if tboard[i][j] == 'B':
                    tboard[i][j] = '.'
                    b = move(i, j, direction, tboard)
                    tboard[b[0]][b[1]] = 'B'

    return tboard, r, b

queue = deque([])
queue.append((board, 1))
while True:
    arrival = False
    qboard, cnt = queue.popleft()
    for i in range(4):
        # tboard = qboard.copy()
        # for row in qboard:
        #     print(row)
        rboard, r, b = lean(copy.deepcopy(qboard), i)
        # print(f"r={r}, b={b}, o={o}, cnt={cnt}")
        # for row in rboard:
        #     print("".join(row))
        
        if r == o and b != o:
            arrival = True
            break
        elif r == o and b == o:
            break
        queue.append((rboard, cnt+1))

    # if cnt > 3:
    #     print(cnt)
    #     break

    if arrival:
        print(cnt)
        break
    if cnt > 10:
        print(-1)
        break