import random

def play():
    user = input("Seciminiz nedir ? 'r' tas icin, 'p' kagıt icin,'s' makas icin\n")
    computer = random.choice(["r","p","s"])

    if user == computer:
        return "Berabere!"

    if is_win(user,computer):
        return "Kazandınız!"
    else:
        return "Kaybettiniz!"

def is_win(player,opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True
print(play())