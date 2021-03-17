import sys

# Board
mijnbord = ["-", "-", "-",
            "-", "-", "-",
            "-", "-", "-", ]

# Vetoond het bord


def borddisplay():
    print(mijnbord[0] + " | " + mijnbord[1] + " | " + mijnbord[2])
    print(mijnbord[3] + " | " + mijnbord[4] + " | " + mijnbord[5])
    print(mijnbord[6] + " | " + mijnbord[7] + " | " + mijnbord[8])

# Invoer van de waardes voor speler 1 en speler 2


def spelers():

    def speler1():
        answer = int(
            input("Speler 1: Geef een getal tussen 0 en 9 voor je antwoord ")) - 1
        mijnbord[answer] = str("X")
        borddisplay()
        regels()

    def speler2():
        answer = int(
            input("Speler 2: Geef een getal tussen 0 en 9 voor je antwoord ")) - 1
        mijnbord[answer] = str("O")
        borddisplay()
        regels()

    speler1()
    speler2()

# Game logic


def regels():

    speler1bericht = ("Speler 1 wint!")
    speler2bericht = ("Speler 2 wint!")
    speler1sign = "X"
    speler2sign = "O"

    # Horizontaal Speler 1
    if mijnbord[0] == speler1sign and mijnbord[1] == speler1sign and mijnbord[2] == speler1sign or \
            mijnbord[3] == speler1sign and mijnbord[4] == speler1sign and mijnbord[5] == speler1sign or \
    mijnbord[6] == speler1sign and mijnbord[7] == speler1sign and mijnbord[8] == speler1sign:
        print(speler1bericht)
        sys.exit()

    # Verticaal Speler 1
    if mijnbord[0] == speler1sign and mijnbord[3] == speler1sign and mijnbord[6] == speler1sign or \
            mijnbord[1] == speler1sign and mijnbord[4] == speler1sign and mijnbord[7] == speler1sign or \
    mijnbord[2] == speler1sign and mijnbord[5] == speler1sign and mijnbord[8] == speler1sign:
        print(speler1bericht)
        sys.exit()

    # Diagonaal Speler 1
    if mijnbord[0] == speler1sign and mijnbord[4] == speler1sign and mijnbord[8] == speler1sign or \
            mijnbord[2] == speler1sign and mijnbord[4] == speler1sign and mijnbord[6] == speler1sign:
        print(speler1bericht)
        sys.exit()

    # Horizontaal Speler 2
    if mijnbord[0] == speler2sign and mijnbord[1] == speler2sign and mijnbord[2] == speler2sign or \
            mijnbord[3] == speler2sign and mijnbord[4] == speler2sign and mijnbord[5] == speler2sign or \
    mijnbord[6] == speler2sign and mijnbord[7] == speler2sign and mijnbord[8] == speler2sign:
        print(speler2bericht)
        sys.exit()

    # Verticaal Speler 2
    if mijnbord[0] == speler2sign and mijnbord[3] == speler2sign and mijnbord[6] == speler2sign or \
            mijnbord[1] == speler2sign and mijnbord[4] == speler2sign and mijnbord[7] == speler2sign or \
    mijnbord[2] == speler2sign and mijnbord[5] == speler2sign and mijnbord[8] == speler2sign:
        print(speler2bericht)
        sys.exit()

    # Diagonaal Speler 2
    if mijnbord[0] == speler2sign and mijnbord[4] == speler2sign and mijnbord[8] == speler2sign or \
            mijnbord[2] == speler2sign and mijnbord[4] == speler2sign and mijnbord[6] == speler2sign:
        print(speler2bericht)
        sys.exit()


while "-" in mijnbord:
    spelers()
else:
    print("Het spel is voorbij. Er is geen winnaar.")
