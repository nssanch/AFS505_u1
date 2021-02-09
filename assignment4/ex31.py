#EX 31 Making Decisions

print("""You enter a dark room with three doors.
Do you go through door #1, door #2, or door #3?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("You are standing on a beach.")
    print("Flat marsh lies behind you, endless waves are ahead.")
    print("What do you do?")
    print("1. Walk into the ocean")
    print("2. Turn around and walk inland")

    direction = input("> ")
    if direction == "1":
        print("You are pulled under the waves and drown in watery depths")
        print("You saw a giant squid before you died. Good job!")
    elif direction == "2":
        print("You see a fully stacked Starship on the orbital launch pad.")
        print("What do you do?")
        print("1. Get on board.")
        print("2. Sit down and watch the launch.")

        launch = input("> ")
        if launch == "1":
            print("You are going to Mars. Good job!")
        else:
            print("You aren't supposed to be here.")
            print("You are excorted away by security. Good job!")
    else:
        print("That sound boring.")

else:
    print("You stumble around and fall on a knife and die. Good job!")
