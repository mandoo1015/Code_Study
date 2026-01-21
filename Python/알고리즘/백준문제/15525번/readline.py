import sys

T = int(input("테스트케이스 개수를 입력하세요 : "))

for i in range (T):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(a + b)