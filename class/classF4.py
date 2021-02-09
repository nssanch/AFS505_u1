#Class Exercises February 4

from sys import argv
script, filename = argv

#initialize
p_total = 0
p_count = 0
p_min = float("inf")
p_max = float("-inf")

p_file = open(filename)

line = p_file.readline()

while line:
    line = line.strip()
    if (line == "") or (line.find('#') != -1):
        line = p_file.readline()
        continue
    #print(line)
    p = float(line)
    p_total += p
    p_count += 1
    if p < p_min:
        p_min = p
    if p > p_max:
        p_max = p
    line = p_file.readline()

p_ave = p_total / p_count
print(f"Average = {p_ave}\nMin = {p_min}\nMax = {p_max}")
