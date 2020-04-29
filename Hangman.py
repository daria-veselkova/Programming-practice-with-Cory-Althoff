import random


def hangman(word):
    wrong = 0
    stages = ["____________             ",
              "|           |            ",
              "|           |            ",
              "|           O            ",
              "|          /|\           ",
              "|          / \           ",
              "|                        ",
              "|                        ",]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False

    print("Добро пожаловать на казнь!")
    print("Слово: ", " ".join(board))

    while wrong < len(stages):
        print("\n")
        msg = input("Введите букву: ")
        if msg in rletters:
            ind = rletters.index(msg)
            board[ind] = msg
            rletters[ind] = "$"
            print(" ".join(board))
        else:
            wrong += 1
            e = wrong + 1
            print("\n".join(stages[0:e]))

        if "_" not in board:
            print("Вы выиграли! Было загадано слово: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("Вы проиграли! Было загадано слово: {}.".format(word))


words = ["cat", "dog", "sheep", "horse", "mouse", "mice", "deer", "hamster",
         "bird", "whale", "apple", "orange", "melon", "ginger", "berry", "tomato",
         "cabbage", "cucumber", "pear", "tree", "rock", "earth", "lake", "river",
         "mountain", "sun", "water", "wind", "storm"]
random_word = random.choice(words)

hangman(random_word)
