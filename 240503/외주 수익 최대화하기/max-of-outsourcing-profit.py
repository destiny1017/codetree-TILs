import sys

n = int(sys.stdin.readline())
jobs = []
result = 0

for i in range(n):
    jobs.append(tuple(map(int, sys.stdin.readline().split())))

dp = [0] * (n)

for i in range(n):
    dp[i] = dp[i-1]
    for j in range(i+1):
        if j + jobs[j][0] - 1 == i:
            dp[i] = max(dp[i], dp[i - jobs[j][0]] + jobs[j][1])

print(max(dp))