import sys
n = int(sys.stdin.readline())

lines = list(int(sys.stdin.readline()) for _ in range(n))
lines.sort()

max_w = lines[0] * n

for i in range(1, n):
    if lines[i] == lines[i-1]:
        continue
    
    max_w = max(max_w, lines[i] * (n-i))

print(max_w)