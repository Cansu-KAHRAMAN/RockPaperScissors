#rock paper scissors game
import random
while True:
    choices=["rock","paper","scissors"]
    computer= random.choice(choices)  #bilgisayarın seçimi
    player= None

    while player not in choices:   #listenin içinde olan bir şey seçilene kadar devam et sormaya
        player= input("rock, paper or scissors?: ").lower()  #oyuncunun seçimini alma

    if player == computer:
        print("computer: ",computer)  #bilg ve oyuncunun verisini yazdırma
        print("player: ",player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ",computer)
            print("player: ",player)
            print("I won!")
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("You won!")   
    elif player == "paper":
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("I won!")
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You won!")   
    elif player == "scissors":
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("I won!")
        if computer == "paper":
            print("computer: ",computer)
            print("player: ",player)
            print("You won!")   
    
    play_again = input("Play Again? (yes/no): ").lower()  #yeniden oynamak ister misin

    if play_again != "yes":  #hayır döngüden çık
        break
print("Byee!")    