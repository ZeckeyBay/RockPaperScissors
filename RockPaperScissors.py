import random

def play():
    user = input("Seciminiz nedir ? 't' tas icin, 'k' kagıt icin,'m' makas icin\n")
    computer = random.choice(["t","k","m"])

    if user == computer:
        return "Berabere!"

    if is_win(user,computer):
        return "Kazandınız!"
    else:
        return "Kaybettiniz!"

def is_win(player,opponent):
    if (player == "t" and opponent == "m") or (player == "m" and opponent == "k") or (player == "k" and opponent == "t"):
        return True
print(play())

""" Deneme """
