# Python 기본

### 주석(Comment)
코드에 설명을 달고 싶을 때 사용한다. 실행에는 영향을 주지 않는다.
```python
# 한 줄 주석은 # 으로 시작

"""
여러 줄 주석은
큰따옴표 3개로 감싸면 된다
"""
```
💡Tip : 주석은 "왜 이렇게 했는지"를 적는 게 좋다. "무엇을 했는지"는 코드를 보면 알 수 있으니까!

---

### 자료형(Data Type)
숫자 vs 문자
겉보기엔 같아 보여도 자료형이 다르면 완전히 다르게 작동한다.

```python
# 숫자형
print(2 + 3)      # 5 (덧셈)

# 문자형 (따옴표로 감싸면 문자)
print('2' + '3')  # 23 (문자열 연결)
```
**자료형 확인하기**

```python
print(type(2))      # <class 'int'>
print(type('2'))    # <class 'str'>
print(type(3.14))   # <class 'float'>
print(type(True))   # <class 'bool'>
```

**자료형 변환**
```python
# 문자 → 숫자
num = int('123')    # 123 (정수)
num = float('3.14') # 3.14 (실수)

# 숫자 → 문자
text = str(123)     # '123'
```
---

### 숫자 연산
기본 연산자
- '+' : 덧셈
- '-' : 뺄셈
- ' * ' : 곱셈
- '/' : 나눗셈
- '//' : 버림 나눗셈 (7//2 = 3)
- '%' : 나머지 (7 % 2 = 1)
- ' ** ' : 거듭제곱

⚠️ 나눗셈 주의사항
Python에서 / 연산은 항상 실수형(float)으로 결과가 나온다!
```python
print(6 / 2)    # 3.0 (정수끼리 나눠도 실수!)
print(7 / 2)    # 3.5
print(7 // 2)   # 3 (버림 나눗셈 = 정수 결과)
```
버림 나눗셈도(//)도 실수가 끼면 실수로 나온다.
```python
print(7.0 // 2)   # 3.0 (실수형 결과)
print(7 // 2.0)   # 3.0
```

**반올림(round)**
```python
print(round(3.141592))       # 3 (소수점 첫째자리에서 반올림)
print(round(3.141592, 2))    # 3.14 (소수점 셋째자리에서 반올림)
```
---

### 문자열 (String)
**따옴표 사용법**
```python
# 기본
print('Hello')
print("Hello")

# 문자열 안에 따옴표를 넣고 싶을 때
print("I'm excited")          # 바깥을 ""로 감싸기
print('He said "Hello"')      # 바깥을 ''로 감싸기

# 둘 다 넣고 싶을 때 → 이스케이프 문자 사용
print('I\'m "excited"')       # I'm "excited"
print("I\'m \"excited\"")     # I'm "excited"

"""
이스케이프 문자
\' : 작은따옴표
\" : 큰따옴표
\\ : 역슬래시
\n : 줄바꿈
\t : 탭
"""
```

**f-string (포맷 문자열) ⭐**
python 3.6부터 사용 가능한 가장 편한 방식!
```python
name = "김철수"
age = 25

# 기존 방식 (불편)
print("이름: " + name + ", 나이: " + str(age))

# f-string (편리!)
print(f"이름: {name}, 나이: {age}")
```

**계산도 가능:**
```python
num1 = 1
num2 = 3
print(f"{num1} 나누기 {num2}은 {num1/num2}입니다.")
# 1 나누기 3은 0.3333333333333333입니다.
```
**소수점 자리수 지정:**
```python
print(f"{num1} 나누기 {num2}은 {num1/num2:.2f}입니다.")
# 1 나누기 3은 0.33입니다.

"""
:.2f -> 소수점 2자리
:.0f -> 소수점 없음
:, -> 천 단위 콤마
:>10 -> 오른쪽 정렬 (10칸)
"""
```
---

### 함수 (Function)
**기본 구조**
```python
def 함수이름(파라미터1, 파라미터2):
    # 실행할 코드
    return 반환값
```
**예시**
```python
def greet(name):
    return f"안녕하세요, {name}님!"

message = greet("철수")
print(message)  # 안녕하세요, 철수님!
```
**파라미터 vs 인자(Argument)**
``` python
def add(a, b):    # a, b는 파라미터 (매개변수)
    return a + b

result = add(3, 5)  # 3, 5는 인자 (전달인자)
```

**기본값 설정**
```python
def greet(name, greeting="안녕하세요"):
    return f"{greeting}, {name}님!"

print(greet("철수"))              # 안녕하세요, 철수님!
print(greet("철수", "반갑습니다"))  # 반갑습니다, 철수님!
```

