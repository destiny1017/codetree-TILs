n = int(input())
move = [tuple(input().split()) for _ in range(n)]

indicator = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}
x = 0
y = 0
visit_map = {} # {(x,y): [step, min_visit]}
step = 0

for i in range(n):
    direction, distance = move[i]

    for j in range(int(distance)):
        step += 1
        x += indicator[direction][1]
        y -= indicator[direction][0]

        if (x,y) in visit_map:
            min_cnt = step - visit_map[(x,y)][0]
            visit_map[(x,y)][1] = min(visit_map[(x,y)][1], min_cnt)
            visit_map[(x,y)][0] = step
        else:
            visit_map[(x,y)] = [step, 10 * 100]

min_visit = 10 * 100
for x, y in visit_map:
    m_visit = visit_map[(x,y)][1]
    min_visit = min(min_visit, m_visit)
        
print(min_visit if min_visit < 10*100 else -1)