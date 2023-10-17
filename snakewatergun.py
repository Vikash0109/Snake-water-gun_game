import random

print("It's time to play the game \"Snake Water Gun\"\n")
name = input("Enter your name: ")
I = 0
k = 0
Rule = input("The main rules are: \"Gun will kill the snake, but it gets destroyed by water. Water does not kill the snake, but the snake drinks the water\"\nType [Y] to start the game: ")
if Rule == 'Y':
    print("Start... Play well!")

while True:
    k = k + 1
    player = input("Enter your choice [gun, water, snake]: ")

    words = ["gun", "water", "snake"]
    word = random.choice(words)

    print("You:", player)
    print("Computer:", word)
    print(f"\n{player}   VS  {word}")

    if player == word:
        print("Draw!")
        I = I + 2.5
    else:
        if word == "gun" and player == "water":
            print("You won!")
            I = I + 5
        elif word == "gun" and player == "snake":
            print("You lost!")
        elif word == "water" and player == "snake":
            print("You won!")
            I = I + 5
        elif word == "water" and player == "gun":
            print("You lost!")
        elif word == "snake" and player == "water":
            print("You lost!")
        elif word == "snake" and player == "gun":
            print("You won!")
            I = I + 5
        else:
            print("Invalid syntax")

    if k == 5:
        print(f"{name}'s score is {I}")
        break

