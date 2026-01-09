import datetime

today = datetime.datetime.now()
pi_day = datetime.datetime(2025, 3, 14, 13, 6, 15)
print(today - pi_day)
print(type(today - pi_day))  # timedelta 타입(날짜 간의 차이를 나타내는 타입)

# timedelta를 생성
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)

print(today)
print(today + my_timedelta) # 현재 시간에 5일 3시간 10분 50초 더하기