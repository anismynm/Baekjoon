N = int(input())
length = list(map(int, input().split()))
gas_price = list(map(int, input().split()))

cost = 0
now = 0
while now < len(gas_price): # 4
    found = False
    for i in range(now + 1, len(gas_price)):
        if gas_price[i] < gas_price[now]:
            cost += gas_price[now] * sum(length[now:i])
            now = i
            found = True
            break
    if not found:
        cost += gas_price[now] * sum(length[now::])
        now = len(gas_price)

print(cost)