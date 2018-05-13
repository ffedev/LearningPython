import random

Avengers = ["Hawkeye", "Black Widow", "Ant-Man", "Falcon",
            "Winter Soldier", "War Machine", "Spider-Man",
            "Captain America", "Iron Man", "Black Panther",
            "Scarlet Witch", "Vision", "Thor", "Hulk",
            "Thanos", "Star-Lord", "Gamora", "Loki",
            "Quicksilver", "Doctor Strange", "Nebula",
            "Nick Fury",
            "Rocket", "Heimdall", "Groot", "Drax",
            "Mantis"]


def coinToss():
    flip = random.randrange(2)
    return flip

def fingerSnap():
    for i in range(len(Avengers)):
        coinToss()
        if coinToss() == 0:
            print(Avengers[i] + ": Vive")
        else:
            print(Avengers[i] + ": Muore")

def print_welcome():
    print("Ciao, con questo programma puoi schioccare le dita e scoprire quali Avengers verranno distrutti.")

print(print_welcome())

#nome = input('Inserisci il tuo nome: ')

def menu_comandi():
    print(" ________________________Comandi__________________________")
    print("|                                                        |")
    print("|'M' torna al menù dei comandi                           |")
    print("|'S' Schiocca le dita con il guanto dell'infinito        |")
    print("|'A' Aggiungi personaggi extra alla lista degli Avengers |")
    print("|'C' Credits                                             |")
    print("|'E' esci dal programma                                  |")
    print("|________________________________________________________|")

comando = "m"
while comando != "e":
    if comando == "s":
        fingerSnap()
        comando = input("Comandi: ")
    elif comando == "a":
        add = input("Aggiungi un nome: ")
        if add not in Avengers:
            Avengers.append(add)
        comando = input("Comandi: ")
    elif comando == "c":
        print("Made By Trenton!")
        comando = input("Comandi: ")
    elif comando == "m":
        menu_comandi()
        comando = input("Inserisci un comando: ")
    elif comando == "e":
        print(" ", end="")
    else:
        print("Comando non accettato.")                 #Come rendere l'input dei comandi Case insensitive?
        comando = input("Inserisci un comando valido: ")   # Potrei usare "E, e"? ma sembra scomodo...



#print(fingerSnap())

# Aggiungi i tuoi amici:
# Scommetti su uno di loro

