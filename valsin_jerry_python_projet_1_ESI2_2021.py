import random

player1 = {
    "name": "",
    "lifes": 50,
    "potions": 3,
}

player2 = {
    "name": "Ennemi",
    "lifes": 50,
    "potions": 0,
}


def attack():
    damage = random.randint(5, 10)
    player1["lifes"] = player1["lifes"] - damage

    if player1["lifes"] <= 0:
        endGame(1)

    print("You suffer ", damage, "damage")


def attackPlayer():
    damage = random.randint(5, 15)
    player2["lifes"] = player2["lifes"] - damage

    print("You inflict ", damage, "damage")

    if player2["lifes"] <= 0:
        endGame(2)


def takePotion():
    treatment = random.randint(15, 50)
    player1["lifes"] = player1["lifes"] + treatment
    player1["potions"] = player1["potions"] - 1
    print("You recover ", treatment, "of life")


def overview():
    print("You have ", player1["lifes"],
          "life points and your opponent has", player2["lifes"], "life points")


def actionPlayer():
    choice = 0
    while choice != 1 and choice != 2:
        if player1["potions"] > 0:
            choice = int(
                input("Would you like to attack (1) or use a potion (2)? "))
        else:
            choice = int(
                input("You have no more potions, you can only attack (1) : "))

    print(" ")

    if choice == 1:
        attackPlayer()
    if choice == 2:
        takePotion()

    print(" ")

    if player1["lifes"] > 0 and player2["lifes"] > 0:
        attack()
        print(" ")
        overview()


def endGame(lost):
    if lost == 1:
        print("Player ", player2["name"], "to win")
    else:
        print("Player ", player1["name"], "to win")


player1["name"] = input("Player name : ")

while player1["lifes"] > 0 and player2["lifes"] > 0:
    actionPlayer()
