#Oh dear lord,

#Actually this looks kinda fun

#define variable with slots for stuff in format
formatter = "{} {} {} {}"
#did we really need to name this formatter?
#something like put_stuff_here would have been way less confusing
#but I guess that's kind of the point

#print formatter with numbers in slots
print(formatter.format(1, 2, 3, 4))
#print formatter with strings in slots
print(formatter.format("one", "two", "three", "four"))
#print formatter with boolean values in slots
print(formatter.format(True, False, False, True))
#print formatter with itself in slots
#Is this considered iiterative?
print(formatter.format(formatter, formatter, formatter, formatter))
#how about now?
print(formatter.format(
            formatter.format(1, 2, 3, 5),
            formatter.format('one', 'two', 'three', 'five'),
            formatter.format(3 == 3, 2 < 1, 2 + 1 > 2 + 2, 5 <= 7),
            formatter.format("gosh", "this", "is", "long")
    ))
#last one
print(formatter.format(
            " I can't wait\n",
            "To go to Mars\n",
            "And grow my crops\n",
            "In enclosed farms"
    ))
