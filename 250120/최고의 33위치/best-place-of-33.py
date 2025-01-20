n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
result = 0
def calc(n, m):
    sum = 0
    for i in range(n, n+3):
        for j in range(m, m+3):
            if grid[i][j] == 1:
                sum += 1
    return sum

for i in range(n-2):
    for j in range(n-2):
        result = max(result, calc(i, j))

print(result)