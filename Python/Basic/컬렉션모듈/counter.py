from collections import Counter

# 가상 로그 데이터: (사용자ID, 방문페이지)
logs = [
    ("user_A", "home"), ("user_B", "shop"), ("user_A", "login"),
    ("user_C", "home"), ("user_A", "shop"), ("user_B", "home"),
    ("user_A", "logout"), ("user_C", "shop"), ("user_C", "pay")
]

# Counter : 요소의 개수를 딕셔너리 형태로 반환
# 모든 방문 페이지 추출
all_pages = [page for _, page in logs]

# 카운터 객체 생성
page_counts = Counter(all_pages)

print("전체 페이지 방문 횟수:", page_counts)
# 가장 많이 방문된 상위 2개 페이지
print("인기 페이지 Top 2:", page_counts.most_common(2))
# 출력: [('shop', 3), ('home', 3)]

