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
nr, nb = [-1, -1], [-1, -1]
board = []

for i in range(n):
    board.append([])
    for j, char in enumerate(input()):
        if char == 'O':
            o = [i, j]
        if char == 'R':
            char = '.'
            nr = [i, j]
        elif char == 'B':
            char = '.'
            nb = [i, j]
        board[i].append(char)


def move(x, y, nr, nb, direction):
    nx, ny = x, y
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if board[nx][ny] == '#' or [nx, ny] == nr or [nx, ny] == nb:
            break
        x, y = nx, ny
    return [x, y]

def lean(direction, nr, nb):

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
                if i == nr[0] and j == nr[1]:
                    r = move(i, j, nr, nb, direction)
                if i == nb[0] and j == nb[1]:
                    if r == o:
                        b = move(i, j, [0,0], nb, direction)
                    else:
                        b = move(i, j, nr, nb, direction)
    elif direction in [2, 3]:
        for j in range(stj, edj, operj):
            for i in range(n):
                if i == nr[0] and j == nr[1]:
                    r = move(i, j, nr, nb, direction)
                if i == nb[0] and j == nb[1]:
                    if r == o:
                        b = move(i, j, [0,0], nb, direction)
                    else:
                        b = move(i, j, nr, nb, direction)

    return r, b

queue = deque([])
queue.append((nr, nb, 1))
while queue:
    arrival = False
    nr, nb, cnt = queue.popleft()
    # board[nr[0]][nr[1]] = 'R'
    # board[nb[0]][nb[1]] = 'B'
    # print("##### start")
    # for row in board:
    #     print("".join(row))
    
    # board[nr[0]][nr[1]] = '.'
    # board[nb[0]][nb[1]] = '.'
    for i in range(4):
        r, b = lean(i, nr, nb)
        # print(f"r={r}, b={b}, o={o}, i={i}, cnt={cnt}")

        # board[r[0]][r[1]] = 'R'
        # board[b[0]][b[1]] = 'B'
        # for row in board:
        #     print("".join(row))
        
        # board[r[0]][r[1]] = '.'
        # board[b[0]][b[1]] = '.'
        
        if r == o and b != o:
            arrival = True
            break
        elif r == o and b == o:
            continue
        elif r == nr and b == nb:
            continue
        queue.append((r, b, cnt+1))
        # print("add")

    # if cnt > 3:
    #     print(cnt)
    #     break

    if arrival:
        print(cnt)
        break
    if cnt > 10:
        print(-1)
        break