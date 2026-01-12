# 리스트

**기본 사용법**
```python
numbers = [2, 3, 5, 7, 11, 13]
fruits = ["사과", "바나나", "포도"]
mixed = [1, "hello", 3.14, True]  # 여러 자료형 혼합 가능
```

**인덱싱(Indexing)**
```python
numbers = [2, 3, 5, 7, 11, 13]

# 양수 인덱스 (앞에서부터, 0부터 시작)
print(numbers[0])   # 2
print(numbers[2])   # 5

# 음수 인덱스 (뒤에서부터, -1부터 시작)
print(numbers[-1])  # 13 (마지막)
print(numbers[-2])  # 11 (뒤에서 두 번째)
```

**슬라이싱(Slicing)**
```python
numbers = [2, 3, 5, 7, 11, 13]

print(numbers[2:5])   # [5, 7, 11] (인덱스 2, 3, 4)
print(numbers[2:])    # [5, 7, 11, 13] (인덱스 2부터 끝까지)
print(numbers[:3])    # [2, 3, 5] (처음부터 인덱스 2까지)
print(numbers[::2])   # [2, 5, 11] (처음부터 끝까지, 2칸씩)
print(numbers[::-1])  # [13, 11, 7, 5, 3, 2] (역순)
```

**리스트 수정**
```python
numbers = [2, 3, 5, 7, 11]

# 추가
numbers.append(13)          # 끝에 추가: [2, 3, 5, 7, 11, 13]
numbers.insert(0, 1)        # 특정 위치에 추가: [1, 2, 3, 5, 7, 11, 13]

# 삭제
del numbers[0]              # 인덱스로 삭제
numbers.remove(5)           # 값으로 삭제 (첫 번째만)
last = numbers.pop()        # 마지막 요소 꺼내기 (삭제 + 반환)
numbers.clear()             # 전체 삭제
```

⚠️ del vs remove 차이:
- del numbers[2] -> 인덱스 2번 삭제
- numbers.remove(5) -> 값이 5인 요소 삭제

**리스트 정렬**
```python
numbers = [19, 13, 2, 5, 3, 11, 7, 17]

# 새 리스트로 정렬 (원본 유지)
new_list = sorted(numbers)              # 오름차순
new_list = sorted(numbers, reverse=True)  # 내림차순

# 원본 리스트 직접 정렬
numbers.sort()                # 오름차순
numbers.sort(reverse=True)    # 내림차순
numbers.reverse()             # 순서 뒤집기 (정렬 아님!)
```
⚠️ numbers.sort(reverse = True)와 numbers.reverse의 차이
```python
numbers = [1,5,3,4,2]
numbers.reverse()
print(numbers)
# 출력 결과 : [2,4,3,5,1]

numbers.sort(reverse = True)
print(numbers)
#출력 결과 : [5,4,3,2,1]
```

**리스트 검색**
```python
numbers = [19, 13, 2, 5, 3, 11, 7, 17]

# 존재 여부 확인
print(19 in numbers)      # True
print(100 in numbers)     # False
print(100 not in numbers) # True

# 인덱스 찾기
print(numbers.index(13))  # 1 (없으면 오류!)

# 개수 세기
print(numbers.count(5))   # 1
```
---

### 딕셔너리
**기본 사용법**
key : value 쌍으로 데이터를 저장한다.

```python
my_bank = {
    '월급': '카카오뱅크',
    '생활비': 'kb국민',
    '투자': '한국투자증권',
    '비상금': '토스뱅크'
}

# 값 가져오기
print(my_bank['월급'])  # 카카오뱅크

# 값 수정
my_bank['생활비'] = 'ibk기업은행'

# 추가
my_bank['주택청약'] = '하나은행'

# 삭제
del my_bank['주택청약']
```

**딕셔너리 순회**
```python
# key만 순회
for key in my_bank.keys():
    print(key)
    
print() # 실행결과 구분

# value만 순회
for value in my_bank.values():
    print(value)
    
print()

# key, value 함께 순회
for key, value in my_bank.items():
    print(f"{key}: {value}")
    
print()

"""
출력 결과
월급
생활비
투자
비상금

카카오뱅크
kb국민
한국투자증권
토스뱅크

월급: 카카오뱅크
생활비: kb국민
투자: 한국투자증권
비상금: 토스뱅크
"""
```

---

### 유용한 내장 함수
enumerate() - 인덱스와 함께 순회
```python
fruits = ['사과', '바나나', '포도']

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 0: 사과
# 1: 바나나
# 2: 포도
```

zip() - 여러 리스트 동시 순회
```python
names = ['철수', '영희', '민수']
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}점")

# 철수: 85점
# 영희: 92점
# 민수: 78점
```
---

### List Comprehension ⭐
리스트를 한 줄로 만드는 파이썬다운 방식!

**기본 형태**
```python
# 일반적인 방식
squares = []
for i in range(10):
    squares.append(i * i)

# List Comprehension
squares = [i * i for i in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**조건 추가**
```python
# 짝수의 제곱만
squares = [i * i for i in range(10) if i % 2 == 0]
# [0, 4, 16, 36, 64]
```

**실전 예시**
```
# 문자열 리스트를 대문자로
words = ['hello', 'world', 'python']
upper_words = [word.upper() for word in words]
# ['HELLO', 'WORLD', 'PYTHON']

# 특정 조건 필터링
numbers = [1, -2, 3, -4, 5, -6]
positives = [n for n in numbers if n > 0]
# [1, 3, 5]
```



