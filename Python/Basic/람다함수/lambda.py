from functools import reduce

# sorted와 함께
students = [("철수", 85), ("영희", 92), ("민수", 78)]
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
# [("영희", 92), ("철수", 85), ("민수", 78)]

# map, filter, reduce와 함께
numbers = [1, 2, 3, 4, 5]
reduced = reduce(lambda x, y: x + y, numbers)
# 15 (1 + 2+ 3+ 4+ 5)
doubled = list(map(lambda x: x * 2, numbers))
# [2, 4, 6, 8, 10]
filtered = list(filter(lambda x: x > 2, numbers))
# [3, 4, 5]
