#More printing

print("Mary had a little lamb.")
#make a format string without defining a new variable first, neat
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) #I'm convinced this string math is actually magic
#like, I'm trying to think of how I would do something so simple in C (granted it's been almost a year since I last used C)
#And I think I'd have to write a for loop, and I could probably make it a function I could call for any string and multiplier
#But I just appreciate that python can do all that within 'print'

#make a lot of one letter string variables
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#Put the strings together, and a space
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
#print() usually ends with a new line, but you can change that to something else by using end=''
