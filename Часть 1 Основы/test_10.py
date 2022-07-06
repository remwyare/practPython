import random

def hangman(words):
    i = random.randint(0,len(words)-1)
    word = words[i]
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    board = ["__"] * len(word)
    rletters = list(word)
    win = False
    print("Добро пожаловать на казнь!")
    
    while wrong < len(stages):
        char = input("Введите букву: ")
        if char in rletters:
            i = rletters.index(char)
            board[i] = char
            rletters[i] = "$$"
            if "__" not in board:
                print("Вы выиграли! было загадано слово: ")
                print(" ".join(board))
                win = True
                break
        else:
            wrong +=1
        print(" ".join(board))
        print("\n".join(stages[:wrong+1]))
    if not win:
        print("Вы проиграли! Было загадано слово: {}".format(word))
        
        
                
    






    
while True:
    if input("Y/N?") == "N":
        break
    hangman(["кот","собака","кит","крот","рыбка","попугай","корова","аист", "Орел"])    
