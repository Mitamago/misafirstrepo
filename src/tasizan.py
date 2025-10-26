total = 0
start_hour = 12
start_minute = 25

for i in range(1, 51):
    total += i
    if i == 1:
        print(f"{i}")
    else:
        # 1225を12時25分として、そこから累計分を加算
        total_minutes = start_minute + total
        new_hour = start_hour + total_minutes // 60
        new_minute = total_minutes % 60
        # 24時間制で表示
        display_hour = new_hour % 24
        print(f"{total - i}の{i}分後は、{display_hour:02d}時{new_minute:02d}分です！")
