#EX 15
#Reading files

#get inputs from command line
from sys import argv
script, filename = argv

#open file
txt = open(filename)
#display contents of file (read file and print)
print(f"Here's your file, {filename}:")
print(txt.read())

#close file
txt.close()

#get filename from user
print("Type the filename again:")
same_filename = input("> ")

#open and read the file again
same_txt = open(same_filename)
print(same_txt.read())

#close file
same_txt.close()
