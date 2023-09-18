current_hour, current_min = map(int, input().split())
plus_time = int(input())

plus_hour = plus_time // 60
plus_min = plus_time % 60

if current_min + plus_min >= 60:
    min_result = (current_min + plus_min) % 60
    carry_hour = (current_min + plus_min) // 60
else:
    min_result = current_min + plus_min
    carry_hour = 0

if current_hour + plus_hour + carry_hour >=24:
    hour_result = (current_hour + plus_hour + carry_hour) % 24
else: 
    hour_result = current_hour + plus_hour + carry_hour

print(hour_result, min_result)