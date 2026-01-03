import random 
choices=['rock','paper','scissors']
computer=random.choice(choices)
user=input("Enter your choice: ")
print("com choose:",computer)
if user==computer:
    print("Draw")
elif(user == "rock" and computer == "scissors") or \
    (user == "paper" and computer == "rock") or \
    (user == "scissors" and computer == "paper"):
    print("Congragulation you win!!!!")

else:
    print("you lose!!!")