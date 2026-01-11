import random

# 상수 정의
ANSWER = random.randint(1, 20)
CHANCE = 4

# 변수 정의
tries = 0
guess = -1

while guess != ANSWER and tries < CHANCE:

    guess = int(input(f"기화가 {CHANCE - tries}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요 : "))

    tries += 1

    if guess > ANSWER:
        print("Down")
    elif guess < ANSWER:
        print("UP")

if guess == ANSWER:
    print(f"축하합니다. {tries}번만에 숫자를 맞히셨습니다.")
else:
    print(f"아쉽습니다. 정답은 {ANSWER}였습니다.")
