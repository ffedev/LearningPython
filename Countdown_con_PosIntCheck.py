
def check_positive_int_input(prompt):           # Modifico la funzione aggiungendo il check numero Int
    number = int(input(prompt))
    while number <= 0:
        print('Deve essere un numero positivo!')
        number = float(input(prompt))           # Qualcosa non funziona, il loop non mi permette di
    else:                                       # controllare i numeri float se prima non controlla i negativi
        print("Deve essere un numero intero!")  # se metto un negativo e inserisco un float dopo il messaggio
        number = int(input(prompt))             # di errore funziona, altrimenti va in errore.
    return number                               # Credo sia più comodo avere un check per tutto quello che NON È
                                                # un Positive Int, così da escludere lettere e simboli
startNumber = check_positive_int_input("Numero di partenza: ")

def count_down(n):
    print(n)
    if n > 0:
        return count_down( n -1)

count_down(startNumber)