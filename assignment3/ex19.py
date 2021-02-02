def countdown(SN, time):
    print(f"SN{SN} is fueled and ready to launch.")
    print(f"Liftoff is in T-{time} minutes.")
    print("Better tune in to the live stream.\n")


print("We can just give the function numbers directly:")
countdown(9, 22)


print("OR, we can use variables from our script:")
prototype_number = 10
time_remaining = 27000

countdown(prototype_number, time_remaining)


print("We can even do math inside too:")
countdown(10-2, "one month ago")


print("And we can combine the two, variables and math:")
countdown(prototype_number + 1, time_remaining * 3)
