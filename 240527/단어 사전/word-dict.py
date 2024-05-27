import sys

word_set = set([s for s in sys.stdin.readline().split()])
print(" ".join(sorted(list(word_set))))