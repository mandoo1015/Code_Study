# 조건문과 반복문

### 조건문 (if문)

**기본 구조**
```python
if 조건:
    # 조건이 True일 때 실행
```
⚠️ 주의 : Python은 들여쓰기(indentation)가 문법이다! 보통 스페이스 4칸을 사용한다.

**if-else**
```python
age = 20

if age >= 18:
    print("성인입니다.")
else:
    print("미성년자입니다.")
```

**if - elif - else**
여러 조건을 순차적으로 검사할 때 사용한다.
```python
score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"학점: {grade}")  # 학점: B
```
💡Tip : elif는 위에서부터 순서대로 검사하고, 하나라도 True면 나머지는 검사하지 않는다.

---

### 비교 연산자
- '==' : 같다
- '!=' : 다르다
- '>' : 크다
- '<' : 작다
- '>=' : 크거나 같다
- '<=' : 작거나 같다

⚠️주의 : =는 대입, ==는 비교
```python
x = 5      # 대입: x에 5를 저장
x == 5     # 비교: x가 5와 같은지 확인 → True
```
---

### 논리 연산자
- and : 그리고 -> 둘 다 True여야 True
- or : 또는 -> 하나라도 True면 True
- not : 부정 -> True <-> False
  
```python
age = 25
has_id = True

# and: 둘 다 만족해야 함
if age >= 19 and has_id: ## age >= 19 : True, has_id : True
    print("입장 가능합니다.")

# or: 하나만 만족해도 됨
is_vip = False
is_member = True

if is_vip or is_member: #is_vip : False, is_member : True
    print("할인 적용됩니다.")

# not: 조건 반전
is_banned = False

if not is_banned: #is_banned : False, not is_banned : True
    print("서비스 이용 가능합니다.")
   
"""
출력결과
입장 가능합니다.
할인 적용됩니다.
서비스 이용 가능합니다.
"""
```
**복합조건**
```python
score = 85
attendance = 90

# 성적 80점 이상이고, 출석률 75% 이상이면 통과
if score >= 80 and attendance >= 75:
    print("통과!")

# 괄호로 우선순위 명확하게 하기
if (score >= 90) or (score >= 80 and attendance >= 90):
    print("장학금 대상!")

"""
출력결과
통과!
장학금 대상!
"""
```
**조건문 심화**
```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("운전 가능합니다.")
    else:
        print("면허가 필요합니다.")
else:
    print("성인이 되어야 합니다.")
    
"""
출력결과
운전 가능합니다.
"""
```

💡Tip : 중첩이 깊어지면 가독성이 떨어진다. and로 합치거나 함수로 분리하자.
``` python
# 더 깔끔한 방식
if age >= 18 and has_license:
    print("운전 가능합니다.")
elif age >= 18:
    print("면허가 필요합니다.")
else:
    print("성인이 되어야 합니다.")
```
---

### while 반복문
조건이 True인 동안 계속 반복한다.

**기본 구조**
```python
while 조건:
    # 조건이 True인 동안 반복 실행
```
**예시 : 1부터 5까지 출력**
```python
i = 1

while i <= 5:
    print(i)
    i += 1  # i = i + 1과 동일

# 출력:
# 1
# 2
# 3
# 4
# 5
```
💡i+=1을 빼먹으면 무한 루프에 빠진다!

**예시 : 합계 구하기**
```python
# 1부터 100까지의 합
total = 0
i = 1

while i <= 100:
    total += i
    i += 1

print(f"1부터 100까지의 합: {total}")  # 5050
```
---

### for 반복문
정해진 횟수만큼 또는 컬렉션의 요소만큼 반복한다.

💡for 반복문 설명을 하면서 리스트가 나오는데, 리스트에 대한 자세한 설명은 'Python 리스트'에 기재해 놓았습니다!

**기본 구조**
```python
for 변수 in 반복가능한것:
    # 반복 실행
```

**리스트 순회**
```python
fruits = ['사과', '바나나', '포도']

for fruit in fruits:
    print(fruit)

# 출력:
# 사과
# 바나나
# 포도
```

