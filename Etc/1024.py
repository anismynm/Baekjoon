import sys
input = sys.stdin.readline

n, l = map(int, input().split())

while True:
    if l > 100:
        print(-1)
        break
    mid = n / l
    if l % 2 == 0 and mid - 0.5 == int(mid) and mid * l == n: # 길이가 짝수, 중간 값 ~~.5 형태, 합이 답 만족
        if int(mid) - (l // 2 - 1) < 0: # 답의 범위가 음수가 되지 않는지
            print(-1)
            break
        for i in range(int(mid) - (l // 2 - 1), int(mid) + (l // 2 + 1)):
            print(i, end = ' ')
        print()
        break
    elif l % 2 != 0 and mid == int(mid) and mid * l == n: # 길이가 홀수, 중간 값 정수, 합이 답 만족
        if int(mid) - (l // 2) < 0: # 답의 범위가 음수가 되지 않는지
            print(-1)
            break
        for i in range(int(mid) - (l // 2), int(mid) + (l // 2) + 1):
            print(i, end = ' ')
        print()
        break
    l += 1