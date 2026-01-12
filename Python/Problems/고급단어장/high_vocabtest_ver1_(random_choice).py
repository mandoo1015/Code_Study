import random

vocab = {}
with open('vocabulary.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        data = line.strip().split(': ')
        # ['cat', '고양이'], ...
        english_word, korean_word = data[0], data[1]
        vocab[english_word] = korean_word

keys = list((vocab.keys()))
while True:
    english_word = random.choice(keys)
    korean_word = vocab[english_word]

    guess = input(f"{korean_word}: ")

    if guess == english_word:
        print("맞았습니다!")
    elif guess == 'q':
        break
    else:
        print(f"틀렸습니다. 정답은 {english_word}입니다.")
        
