#EX 18
#Finally Functions!!

#can we make functions that act on variables?
#can we make functions that return a variable? -- yes
#what does * do? Does it mean it's a certain type of object?
#can function names contain numbers--yes

#Bad Madlibs
def print2(*words):
    noun, verb = words
    print(f"The beautiful {noun} {verb} on the beach.")

def print2_new(verb, noun):
    print(f"A sunbather {verb} on a beach towel.")
    print(f"He enjoyed the sights, such as the {noun}.")

def print1(noun):
    print(f"He was happy to get a close-up view of the {noun}.")

def print0():
    print("That is a range violation.")

print2("Starship prototype", "stood")
print2_new("watched", "rocket")
print1("static-fire")
print0()
