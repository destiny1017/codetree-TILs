'''
필요 함수
1. 4방향 체크 함수
    - 북동남서 방향으로 체크하며 조건 일치시 좌표 리턴
2. 이동 함수
    - 좌표로 이동 후 2로 변경
'''

x, y = map(int, input().split()) # x, y
coord = [int(i) for i in input().split()]
road = []
for i in range(x):
    road.append([int(i) for i in input().split()])

road[coord[0]][coord[1]] = 2 # 시작자리 체크

# 북동남서 이동용 좌표
dx = (-1,0,1,0)
dy = (0,-1,0,1)

def check_road():
    st_direction = coord[2]
    for i in range(4):
        spin_direction = (i + st_direction + 1) % 4 # 좌회전
        nx = coord[0] + dx[spin_direction]
        ny = coord[1] + dy[spin_direction]
        if nx < 0 or nx >= x or ny < 0 or ny >= y:
            continue
        if road[nx][ny] == 1 or road[nx][ny] == 2:
            continue

        if road[nx][ny] == 0:
            coord[2] = spin_direction
            return nx, ny
    return -1, -1

def back_check():
    nx = coord[0] + dx[(coord[2] + 2) % 4]
    ny = coord[1] + dy[(coord[2] + 2) % 4]
    if nx < 0 or nx >= x or ny < 0 or ny >= y:
        return -1, -1
    if road[nx][ny] == 1:
        return -1, -1
    return nx, ny

def move(nx, ny):
    coord[0], coord[1] = nx, ny
    road[nx][ny] = 2

while True:
    # for r in road:
    #     print(r)
    # print()
    nx, ny = check_road()
    if nx >= 0:
        move(nx, ny)
    else:
        bx, by = back_check()
        if bx >= 0:
            move(bx, by)
        else:
            break

cnt = 0
for r in road:
    # print(r)
    for i in r:
        if i == 2:
            cnt += 1

print(cnt)