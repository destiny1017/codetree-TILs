'''
cnt = n // 5
1. if n % 5 == 0 return cnt
2. if n % 5 != 0 while
3. 

'''

n = int(input())

def calc(n):
    cnt = n // 5
    val = n % 5

    if n % 5 == 0:
        return cnt

    while cnt >= 0:
        if val % 3 == 0:
            cnt += val // 3
            return cnt
        val += 5
        cnt -= 1
    return -1

print(calc(n))