import sys

'''
1. 저점매수 고점매도 반복
2. 저점지점과 고점지점 파악하여 최대한 빈번한 매도 수행
3. 다음 가격이 떨어지면 전체 매도, 올라가면 전체 매수
'''

n, w = map(int, input().split())

price = [int(input()) for _ in range(n)]

amount = 0
last_buy = 0
buy_flag = False

for i in range(n-1):
    today, tomorrow = price[i], price[i+1]
    if tomorrow > today: # 내일이 더 크면 매수
        if buy_flag:
            continue
        amount = w // today
        w %= today
        last_buy = today
        buy_flag = True
    else: # 내일이 더 작으면 매도
        w += today * amount
        amount = 0
        buy_flag = False

# 들고 있는 주식이 있고 마지막날 가격이 마지막 전날보다 크면 매도
if amount > 0 and price[-1] > price[-2]:
    w += price[-1] * amount
else: # 마지막날 가격이 떨어지면 마지막 매수 시점가격으로 복귀
    w += last_buy * amount

print(w)