#EX 20
#Functions and files

from sys import argv
script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0) #starts file back at 0 bytes

def print_a_line(line_count, f):
    print(line_count, f.readline(), end = '')

def print_some_lines(first_line, num_lines, f):
    for first_line in range(first_line, first_line + num_lines):
        print(first_line, f.readline(), end = '')

current_file = open(input_file)

print("Whole file:")
print_all(current_file)

print("Rewind:")
rewind(current_file)

#I feel like this should be in a loop
print("three lines")
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)

#So I made it a loop
print("Again?")
rewind(current_file)
print_some_lines(1,3,current_file)

#Alternatively a loop not in a function
print("Last time:")
current_file.seek(0)
current_line = 1
for current_line in range(1,4):
    print_a_line(current_line, current_file)

current_file.close()
