n, b = map(int, input().split())
costs = []
cnt = 0

for i in range(n):
    product, ship = map(int, input().split())
    costs.append((product, ship))

costs.sort(key=lambda x: x[0] + x[1])
i = 0
for i in range(len(costs)):
    cost = costs[i]
    total = cost[0] + cost[1]
    if b >= total:
        b -= total
        cnt += 1
    else:
        if cost[0] // 2 + cost[1] <= b:
            cnt += 1
            break


print(cnt)