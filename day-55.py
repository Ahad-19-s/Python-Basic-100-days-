import random

def game_result(user,computer):
    if user== computer:
        return "DRAW"
    elif(user == "sanke" and computer=="water"):
        return "User Win"
    elif(user=="water"and computer== "gan") or (user== "gan" and computer== "snake"):
        return "User Win"
    else:
        return "computer wins"




choices=["shanke","water","gan"]
user_choice=input("Enter the shake,water,gan: ")
computer_choice=random.choice(choices)
result= game_result(user_choice,computer_choice)


print(f"user choose:{user_choice}")
print(f"computer chose: {computer_choice}")
print(result)