

"""
Dies ist ein Rechner um Kämpfe im Buch Einsamer Wolf schnell zu rechnen.
Erst eine kurze Abfrage der eigenen Stärke und Ausdauer sowie dies Monsters.
To do:
    - Kampftabelle https://mantikoreverlag.de/wp-content/uploads/downloads/1/EW_Kampftabelle.pdf
      muss noch abgebildet werden.
"""

# import random

# Hier die Variablendefinitionen.

HeldenKraft = int((input("Wie hoch ist deine Kraft? ")))
HeldenAusdauer = int((input("Wie ist deine Ausdauer? ")))
# TODO: Dictionaries fertig machen
KampfErgebnisseF = {
    "0-11": -6,
    "0-10": -7,
    "0-9": -7,
    "0-8": -8,
    "0-7": -8,
    "0-6": -9,
    "0-5": -9,
    "0-4": -10,
    "0-3": -10,
    "0-2": -11,
    "0-1": -11,
    "0-0": -12,
    "00": -12,
    "01": -14,
    "02": -14,
    "03": -16,
    "04": -16,
    "05": -18,
    "06": -18,
    "07": -99,
    "08": -99,
    "09": -99,
    "010": -99,
    "011": -99,

    "1-11": -0,
    "1-10": -0,
    "1-9": -0,
    "1-8": -0,
    "1-7": -0,
    "1-6": -0,
    "1-5": -0,
    "1-4": -1,
    "1-3": -1,
    "1-2": -2,
    "1-1": -2,
    "1-0": -3,
    "10": -3,
    "11": -4,
    "12": -4,
    "13": -5,
    "14": -5,
    "15": -6,
    "16": -6,
    "17": -7,
    "18": -7,
    "19": -8,
    "110": -8,
    "111": -9,
}
KampfErgebnisseH = {
    "0-11": -0,
    "0-10": -0,
    "0-9": -0,
    "0-8": -0,
    "0-7": -0,
    "0-6": -0,
    "0-5": -0,
    "0-4": -0,
    "0-3": -0,
    "0-2": -0,
    "0-1": -0,
    "0-0": -0,
    "00": -0,
    "01": -0,
    "02": -0,
    "03": -0,
    "04": -0,
    "05": -0,
    "06": -0,
    "07": -0,
    "08": -0,
    "09": -0,
    "010": -0,
    "011": -0,

    "1-11": -99,
    "1-10": -99,
    "1-9": -99,
    "1-8": -8,
    "1-7": -8,
    "1-6": -6,
    "1-5": -6,
    "1-4": -6,
    "1-3": -6,
    "1-2": -5,
    "1-1": -5,
    "1-0": -5,
    "10": -5,
    "11": -5,
    "12": -5,
    "13": -4,
    "14": -4,
    "15": -4,
    "16": -4,
    "17": -4,
    "18": -4,
    "19": -3,
    "110": -3,
    "111": -3,
}
Zufallszahl = 1 # TODO: Random Kommentar entfernen random.randint(0, 2)
# Teil1 = 0
Unentschieden = True
AnzahlKampf = 0
Nochmal = True
MonsterKraft = 0
MonsterAusdauer = 0
# Hier beginnt das Programm


def kampfNeu():
    global Zufallszahl
    global HeldenAusdauer
    global MonsterAusdauer
    global HeldenKraft
    global MonsterKraft
    KampfQoutient = HeldenKraft - MonsterKraft
    Teil1 = str(Zufallszahl) + str(KampfQoutient)
    HeldenAusdauer =  HeldenAusdauer + KampfErgebnisseH[Teil1]
    MonsterAusdauer = MonsterAusdauer + KampfErgebnisseF[Teil1]
    return HeldenAusdauer, MonsterAusdauer


while Nochmal == True:
    MonsterKraft = int(input("Wie ist die Kraft des Monsters? "))
    MonsterAusdauer = int(input("Wie ist die Ausdauer des Monsters? "))
    print("Du hast also ", HeldenKraft, " Kraft und ", HeldenAusdauer, " Ausdauer.")
    print("Dein Gegner hat ", MonsterKraft, " Kraft und ", MonsterAusdauer, " Ausdauer.")
    print("Der Kampf beginnt!")
    while HeldenAusdauer > 0 and MonsterAusdauer > 0:
        kampfNeu()
        AnzahlKampf += 1
        print("Runde:", AnzahlKampf)
        print("Heldenausdauer neu: ", HeldenAusdauer, " - Monsterausdauer neu: ", MonsterAusdauer)
    else:
        if HeldenAusdauer <= 0 and MonsterAusdauer <= 0:
            print("Beide sind wohl tot!")
        elif HeldenAusdauer > 0 and MonsterAusdauer <= 0:
            print("Monster ist wohl tot! Deine restliche Ausdauer ist", HeldenAusdauer)
            print("Du kannst jetzt weiter kämpfen.")
        else:
            print("Held tot!")
            Nochmal = False

print("Danke fürs spielen!")