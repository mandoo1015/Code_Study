with open('vocabulary.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        answer = line.strip().split(': ')
        english_word, korean_word = answer[0], answer[1]
        guess = input(f"{korean_word}: ")

        if guess == english_word:
            print("맞았습니다!\n")
        else:
            print(f"아쉽습니다. 정답은 {english_word}입니다.\n")




