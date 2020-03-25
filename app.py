
#from  functions import calc

# concatenate your input
boo = input('Enter your girls name? ')
g_colour = input(' what is her favourite colour? ')

print(' your girls name is ' + boo + ' and her favourite colour is ' + g_colour)

# mini password checker
password = input(" Enter your password here: ")
if len(password) < 4:
    print("your password is too short")
elif len(password) > 12:
    print(" please type a shorter password which you can remember!")
else:
    print(f"password {hash(password)} looks good, don't worry it's encrypted")

# temperature checker



try:
    temp = input(" What is today's temperature ? ")
    if int(temp) >= 29:
        print(" you definitely don't want to wear anything today ")
    elif int(temp) <= 15:
        print(" you would want to wear 4 jackets and 3 pairs of jeans ")
    else:
        print(" Its a wonderful day ")
except ValueError:
    print("Dude!! temperatures are always numbers !! ")


# a three time guess game
# need to work on displaying guesses left to user // done

guess_count = 0
lives_available = 3
while guess_count < lives_available:
       guess = input(f'what is my girls name ? you have {lives_available - guess_count} chances left ')
       guess_count += 1
       if guess == boo:
           print("congrats you actually know me ")
           break
else:
    print(" Awwwww seems you don't know me that much ")


# car program

command =""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("bet you can hear that noise! it's your engine running dumbdumb!!!")
        print("car started")
    elif command == "stop":
        print("car Stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
help - for help menu
quit - to quit game
        """)
    elif command == "quit":
        break
    else:
        print(" sorry i don't understand what you typed, kindly press help to access menu")



