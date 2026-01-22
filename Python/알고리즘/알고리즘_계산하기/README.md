# 알고리즘 분석하기

## 알고리즘 분석 시간 아끼는 방법
- 반복문에 집중
- 내장 함수 집중

## 탐색과 정렬 계산하기

### 선형 탐색 알고리즘 계산
```python
def linear_search(target, data):
    n = len(data)
    for idx in range(n):
        if target == data[idx]:
            return idx
```
**계산과정**
```
for idx in range(n) : n번 반복 -> O(n)

결과 : O(n)
```
---

### 이진 탐색 알고리즘 계산
```python
def binary_search(target, data):
    left_index, right_index = 0, len(data) - 1
    while left_index <= right_index:
        mid_idx = (left_index + right_index) // 2
        mid_element = data[mid_idx]
        if target == mid_element:
            return mid_idx
        elif target < mid_element:
            right_index = mid_idx - 1
        elif target > mid_element:
            left_index = mid_idx + 1
```
**계산과정**
```
while ~:
    mid_idx = (left_index + right_index) // 2

최악의 경우 : 반절씩 쪼개서 한 개만 남을 때까지
-> O(lg n)

결과 : O(lg n)
```

---

### 선택 정렬 알고리즘 계산
```python
def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]: 
                min_idx = j
        data[min_idx], data[i] = data[i], data[min_idx]
```
**계산과정**
```python
for i in range(n):
        min_idx = i # -> O(n)
        for j in range(i + 1, n):
            # ...... (2)

        data[min_idx], data[i] = data[i], data[min_idx] # -> O(n)
```

```python
# (2)
for j in range(i + 1, n):
            if data[j] < data[min_idx]: 
                min_idx = j
```
| i | 시행 횟수 |
| :----: | :----: |
| 0 | n - 1 |
| 1 | n - 2 |
| 2 | n - 3 |
| ... | ... |
| n-1 | 1 |

총 시행 횟수 : `(n-1)` * `(n)` / `2` -> `O(n²)` (최선, 최악, 평균 상관없이 모두)

결과 : `O(n)` + `O(n²)` + `O(n)` -> `O(n²)`

---

### 삽입정렬 알고리즘 계산

**최선 : 리스트가 이미 정렬되어 있을 때**

한번씩 거쳐만 가면 됨 -> `O(n)`

**최악 : 리스트가 역순으로 정렬되어 있을 때**

- 인덱스가 1일 때 -> 1번 옮김
- 인덱스가 2일 때 -> 2번 옮김

...

- 인덱스가 마지막일 때 -> n -1번 옮김

`1` + `2` + ... + `(n - 1)` : `O(n²)`


## 일반적인 시간 복잡도
`O(1)` < `O(lg n)` < `O(n)` < `O(n lg n)` < `O(n²)`

## 공간복잡도
입력해주는 데이터의 크기에 따라 **차지하는 메모리 공간**이 얼마나 증가하는지를 나타내는 지표



