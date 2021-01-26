#Fun with Strings

#Define types_of_people as 10
types_of_people = 10
#define x as a f-string with types_of_people
x = f"There are {types_of_people} types of people."

#define two variable as simple strings
binary = "binary"
do_not = "don't"
#define y as a f-strign using binary and do_not
y = f"Those who know {binary} and those who {do_not}."

#print the f-string variables
print(x)
print(y)

#print f-strings with f-string variables
print(f"I said: {x}")
print(f"I also said: '{y}'")

#How does python treat 'False'? Is it stored as a 0, is it its own thing, or what
#after reading more, its a boolean value, which still doesn't entirely explain it, but I'm fine with that answer for now
hilarious = 4 > 6

#Define variabe with space for another variable,
joke_evaluation = "Isn't that joke so funny?!\n\t {}"

#I think I'll have fun with this
#Does it just tell the variable which variable to put inside
print(joke_evaluation.format(hilarious))

#Define two more string variables
w = "This is the left side of..."
e = "a string with a right side."

#print the two strings together
#I guess the '+' can concatenate strings
print(w + e)