**range와 함께 사용**
```python
# 0부터 4까지 (5번 반복)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# 1부터 5까지
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# 0부터 10까지, 2씩 증가
for i in range(0, 11, 2):
    print(i)  # 0, 2, 4, 6, 8, 10

# 10부터 1까지 (역순)
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

**문자열 순회**
```python
word = "Python"

for char in word:
    print(char)

# 출력:
# P
# y
# t
# h
# o
# n
```

**딕셔너리 순회**
```python
scores = {'철수': 85, '영희': 92, '민수': 78}

# key만 순회 (기본)
for name in scores:
    print(name)  # 철수, 영희, 민수

# value만 순회
for score in scores.values():
    print(score)  # 85, 92, 78

# key, value 함께 순회
for name, score in scores.items():
    print(f"{name}: {score}점")
```

**enumerate() - 인덱스와 함께**
```python
fruits = ['사과', '바나나', '포도']

for index, fruit in enumerate(fruits):
    print(f"{index}번: {fruit}")

# 출력:
# 0번: 사과
# 1번: 바나나
# 2번: 포도

# 시작 인덱스 지정
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}번: {fruit}")

# 출력:
# 1번: 사과
# 2번: 바나나
# 3번: 포도
```

**zip() - 여러 리스트 동시 순회**
```python
names = ['철수', '영희', '민수']
scores = [85, 92, 78]
grades = ['B', 'A', 'C']

for name, score, grade in zip(names, scores, grades):
    print(f"{name}: {score}점 ({grade})")

# 출력:
# 철수: 85점 (B)
# 영희: 92점 (A)
# 민수: 78점 (C)
```
⚠️ 주의 : 길이가 다르면 가장 짧은 것에 맞춰진다.
```python
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']

for x, y in zip(a, b):
    print(x, y)  # (1, a), (2, b), (3, c) - 3개만 출력
```
---

## 중첩 반복문
반복문 안에 반복문을 넣을 수 있다.
```python
for i in range(2, 10):
    print(f"--- {i}단 ---")
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print()  # 단 사이에 빈 줄
```
### 반복문 제어
**break - 반복 중단**

조건을 만족하면 반복문을 완전히 빠져나온다.
```python
# 1부터 10까지 중 5를 찾으면 중단
for i in range(1, 11):
    if i == 5:
        print("5를 찾았습니다!")
        break
    print(i)

# 출력:
# 1
# 2
# 3
# 4
# 5를 찾았습니다!
```

**continue - 다음 반복으로**

현재 반복을 건너뛰고 다음 반복으로 넘어간다.
```python
# 짝수만 건너뛰기
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)

# 출력:
# 1
# 3
# 5
```
---

**else와 함께 사용**

반복문이 break 없이 정상 종료되면 else 블록이 실행된다.
```
# break로 중단된 경우
for i in range(1, 6):
    if i == 3:
        print("3 발견! 중단합니다.")
        break
else:
    print("모든 반복 완료!")  # 실행 안 됨

# break 없이 정상 종료된 경우
for i in range(1, 6):
    print(i)
else:
    print("모든 반복 완료!")  # 실행됨
```

💡리스트에서 특정 값을 찾을 때 유용하다.
```python
numbers = [1, 3, 5, 7, 9]

for num in numbers:
    if num == 4:
        print("4를 찾았습니다!")
        break
else:
    print("4가 리스트에 없습니다.")  # 이게 출력됨
```

### while vs for 언제 사용할까?
| 상황 | 해결 |
| :--- | :----: |
| 횟수가 정해진 반복 | for |
| 컬렉션 순회 | for |
| 조건 기반 반복 (언제 끝날지 모를 때) | while |
| 무한 루프 필요 | while True (명시적으로 break로 종료) |
| 사용자 입력 대기 | while |

**예 : for가 적합한 경우**
```python
# 리스트의 모든 요소 출력
fruits = ['사과', '바나나', '포도']
for fruit in fruits:
    print(fruit)

# 정해진 횟수만큼 반복
for i in range(10):
    print("안녕하세요!")
```

while이 적합한 경우
```python

# 특정 조건을 만족할 때까지 반복
count = 0
while count < 3:
    answer = input("비밀번호: ")
    if answer == "1234":
        print("로그인 성공!")
        break
    count += 1
    print(f"틀렸습니다. 남은 기회: {3 - count}회")
else:
    print("계정이 잠겼습니다.")
```



