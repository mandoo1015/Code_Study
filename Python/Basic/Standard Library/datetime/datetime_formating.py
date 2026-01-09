import datetime

# datetime 포매팅
today = datetime.datetime.now()

print(today)
print(today.strftime("%A, %B %dth %Y"))