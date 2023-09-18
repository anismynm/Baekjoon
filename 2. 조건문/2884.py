h, m = map(int, input().split())
if h != 0:
    if m >= 0 and m <= 44:
        h = h - 1
        m = m + 15
    elif m >= 45 and m <= 59:
        m = m - 45
elif h == 0:
    if m >= 0 and m <= 44:
        h = h + 23
        m = m + 15
    elif m >= 45 and m <= 59:
        m = m - 45
    
print(h, m)