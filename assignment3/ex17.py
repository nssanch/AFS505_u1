#EX 17
#Copying files
from sys import argv
from os.path import exists
script, from_file, to_file = argv
#open(to_file, 'w').write(open(from_file).read())

print(f"Copying from {from_file} to {to_file}.")

indata = open(from_file).read()

print(f"{from_file} is {len(indata)} bytes long.")

print(f"Does {to_file} already exist? {exists(to_file)}")
print("Ready, hit ENTER to continue or ctrl + C to abort.")
input()

outfile = open(to_file, 'w')
outfile.write(indata)

print("All done")

outfile.close()
