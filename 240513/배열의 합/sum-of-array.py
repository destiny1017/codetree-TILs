arr = [list(map(int, input().split())) for line in range(4)]
for row in arr:
    print(sum(row))