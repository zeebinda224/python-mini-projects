import random
def play():
    user=input("Enter your choice: r for rock, p for paper, s for scissors\n")
    robot=random.choice(["r","p","s"])

    if user==robot:
        return "Tie"
    if is_win(user,robot):
        return "You won!"
       
    
def is_win(player,opponent):
    if (player =="r" and opponent =="s") or (player =="s" and opponent=="p")\
    or (player =="p" and opponent =="r"):
        return True
    e
    
print(play())


