import sys
input = sys.stdin.readline

N = int(input())
heart_x = heart_y = back = left_arm = right_arm = left_leg = right_leg = now = 0

i = 2
while True:
    now += 1
    tmp = input().rstrip()
    if '*' in tmp:
        heart_x = i
        heart_y = tmp.index('*') + 1
        break
    i += 1

now += 1
tmp = input().rstrip()
left_arm = heart_y - 1 - tmp.index("*")
right_arm = tmp.count("*") - 1 - left_arm
    
while True:
    now += 1
    if now > N: break
    tmp = input().rstrip()
    if tmp.count("*") == 2:
        left_leg += 1
        right_leg += 1
    elif tmp.count("*") == 1:
        if left_leg == 0 and right_leg == 0:
            back += 1
        else:
            if tmp.index('*') == heart_y:
                right_leg += 1
            else:
                left_leg += 1
    else:
        break

print(f"{heart_x} {heart_y}\n{left_arm} {right_arm} {back} {left_leg} {right_leg}")