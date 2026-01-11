import random

chance = 4
answer = random.randint(1, 20)  # 1에서 20사이의 랜덤한 숫자를 정답으로 설정
trial_num = 0
success = False  # 성공 여부를 False로 설정

while chance > 0:   # 4번의 기회 설정
    # 정답 입력 받기
    trial = int(input(f"기화가 {chance}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요 : "))

    trial_num += 1  # 시도 횟수 1 증가
    chance -= 1  # 기회는 1 감소

    if trial == answer:  # 정답을 맞췄다면
        success = True
        break
    elif trial > answer:  # 시도가 정답보다 크다면
        print("Down")
    elif trial < answer:  # 시도가 정답보다 작다면
        print("UP")

if success:
    print(f"축하합니다. {trial_num}번만에 숫자를 맞히셨습니다.")
else:
    print(f"아쉽습니다. 정답은 {answer}였습니다.")