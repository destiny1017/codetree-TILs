import sys
import math

n = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().split()))
leader, member = map(int, sys.stdin.readline().split())
val = 0

for p in people:
    p -= leader
    val += 1
    if p > 0:
        val += math.ceil(p / member)

print(val)