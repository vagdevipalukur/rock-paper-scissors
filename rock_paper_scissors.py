import random
choices=["rock", "paper", "scissors"]
user=input("enter rock,paper or scissors:")
computer=random.choice(choices)
print("computer chose",computer)
if user==computer:
    print("it's s tie!")
elif user=="rock" and computer=="scissors":
    print("you win!")
elif user=="paper" and computer=="rock":
    print("you win!")
elif user=="scissors" and computer=="paper":
    print("you win!")
elif user not in choices:
    print("invaild choice!")
else:
    print("computer wins!")
