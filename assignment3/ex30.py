#EX 30 --- IF ELSE
#I kinda want to show off the battleship game I wrote in C
#I had to let the computer make decisions about how to play
#And I made the computer really good at making those decisions
#By writing a WHOLE TON of nested and branching if-else statements
#It's so good that it beats an intelligent human about 45% of the time
#It would beat someone who doesn't use a good search pattern more often

people = 30
cars = 40
trucks = 15


if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
    #I forgot to indent the line above and it threw an error,
    #even though the else condition wasn't called
