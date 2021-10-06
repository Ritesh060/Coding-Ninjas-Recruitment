import random

words = ["ant", "elepphant", "mouse", "horse", "lizard", "yak", "tiger", "eagle", "camel", "pigeon", "hawk", "donkey", "pig", "zebra", "bison", "falcon", "goat", "iguanas", "jackal", "kite", "leopard", "macaw", "ningen", "owl"]

def word():
    word = random.choice(words)
    return word.upper()


def hangman(tries):
    states = ["""                 |--------------
                 |              |
                 |              O
                 |           \  |    /
                 |              |
                 |              /\
                 |   
                 
                 """,
            """               |-----------------
               |                |
               |                O
               |            \   |  /
               |                |
               |                /
               |
                                       
                                       """,
            """               |--------------
               |              |
               |              O
               |           \  |    /
               |              |
               |              
               |   
                 
                 """,
            """               |--------------
               |              |
               |              O
               |           \      /
               |              
               |             
               |   
                 
                 """,
                """                   |--------------
                   |              |
                   |              O
                   |           \     
                   |              
                   |              
                   |   
                 
                 """,
                 """                    |--------------
                    |              |
                    |              O
                    |                
                    |              
                    |              
                    |   
                 
                 """
                 ,
                 """                    |--------------
                    |              |
                    |              
                    |                 
                    |              
                    |              
                    |   
                 
                 """             
                ]
    return states[tries]

def play(word):
    word_blank  = "_ " * len(word)
    win = False
    guessed_letters = []
    guessed_word = []
    tries = 6
    print("Welcome to Hangman!!!")
    print("Guess the correct word to win.")
    print(hangman(tries))
    print(word_blank)
    print()
    while not win and tries>0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in word:
                print(guess, "is not in the word.")
                tries-=1
            else:
                print(guess,"is in the word.")
                guessed_letters.append(guess)
                word_list_guessed = list(word_blank)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_list_guessed[index] = guess

                word_blank = "".join(word_list_guessed)
                if word  in word_blank:
                    win = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess.upper in guessed_word:
                print("You already guessed the word", guess)
            elif guess.upper() != word:
                print(guess, "is not the word.")
                tries-=1
                guessed_word.append(guess)

            else:
               if word in guess.upper():
                   win = True
                   break


        else:
            print("Not a valid guess")

        print(hangman(tries))
        print(word_blank)
        print()
    if win:
        print("You won the game!!")
    else:
        print("You ran out of tries and lost. The word was", word, ".")


def play_game():
    u = word()
    play(u)
    while input("Want to play again??(Y/N)").upper() == "Y":
        u = word()
        play(u)
play_game()

