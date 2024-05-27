import sys
n = int(sys.stdin.readline())
lines = [int(sys.stdin.readline()) for _ in range(n)]
lines.sort()
prev = 0
for line in lines:
    now = line * n
    if now < prev:
        break
    prev = now
    n -= 1

print(prev)