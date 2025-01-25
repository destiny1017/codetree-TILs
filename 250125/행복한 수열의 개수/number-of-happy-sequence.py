n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
cnt = 0

for i in range(n):
    prev = 0
    same = 1
    for j in range(n):
        if grid[i][j] == prev:
            same += 1
        else:
            same = 1
        if same >= m:
            cnt += 1
            break
        prev = grid[i][j]

for i in range(n):
    prev = 0
    same = 1
    for j in range(n):
        if grid[j][i] == prev:
            same += 1
        else:
            same = 1
        if same >= m:
            cnt += 1
            break
        prev = grid[j][i]

print(cnt)