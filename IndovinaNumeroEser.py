#Modify the higher or lower program from this section to keep track of
# how many times the user has entered the wrong number. If it is more
# than 3 times, print "That must have been complicated."
# at the end, otherwise print "Good job!"

number = 7
guess = -1
count = 0

print("Indovina il numero!")
while guess != number:
    guess = int(input("Il numero è... "))
    count = count + 1
    if guess == number:
        print("Hooray! Hai indovinato!")
        if count == 1:
            print("Hacker!")
        elif count > 4:
            print("Era Difficile?")
        elif count >= 3:
            print("è stato facile")
    elif guess < number:
        print("Piu grande...")
    elif guess > number:
        print("Piu piccolo.")