import sys
n = int(sys.stdin.readline())
lines = [int(sys.stdin.readline()) for _ in range(n)]
lines.sort()
prev = 0

for i in range(len(lines)):

    if lines[i] == lines[i-1]:
        continue

    now = lines[i] * (n-i)
    
    if now < prev:
        break

    prev = now
 

print(prev)