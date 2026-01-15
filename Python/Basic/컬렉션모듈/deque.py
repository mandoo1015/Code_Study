from collections import deque

# 가상 로그 데이터: (사용자ID, 방문페이지)
logs = [
    ("user_A", "home"), ("user_B", "shop"), ("user_A", "login"),
    ("user_C", "home"), ("user_A", "shop"), ("user_B", "home"),
    ("user_A", "logout"), ("user_C", "shop"), ("user_C", "pay")
]

# deque : 양방향 삽입/삭제, maxlen 지원
# 최대 3개의 최근 활동만 저장하는 큐
recent_history = deque(maxlen=3)

for _, page in logs:
    recent_history.append(page)

print(f"최근 방문한 페이지 3개: {recent_history}")
# 출력: deque(['logout', 'shop', 'pay'], maxlen=3)
