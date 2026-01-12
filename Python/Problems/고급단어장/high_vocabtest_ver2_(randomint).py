import random

vocab = {}
with open('vocabulary.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        data = line.strip().split(': ')
        # ['cat', '고양이'], ...
        english_word, korean_word = data[0], data[1]
        vocab[english_word] = korean_word

# 키 목록 가져오기 ['cat', 'apple', 'church', ...]
keys = list((vocab.keys()))

# 문제 내기
while True:
    # 랜덤한 문제 받아오기
    index = random.randint(0, len(keys)-1)
    english_word = keys[index]
    korean_word = vocab[english_word]

    # 유저 입력값 받기
    guess = input(f"{korean_word}: ")

    if guess == english_word:
        print("맞았습니다!")
    elif guess == 'q':
        break
    else:
        print(f"틀렸습니다. 정답은 {english_word}입니다.")
