n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words_map = {}
words = [""]
for i in range(1, n+1):
    word = input()
    words.append(word)
    words_map[word] = i

queries = [input() for _ in range(m)]

# Write your code here!
for q in queries:
    if q.isdigit():
        print(words[int(q)])
    else:
        print(words_map[q])