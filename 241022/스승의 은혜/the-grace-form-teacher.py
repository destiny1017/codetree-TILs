n, b = map(int, input().split())
costs = []
cnt = 0
discount = False

for i in range(n):
    product, ship = map(int, input().split())
    costs.append((product, ship))

costs.sort()
for cost in costs:
    total = cost[0] + cost[1]
    if b >= total:
        b -= total
        cnt += 1
    else:
        if not discount:
            total = cost[0] // 2 + cost[1]
            if b >= total:
                b -= total
                cnt += 1
                discount = True
        break

print(cnt)