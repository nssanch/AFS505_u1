#EX 29 --- IF statements
#A programer's wife tells him
#"to go to the store to get a gallon of milk and if there's eggs, get a dozen"
#He comes back with 12 gallons of milk
#Because there were eggs

##I don't like genderstereotyping the programmer, but it makes the joke flow better

people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")
