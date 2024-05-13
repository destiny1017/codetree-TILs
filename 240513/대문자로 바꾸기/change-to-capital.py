arr = [ input().split() for _ in range(5)]
for row in arr:
    print(" ".join(chr(ord(s) + ord('A') - ord('a')) for s in row))