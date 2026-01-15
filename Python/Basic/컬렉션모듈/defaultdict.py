from collections import defaultdict

# 가상 로그 데이터: (사용자ID, 방문페이지)
logs = [
    ("user_A", "home"), ("user_B", "shop"), ("user_A", "login"),
    ("user_C", "home"), ("user_A", "shop"), ("user_B", "home"),
    ("user_A", "logout"), ("user_C", "shop"), ("user_C", "pay")
]

# defaultdict : 존재하지 않는 키 접근 시 기본값 자동 생성
# 리스트를 기본값으로 가지는 defaultdict 생성
user_pages = defaultdict(list)

for user, page in logs:
    user_pages[user].append(page)

print("사용자별 방문 기록:")
for user, history in user_pages.items():
    print(f"{user}: {history}")
# 출력: user_A: ['home', 'login', 'shop', 'logout'] ...
