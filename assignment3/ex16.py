#EX 16
#Reading and Writing files

from sys import argv
script, filename = argv

print(f"This program will erase {filename}. Do you want to proceed?")
print("Press Ctr + C to quit program.")
print("Otherwise, press ENTER to continue.")
input("...")

txt = open(filename, 'w')
txt.truncate()
print(f"Great, {filename} has been erased.")
print("Now we will write four new lines to this file.")
print("What should we write?")
line1 = input("1st line: ")
line2 = input("2nd line: ")
line3 = input("3rd line: ")
line4 = input("4th line: ")

all_lines = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n'
txt.write(all_lines)

txt.close()

rtxt = open(filename, 'r')
print(f"\nHere's {filename} now:")
print(rtxt.read())
print("Goodbye")

rtxt.close()
