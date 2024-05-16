from itertools import combinations

n = int(input())
arr = [list(map(int, input())) for i in range(n)]

mlen = len(max(arr, key= lambda x: len(x)))

for i, num in enumerate(arr):
    arr[i] = ([0] * (mlen - len(num))) + num


result = False

for i in range(n, 0, -1):
    for comb in combinations(arr, i):
        carry = False
        total_arr = []
        for j in range(mlen):
            total = sum([x[j] for x in comb])
            total_arr.append(total)
        
        for num in total_arr:
            if num >= 10:
                carry = True
                break

        if not carry:
            print(i)
            result = True
            break
    if result:
        break