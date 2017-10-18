# Questo programma calcola le Aree delle figure geometriche
# utilizza un menù testuale, e presto verranno aggiunte
# nuove funzionalità


def rectangle_area(base, altezza):
    return base * altezza


def square_area(lato):
    return lato * lato


def circle_area(raggio):
    return 3.14 * raggio**2


def print_welcome(name):
    print('Ciao,', nome, "Questo programma è in grado di calcolare le Aree.")  # Ho aggiunto un commento 


def menu_comandi():
    print("Comandi:")
    print(" 'M' torna al menù dei comandi")
    print(" 'Q' calcola l'area del quadrato")
    print(" 'R' calcola l'area del rettangolo")
    print(" 'C' calcola l'area del cerchio")
    print(" 'E' esci dal programma")


def check_positive_input(prompt):
    number = float(input(prompt))
    while number <= 0:
        print('Deve essere un numero positivo!')
        number = float(input(prompt))
    return number


nome = input('Inserisci il tuo nome: ')

print_welcome(nome)

comando = "m"
while comando != "e":
    if comando == "q":
        lato = check_positive_input("Lato: ")
        print("Area del quadrato:", square_area(lato))
        comando = input("Comandi: ")
    elif comando == "r":
        base = check_positive_input("Base del rettangolo: ")
        altezza = check_positive_input("Altezza del rettangolo: ")
        print("Area del rettangolo:", rectangle_area(base, altezza))
        comando = input("Comandi: ")
    elif comando == "c":
        raggio = check_positive_input("Raggio del cerchio: ")
        print("Area del cerchio: ", circle_area(raggio))
        comando = input("Comandi: ")
    elif comando == "m":
        menu_comandi()
        comando = input("Comandi: ")
    elif comando == "e":
        print(" ", end="")
    else:
        print("Comando non accettato.")                 #Come rendere l'input dei comandi Case insensitive?
        comando = input("Inserisci un comando valido: ")   # Potrei usare "E, e"? ma sembra scomodo...
