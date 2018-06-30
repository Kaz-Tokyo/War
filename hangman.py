import random
print("Type f to finish inserting words.")
wordlist = []
while True:
    wordstorage = input("Type a word for the game:")
    wordlist.append(wordstorage)
    if wordstorage == "f":
        wordlist.pop()
        break
d = len(wordlist)-1
word = wordlist[random.randint(0,d)]
def hangman(word):
    print("Welcome to Hangman")
    wrong=0
    stages=["",
            "________        ",
            "|       |       ",
            "|       |       ",
            "|       O       ",
            "|      /|\      ",
            "|      / \      ",
            "|    _______    "]
    rletters=list(word)
    board=["_"]*len(word)
    win=False

    while wrong < len(stages)-1:
        print("\n")
        msg="Guess a character in the word:"
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]="$"
        else:
            wrong +=1
        print((" ".join(board)))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!")
            print((" ".join(board)))
            win=True
            break
    if "_" in board:
        print("You lose.. It was {}.".format(word))

