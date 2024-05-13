arr = [ input().split() for _ in range(5)]
for row in arr:
    print(" ".join(s.upper() for s in row))