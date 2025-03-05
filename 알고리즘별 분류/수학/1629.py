A, B, C = map(int, input().split())

def solution(A, B, C):
    if B == 1:
        return A % C
    else:
        num = solution(A, B // 2, C)
        if B % 2 == 0:
            return num * num % C
        else:
            return num * num * A % C

print(solution(A, B, C))