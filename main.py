import random

list1=["Stone","Paper","Scissor"]

choice=random.choice(list1)
no_of_round=1
player=0
computer=0

print("Total number of round is 10. All the best!")

while(no_of_round<=10):
    inp1 = input("Please enter your choice. Your choices are Stone, Paper & Scissor-\n")
    choice = random.choice(list1)
    if inp1 == "Stone" or inp1=="stone" and choice == "Scissor" or choice == "scissor":
        player+=1
        print("You chose Stone and computer chose Scissor and thus you won\n")
    elif inp1 == "Stone" or inp1=="stone" and choice == "Paper" or choice == "paper":
        computer+=1
        print("You chose Stone and computer chose Paper and thus you lost\n")
    elif inp1 == "Stone" or inp1=="stone" and choice == "Stone" or choice == "stone":
        print("You chose Stone and computer chose Stone too and thus its a tie\n")
    elif inp1 == "Paper" or inp1=="paper" and choice == "Paper" or choice == "paper":
        print("You chose Paper and computer chose Paper too and thus its a tie\n")
    elif inp1 == "Paper" or inp1=="paper" and choice == "Scissor" or choice == "scissor":
        computer+=1
        print("You chose Paper and computer chose Scissor and thus you lost\n")
    elif inp1 == "Paper" or inp1=="paper" and choice == "Stone" or choice == "stone":
        player+=1
        print("You chose Paper and computer chose Stone and thus you won\n")
    elif inp1 == "Scissor" or inp1=="scissor" and choice == "Scissor" or choice == "scissor":
        print("You chose Scissor and computer chose Scissor and thus its a tie\n")
    elif inp1 == "Scissor" or inp1=="scissor" and choice == "Paper" or choice == "paper":
        player+=1
        print("You chose Scissor and computer chose Paper and thus you won\n")
    elif inp1 == "Scissor" or inp1=="scissor" and choice == "Stone" or choice == "stone":
        computer+=1
        print("You chose Scissor and computer chose Stone and thus you lost\n")

    elif inp1 != "Stone" or "Scissor" or "Paper" or "stone" or "paper" or "scissor":
        print("Wrong input. Please input between Stone, Scissor and Paper\n")
        continue
    print(10-no_of_round,"-Number of rounds left")
    no_of_round=no_of_round+1
    if(no_of_round>10):
        print("Game over")
if player>computer:
    print("Congrats! You won the game")
elif player<computer:
    print("Oops! You lost the game")
else:
    print("Match drawn")
print("Your score-", player)
print("Computer score-", computer)