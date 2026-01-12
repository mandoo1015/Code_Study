# 📁 파일입출력

### 파일에 있는 내용 받아오기

**기본형식**
```python
with open('파일명', 'r') as f:
    for line in f:
        print(line)

# 출력결과
# 파일에 있는 내용을 한 줄씩 받아옴.
```
---

### strip()과 split()

**strip()**
```python
print("       abc     def         ".strip())
print("     \t      \n  abc def     \n\n\n".strip())

# 출력 결과
# abc     def
# abc def
```
앞 뒤의 화이트 스페이스 제거

**split()**
```python
my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split(". "))

numbers = ("    \n\n   2   \t   3  \n  5 7 11  \n\n".split())
print(numbers[0] + numbers[1])

# 출력 결과
# ['1', '2', '3', '4', '5', '6']
# 23
```
- split()은 문자열의 형태로 반환한다.
- 정수형 연산을 하고 싶다면 정수형으로 변환해줘야 한다.
  
---

### 파일에 쓰기
**쓰기**
```python
with open('new_file.txt', 'w') as f:
    f.write("Hello world!\n")
    f.write("My name is Codeit.\n")

# 출력 결과
"""
new_file.txt :

Hello world
my name is Codeit.
"""
```

**내용 추가**
```python
with open('new_file.txt', 'a') as f:
    f.write("Hello world!\n")
    f.write("My name is Codeit.\n")
```
'a' 앞에 파일명을 안 적었다면, 새로운 파일을 만들고 그곳에 내용 추가


